import './QuestionFeedback.css';

export default function QuestionFeedback({ question, userAnswer, onNext, onQuit }) {
  const isCorrect = userAnswer === question.correctIndex;
  const correctAnswer = question.choices[question.correctIndex];
  const userAnswerText = question.choices[userAnswer];
  
  // Get verse text from embedded data
  const verseText = question.verses?.kjv || '';
  const hasVerse = Boolean(verseText);

  return (
    <div className="question-feedback">
      <div className="question-display">
        <div className="theme-badge">{question.theme}</div>
        <div className="question-text">{question.question}</div>
      </div>

      <div className={`result-banner ${isCorrect ? 'correct' : 'incorrect'}`}>
        <div className="result-icon">
          {isCorrect ? '✓' : '✗'}
        </div>
        <div className="result-text">
          {isCorrect ? 'Correct!' : 'Incorrect'}
        </div>
      </div>

      {!isCorrect && (
        <div className="answer-comparison">
          <div className="user-answer wrong">
            <span className="label">Your answer:</span>
            <span className="value">{userAnswerText}</span>
          </div>
          <div className="correct-answer">
            <span className="label">Correct answer:</span>
            <span className="value">{correctAnswer}</span>
          </div>
        </div>
      )}

      {isCorrect && (
        <div className="correct-answer-display">
          <span className="checkmark">✓</span> {correctAnswer}
        </div>
      )}

      <div className="explanation">
        <div className="explanation-title">Explanation</div>
        <p>{question.explanation}</p>
        {hasVerse && (
          <div className="verse-text">
            <div className="scripture-ref">
              📖 {question.reference.book} {question.reference.chapter}:{question.reference.verse}
            </div>
            <em>"{verseText}"</em>
          </div>
        )}
      </div>

      <button className="next-btn" onClick={onNext}>
        Next Question →
      </button>

      <button className="quit-btn" onClick={onQuit}>
        ← Main Menu
      </button>
    </div>
  );
}
