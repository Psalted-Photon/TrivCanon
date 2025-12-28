/**
 * Hook for managing shuffled round-robin theme rotation with no repeats
 * Ensures all themes, difficulties, and questions are used before any repeat
 */
import { useState, useCallback, useMemo, useRef } from 'react';

function shuffleArray(array) {
  const shuffled = [...array];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

export function useQuizRotation(selectedThemes, questions, rotationMode = 'shuffled', difficulty = 'all') {
  const [currentRound, setCurrentRound] = useState(0);
  
  // For shuffled mode: track used items to prevent repeats
  const usedThemesInCycle = useRef(new Set());
  const usedDifficultiesInCycle = useRef(new Set());
  const usedQuestionsPerCombo = useRef(new Map()); // key: "theme-difficulty", value: Set of used question IDs
  
  // For shuffled mode: shuffled arrays that get regenerated when exhausted
  const shuffledThemes = useRef([]);
  const shuffledDifficulties = useRef([]);
  const shuffledQuestionsByCombo = useRef(new Map()); // key: "theme-difficulty", value: shuffled array
  
  // For ordered mode: simple indices
  const [themeIndexInRound, setThemeIndexInRound] = useState(0);
  const questionIndicesByTheme = useRef(new Map()); // Track question index per theme
  
  // Difficulty order when "all" is selected
  const difficultyOrder = ['easy', 'medium', 'hard'];
  
  // Filter questions by selected themes and difficulty
  const availableQuestions = useMemo(() => {
    return questions.filter(q => 
      selectedThemes.includes(q.theme) &&
      (difficulty === 'all' || q.difficulty === difficulty)
    );
  }, [questions, selectedThemes, difficulty]);
  
  // Group questions by theme and difficulty combo
  const questionsByCombo = useMemo(() => {
    const grouped = new Map();
    
    availableQuestions.forEach(q => {
      const key = `${q.theme}-${q.difficulty}`;
      if (!grouped.has(key)) {
        grouped.set(key, []);
      }
      grouped.get(key).push(q);
    });
    
    // Sort questions in each combo by ID for ordered mode
    grouped.forEach((questions, key) => {
      questions.sort((a, b) => {
        if (typeof a.id === 'string' && typeof b.id === 'string') {
          return a.id.localeCompare(b.id);
        }
        return 0;
      });
    });
    
    return grouped;
  }, [availableQuestions]);
  
  // For ordered mode: group by theme
  const questionsByTheme = useMemo(() => {
    const grouped = {};
    selectedThemes.forEach(theme => {
      const themeQuestions = availableQuestions.filter(q => q.theme === theme);
      themeQuestions.sort((a, b) => {
        if (typeof a.id === 'string' && typeof b.id === 'string') {
          return a.id.localeCompare(b.id);
        }
        return 0;
      });
      grouped[theme] = themeQuestions;
    });
    return grouped;
  }, [availableQuestions, selectedThemes]);
  
  // Get next question for SHUFFLED mode
  const getNextQuestionShuffled = useCallback(() => {
    // Step 1: Select a theme that hasn't been used in current cycle
    if (shuffledThemes.current.length === 0 || usedThemesInCycle.current.size === selectedThemes.length) {
      // All themes used or first time - reshuffle
      shuffledThemes.current = shuffleArray(selectedThemes);
      usedThemesInCycle.current.clear();
    }
    
    // Get next unused theme
    let selectedTheme = null;
    for (const theme of shuffledThemes.current) {
      if (!usedThemesInCycle.current.has(theme)) {
        selectedTheme = theme;
        usedThemesInCycle.current.add(theme);
        break;
      }
    }
    
    if (!selectedTheme) return null;
    
    // Step 2: Select a difficulty that hasn't been used in current cycle
    const availableDifficulties = difficulty === 'all' ? difficultyOrder : [difficulty];
    
    if (shuffledDifficulties.current.length === 0 || usedDifficultiesInCycle.current.size === availableDifficulties.length) {
      // All difficulties used or first time - reshuffle
      shuffledDifficulties.current = shuffleArray(availableDifficulties);
      usedDifficultiesInCycle.current.clear();
    }
    
    // Get next unused difficulty
    let selectedDifficulty = null;
    for (const diff of shuffledDifficulties.current) {
      if (!usedDifficultiesInCycle.current.has(diff)) {
        selectedDifficulty = diff;
        usedDifficultiesInCycle.current.add(diff);
        break;
      }
    }
    
    if (!selectedDifficulty) return null;
    
    // Step 3: Select a question from this theme-difficulty combo that hasn't been used
    const comboKey = `${selectedTheme}-${selectedDifficulty}`;
    const comboQuestions = questionsByCombo.get(comboKey);
    
    if (!comboQuestions || comboQuestions.length === 0) {
      // This combo has no questions, try again with different theme/difficulty
      return getNextQuestionShuffled();
    }
    
    // Initialize tracking for this combo if needed
    if (!usedQuestionsPerCombo.current.has(comboKey)) {
      usedQuestionsPerCombo.current.set(comboKey, new Set());
    }
    
    const usedQuestions = usedQuestionsPerCombo.current.get(comboKey);
    
    // Check if all questions in this combo have been used
    if (usedQuestions.size === comboQuestions.length) {
      // All questions used - clear and reshuffle
      usedQuestions.clear();
      shuffledQuestionsByCombo.current.delete(comboKey);
    }
    
    // Get or create shuffled question array for this combo
    if (!shuffledQuestionsByCombo.current.has(comboKey)) {
      shuffledQuestionsByCombo.current.set(comboKey, shuffleArray(comboQuestions));
    }
    
    const shuffledQuestions = shuffledQuestionsByCombo.current.get(comboKey);
    
    // Find first unused question
    let selectedQuestion = null;
    for (const q of shuffledQuestions) {
      if (!usedQuestions.has(q.id)) {
        selectedQuestion = q;
        usedQuestions.add(q.id);
        break;
      }
    }
    
    // If we couldn't find a question (shouldn't happen), reshuffle and try again
    if (!selectedQuestion && shuffledQuestions.length > 0) {
      usedQuestions.clear();
      shuffledQuestionsByCombo.current.set(comboKey, shuffleArray(comboQuestions));
      selectedQuestion = shuffledQuestionsByCombo.current.get(comboKey)[0];
      usedQuestions.add(selectedQuestion.id);
    }
    
    return selectedQuestion;
  }, [selectedThemes, difficulty, difficultyOrder, questionsByCombo]);
  
  // Get next question for ORDERED mode
  const getNextQuestionOrdered = useCallback(() => {
    if (selectedThemes.length === 0) return null;
    
    const currentTheme = selectedThemes[themeIndexInRound];
    const themeQuestions = questionsByTheme[currentTheme];
    
    if (!themeQuestions || themeQuestions.length === 0) {
      // Move to next theme
      const nextIndex = (themeIndexInRound + 1) % selectedThemes.length;
      setThemeIndexInRound(nextIndex);
      if (nextIndex === 0) {
        setCurrentRound(r => r + 1);
      }
      return getNextQuestionOrdered();
    }
    
    // Get or initialize the question index for this specific theme
    if (!questionIndicesByTheme.current.has(currentTheme)) {
      questionIndicesByTheme.current.set(currentTheme, 0);
    }
    
    const questionIndex = questionIndicesByTheme.current.get(currentTheme);
    const selectedQuestion = themeQuestions[questionIndex];
    
    // Increment this theme's question index
    questionIndicesByTheme.current.set(currentTheme, questionIndex + 1);
    
    // Move to next theme
    const nextIndex = (themeIndexInRound + 1) % selectedThemes.length;
    setThemeIndexInRound(nextIndex);
    if (nextIndex === 0) {
      setCurrentRound(r => r + 1);
    }
    
    return selectedQuestion;
  }, [selectedThemes, themeIndexInRound, questionsByTheme]);
  
  // Main getNextQuestion function
  const getNextQuestion = useCallback(() => {
    if (rotationMode === 'shuffled') {
      return getNextQuestionShuffled();
    } else {
      return getNextQuestionOrdered();
    }
  }, [rotationMode, getNextQuestionShuffled, getNextQuestionOrdered]);
  
  const reset = useCallback(() => {
    setCurrentRound(0);
    setThemeIndexInRound(0);
    questionIndicesByTheme.current.clear();
    
    // Clear shuffled mode tracking
    usedThemesInCycle.current.clear();
    usedDifficultiesInCycle.current.clear();
    usedQuestionsPerCombo.current.clear();
    shuffledThemes.current = [];
    shuffledDifficulties.current = [];
    shuffledQuestionsByCombo.current.clear();
  }, []);
  
  return {
    getNextQuestion,
    reset,
    currentTheme: rotationMode === 'ordered' ? selectedThemes[themeIndexInRound] : null,
    totalQuestions: availableQuestions.length
  };
}
