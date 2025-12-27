/**
 * IndexedDB helper for caching questions offline
 */
import { openDB } from 'idb';

const DB_NAME = 'bible-trivia-db';
const STORE_NAME = 'questions';
const DB_VERSION = 2;

export async function initDB() {
  return openDB(DB_NAME, DB_VERSION, {
    upgrade(db) {
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME);
      }
    },
  });
}

export async function saveQuestions(questions) {
  const db = await initDB();
  await db.put(STORE_NAME, questions, 'all-questions');
}

export async function getQuestions() {
  const db = await initDB();
  return db.get(STORE_NAME, 'all-questions');
}

export async function loadQuestionsWithCache() {
  // Always fetch from network to get latest questions
  const response = await fetch('/questions.json');
  const questions = await response.json();
  
  // Cache for offline use
  await saveQuestions(questions);
  
  return questions;
}
