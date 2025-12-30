import { useState, useEffect } from 'react';
import { loadQuestionsWithCache } from './db';
import { useQuizRotation } from './useQuizRotation';
import ThemeSelector from './components/ThemeSelector';
import QuizQuestion from './components/QuizQuestion';
import QuestionFeedback from './components/QuestionFeedback';
import QuizScore from './components/QuizScore';
import './App.css';

// Preload logo images for smooth transitions
const preloadLogos = () => {
  const logoFiles = [
    'miracles.png', 'prophets.png', 'apostles.png', 'kings-rulers.png',
    'women-of-faith.png', 'battles-conquests.png', 'parables-teachings.png',
    'creation-origins.png', 'prophecy-end-times.png', 'journeys-exile.png',
    'festivals-customs.png', 'wisdom-psalms.png'
  ];
  
  const logoNoTextFiles = [
    'miraclesnotext.png', 'prophetsnotext.png', 'apostlesnotext.png', 'kings-rulersnotext.png',
    'women-of-faithnotext.png', 'battles-conquestsnotext.png', 'parables-teachingsnotext.png',
    'creation-originsnotext.png', 'prophecy-end-timesnotext.png', 'journeys-exilenotext.png',
    'festivals-customsnotext.png', 'wisdom-psalmsnotext.png'
  ];
  
  // Preload Logos
  logoFiles.forEach(file => {
    const img = new Image();
    img.src = `/images/Logos/${file}`;
  });
  
  // Preload LogosNoText
  logoNoTextFiles.forEach(file => {
    const img = new Image();
    img.src = `/images/LogosNoText/${file}`;
  });
};

// Shuffle answer choices and update correctIndex
function shuffleChoices(question) {
  const shuffled = { ...question };
  const correctAnswer = question.choices[question.correctIndex];
  
  // Create array of indices and shuffle
  const indices = question.choices.map((_, i) => i);
  for (let i = indices.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [indices[i], indices[j]] = [indices[j], indices[i]];
  }
  
  // Reorder choices and find new correct index
  shuffled.choices = indices.map(i => question.choices[i]);
  shuffled.correctIndex = shuffled.choices.indexOf(correctAnswer);
  
  return shuffled;
}

export default function App() {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [screen, setScreen] = useState('theme-select'); // 'theme-select', 'question', 'feedback', 'score'
  const [selectedThemes, setSelectedThemes] = useState([]);
  const [selectedDifficulty, setSelectedDifficulty] = useState('all');
  const [quizMode, setQuizMode] = useState('endless');
  const [maxQuestions, setMaxQuestions] = useState(null);
  const [rotationMode, setRotationMode] = useState('shuffled');
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [questionNumber, setQuestionNumber] = useState(1);
  const [userAnswer, setUserAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [results, setResults] = useState([]);

  const { getNextQuestion, reset } = useQuizRotation(selectedThemes, questions, rotationMode, selectedDifficulty);

  useEffect(() => {
    // Preload logo images
    preloadLogos();
    
    // Load all questions initially to populate theme selector
    loadQuestionsWithCache()
      .then(data => {
        console.log('Loaded questions:', data.length, 'total');
        const byTheme = data.reduce((acc, q) => {
          acc[q.theme] = (acc[q.theme] || 0) + 1;
          return acc;
        }, {});
        console.log('Questions by theme:', byTheme);
        setQuestions(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to load questions:', err);
        setLoading(false);
      });
  }, []);

  const handleStartQuiz = async (themes, mode, difficulty, quizModeType) => {
    setSelectedThemes(themes);
    setSelectedDifficulty(difficulty);
    setQuizMode(quizModeType);
    
    // Set max questions based on quiz mode
    const maxQ = quizModeType === '10q' ? 10 : quizModeType === '25q' ? 25 : quizModeType === '50q' ? 50 : null;
    setMaxQuestions(maxQ);
    
    setRotationMode(mode);
    setQuestionNumber(1);
    setScore(0);
    setResults([]);
    
    // Load filtered questions based on selected themes and difficulty
    const difficulties = difficulty === 'all' ? null : [difficulty];
    const filteredQuestions = await loadQuestionsWithCache({ 
      themes: themes.length > 0 ? themes : null,
      difficulties 
    });
    
    console.log(`Loaded ${filteredQuestions.length} questions for selected filters`);
    
    // Update questions state
    setQuestions(filteredQuestions);
    
    // We need to wait for the next render cycle, so use a small timeout
    // or better yet, let's trigger the first question in a useEffect
    // For now, let's use setTimeout to ensure questions are updated
    setTimeout(() => {
      reset();
      const firstQuestion = getNextQuestion();
      if (firstQuestion) {
        setCurrentQuestion(shuffleChoices(firstQuestion));
        setScreen('question');
      }
    }, 0);
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
    // Check if we've reached the max questions for this quiz mode
    if (maxQuestions && questionNumber >= maxQuestions) {
      setScreen('score');
      return;
    }
    
    const nextQuestion = getNextQuestion();
    
    if (nextQuestion) {
      setCurrentQuestion(shuffleChoices(nextQuestion));
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
      setCurrentQuestion(shuffleChoices(firstQuestion));
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

  // Calculate total questions available for selected themes and difficulty
  const totalQuestions = questions.filter(q => 
    selectedThemes.includes(q.theme) && 
    (selectedDifficulty === 'all' || q.difficulty === selectedDifficulty)
  ).length;

  return (
    <div className="app">
      <header className="app-header">
        {screen === 'theme-select' ? (
          <img 
            src="/images/TrivCanonTitle.png" 
            alt="TrivCanon - Master the Canon" 
            className="app-logo"
          />
        ) : (
          <div className="app-title-text">
            <h1>TrivCanon</h1>
            <p className="subtitle">Twelve tribes, one truth.</p>
          </div>
        )}
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
            totalQuestions={maxQuestions || totalQuestions}
            onAnswer={handleAnswer}
            onQuit={handleChangeThemes}
          />
        )}

        {screen === 'feedback' && currentQuestion && userAnswer !== null && (
          <QuestionFeedback
            question={currentQuestion}
            userAnswer={userAnswer}
            onNext={handleNext}
            onQuit={handleChangeThemes}
          />
        )}

        {screen === 'score' && (
          <QuizScore
            score={score}
            totalQuestions={results.length}
            results={results}
            quizMode={quizMode}
            onPlayAgain={handlePlayAgain}
            onChangeThemes={handleChangeThemes}
          />
        )}
      </main>

      <footer className="app-footer">
        <p>Using the King James Version (KJV)</p>
        <p className="question-count">{questions.length} questions available</p>
      </footer>
    </div>
  );
}
