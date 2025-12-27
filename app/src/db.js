/**
 * IndexedDB helper for caching questions offline
 */
import { openDB } from 'idb';

const DB_NAME = 'bible-trivia-db';
const STORE_NAME = 'questions';
const DB_VERSION = 3; // Incremented for new structure

let cachedIndex = null; // Cache the index in memory

export async function initDB() {
  return openDB(DB_NAME, DB_VERSION, {
    upgrade(db) {
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME);
      }
    },
  });
}

export async function saveQuestions(key, questions) {
  const db = await initDB();
  await db.put(STORE_NAME, questions, key);
}

export async function getQuestions(key) {
  const db = await initDB();
  return db.get(STORE_NAME, key);
}

/**
 * Load the question index (cached in memory after first load)
 */
async function loadIndex() {
  if (cachedIndex) {
    return cachedIndex;
  }
  
  const response = await fetch('/questions/index.json');
  cachedIndex = await response.json();
  return cachedIndex;
}

/**
 * Load questions based on theme and difficulty filters
 * @param {Object} options - Filter options
 * @param {string[]} options.themes - Array of theme names to load (e.g., ['Miracles', 'Prophets'])
 * @param {string[]} options.difficulties - Array of difficulties to load (e.g., ['easy', 'medium'])
 * @returns {Promise<Array>} Array of questions matching the filters
 */
export async function loadQuestionsWithCache(options = {}) {
  const { themes = null, difficulties = null } = options;
  
  // Load index
  const index = await loadIndex();
  
  // Filter index based on options
  let filesToLoad = index;
  
  if (themes && themes.length > 0) {
    filesToLoad = filesToLoad.filter(item => themes.includes(item.theme));
  }
  
  if (difficulties && difficulties.length > 0) {
    filesToLoad = filesToLoad.filter(item => difficulties.includes(item.difficulty));
  }
  
  // Load all matching files
  const questionPromises = filesToLoad.map(async (item) => {
    const cacheKey = `${item.themePath}-${item.difficulty}`;
    
    // Try to get from cache first
    let questions = await getQuestions(cacheKey);
    
    // If not in cache or we want fresh data, fetch from network
    if (!questions) {
      const response = await fetch(`/${item.filePath}`);
      questions = await response.json();
      // Cache for offline use
      await saveQuestions(cacheKey, questions);
    }
    
    return questions;
  });
  
  // Wait for all files to load and merge
  const questionArrays = await Promise.all(questionPromises);
  const allQuestions = questionArrays.flat();
  
  return allQuestions;
}
