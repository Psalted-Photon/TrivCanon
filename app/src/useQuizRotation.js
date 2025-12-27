/**
 * Hook for managing shuffled round-robin theme rotation
 */
import { useState, useCallback, useMemo } from 'react';

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
  const [themeIndexInRound, setThemeIndexInRound] = useState(0);
  
  // Create shuffled theme order for current round
  const themeOrder = useMemo(() => {
    if (rotationMode === 'ordered') {
      return selectedThemes;
    }
    // Shuffle themes each round
    return shuffleArray(selectedThemes);
  }, [selectedThemes, currentRound, rotationMode]);
  
  // Filter questions by selected themes and difficulty
  const availableQuestions = useMemo(() => {
    return questions.filter(q => 
      selectedThemes.includes(q.theme) &&
      (difficulty === 'all' || q.difficulty === difficulty)
    );
  }, [questions, selectedThemes, difficulty]);
  
  // Group questions by theme
  const questionsByTheme = useMemo(() => {
    const grouped = {};
    selectedThemes.forEach(theme => {
      grouped[theme] = availableQuestions.filter(q => q.theme === theme);
    });
    return grouped;
  }, [availableQuestions, selectedThemes]);
  
  // Get next question following round-robin pattern
  const getNextQuestion = useCallback(() => {
    if (themeOrder.length === 0) return null;
    
    const currentTheme = themeOrder[themeIndexInRound];
    const themeQuestions = questionsByTheme[currentTheme];
    
    if (!themeQuestions || themeQuestions.length === 0) {
      // Move to next theme if current has no questions
      const nextIndex = (themeIndexInRound + 1) % themeOrder.length;
      if (nextIndex === 0) {
        setCurrentRound(r => r + 1);
      }
      setThemeIndexInRound(nextIndex);
      return getNextQuestion();
    }
    
    // Get random question from current theme
    const randomQuestion = themeQuestions[Math.floor(Math.random() * themeQuestions.length)];
    
    // Move to next theme in round
    const nextIndex = (themeIndexInRound + 1) % themeOrder.length;
    if (nextIndex === 0) {
      // Completed a full round, reshuffle for next round
      setCurrentRound(r => r + 1);
    }
    setThemeIndexInRound(nextIndex);
    
    return randomQuestion;
  }, [themeOrder, themeIndexInRound, questionsByTheme]);
  
  const reset = useCallback(() => {
    setCurrentRound(0);
    setThemeIndexInRound(0);
  }, []);
  
  return {
    getNextQuestion,
    reset,
    currentTheme: themeOrder[themeIndexInRound],
    totalQuestions: availableQuestions.length
  };
}
