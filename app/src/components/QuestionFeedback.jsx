import { useState, useEffect } from 'react';
import './QuestionFeedback.css';

export default function QuestionFeedback({ question, userAnswer, onNext, onQuit }) {
  const isCorrect = userAnswer === question.correctIndex;
  const correctAnswer = question.choices[question.correctIndex];
  const userAnswerText = question.choices[userAnswer];
  const [verseText, setVerseText] = useState('');
  const [loadingVerse, setLoadingVerse] = useState(true);

  useEffect(() => {
    // Fetch the KJV verse text from bible-api.com
    const fetchVerse = async () => {
      try {
        const { book, chapter, verse } = question.reference;
        // bible-api.com format: https://bible-api.com/book+chapter:verse?translation=kjv
        const response = await fetch(
          `https://bible-api.com/${encodeURIComponent(book)}+${chapter}:${verse}?translation=kjv`
        );
        const data = await response.json();
        console.log('Bible API response:', data);
        setVerseText(data.text?.trim() || '');
      } catch (error) {
        console.error('Error fetching verse:', error);
        setVerseText('');
      } finally {
        setLoadingVerse(false);
      }
    };

    fetchVerse();
  }, [question.reference]);

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
        {loadingVerse ? (
          <div className="verse-text loading">Loading verse...</div>
        ) : verseText ? (
          <div className="verse-text">
            <div className="scripture-ref">
              📖 {question.reference.book} {question.reference.chapter}:{question.reference.verse}
            </div>
            <em>"{verseText}"</em>
          </div>
        ) : null}
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
