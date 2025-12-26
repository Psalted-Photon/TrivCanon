import { useState, useEffect } from 'react';
import { loadQuestionsWithCache } from './db';
import { useQuizRotation } from './useQuizRotation';
import ThemeSelector from './components/ThemeSelector';
import QuizQuestion from './components/QuizQuestion';
import QuestionFeedback from './components/QuestionFeedback';
import QuizScore from './components/QuizScore';
import './App.css';

export default function App() {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [screen, setScreen] = useState('theme-select'); // 'theme-select', 'question', 'feedback', 'score'
  const [selectedThemes, setSelectedThemes] = useState([]);
  const [rotationMode, setRotationMode] = useState('shuffled');
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [questionNumber, setQuestionNumber] = useState(1);
  const [userAnswer, setUserAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [results, setResults] = useState([]);

  const { getNextQuestion, reset } = useQuizRotation(selectedThemes, questions, rotationMode);

  useEffect(() => {
    loadQuestionsWithCache()
      .then(data => {
        setQuestions(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load questions:', err);
        setLoading(false);
      });
  }, []);

  const handleStartQuiz = (themes, mode) => {
    setSelectedThemes(themes);
    setRotationMode(mode);
    setQuestionNumber(1);
    setScore(0);
    setResults([]);
    reset();
    
    // Get first question
    const firstQuestion = getNextQuestion();
    if (firstQuestion) {
      setCurrentQuestion(firstQuestion);
      setScreen('question');
    }
  };

  const handleAnswer = (answerIndex) => {
    setUserAnswer(answerIndex);
    const isCorrect = answerIndex === currentQuestion.correctIndex;
    
    if (isCorrect) {
      setScore(score + 1);
    }

    setResults([
      ...results,
      {
        question: currentQuestion,
        userAnswer: answerIndex,
        isCorrect
      }
    ]);

    setScreen('feedback');
  };

  const handleNext = () => {
    const nextQuestion = getNextQuestion();
    
    if (nextQuestion) {
      setCurrentQuestion(nextQuestion);
      setUserAnswer(null);
      setQuestionNumber(questionNumber + 1);
      setScreen('question');
    } else {
      // Quiz complete
      setScreen('score');
    }
  };

  const handlePlayAgain = () => {
    setQuestionNumber(1);
    setScore(0);
    setResults([]);
    reset();
    
    const firstQuestion = getNextQuestion();
    if (firstQuestion) {
      setCurrentQuestion(firstQuestion);
      setUserAnswer(null);
      setScreen('question');
    }
  };

  const handleChangeThemes = () => {
    setScreen('theme-select');
    setSelectedThemes([]);
    setQuestionNumber(1);
    setScore(0);
    setResults([]);
    setCurrentQuestion(null);
    setUserAnswer(null);
  };

  if (loading) {
    return (
      <div className="app-loading">
        <div className="loading-spinner"></div>
        <p>Loading TrivCanon...</p>
      </div>
    );
  }

  // Calculate total questions available for selected themes
  const totalQuestions = questions.filter(q => selectedThemes.includes(q.theme)).length;

  return (
    <div className="app">
      <header className="app-header">
        <h1><span className="logo-mark">TC</span> TrivCanon</h1>
        <p className="app-subtitle">Master the Canon</p>
      </header>

      <main className="app-main">
        {screen === 'theme-select' && (
          <ThemeSelector
            allQuestions={questions}
            onStart={handleStartQuiz}
          />
        )}

        {screen === 'question' && currentQuestion && (
          <QuizQuestion
            question={currentQuestion}
            questionNumber={questionNumber}
            totalQuestions={totalQuestions}
            onAnswer={handleAnswer}
          />
        )}

        {screen === 'feedback' && currentQuestion && userAnswer !== null && (
          <QuestionFeedback
            question={currentQuestion}
            userAnswer={userAnswer}
            onNext={handleNext}
          />
        )}

        {screen === 'score' && (
          <QuizScore
            score={score}
            totalQuestions={results.length}
            results={results}
            onPlayAgain={handlePlayAgain}
            onChangeThemes={handleChangeThemes}
          />
        )}
      </main>

      <footer className="app-footer">
        <p>Using the King James Version (KJV)</p>
      </footer>
    </div>
  );
}
