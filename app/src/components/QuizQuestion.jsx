import './QuizQuestion.css';

export default function QuizQuestion({ question, questionNumber, totalQuestions, onAnswer, onQuit }) {
  return (
    <div className="quiz-question">
      <div className="progress-bar">
        <div 
          className="progress-fill" 
          style={{ width: `${(questionNumber / totalQuestions) * 100}%` }}
        />
      </div>

      <div className="question-header">
        <span className="theme-badge">{question.theme}</span>
        <span className="question-counter">
          Question {questionNumber} of {totalQuestions}
        </span>
      </div>

      <div className="question-text">
        {question.question}
      </div>

      <div className="choices">
        {question.choices.map((choice, index) => (
          <button
            key={index}
            className="choice-btn"
            onClick={() => onAnswer(index)}
          >
            {choice}
          </button>
        ))}
      </div>

      <div className="difficulty-indicator">
        <span className={`difficulty ${question.difficulty}`}>
          {question.difficulty.toUpperCase()}
        </span>
      </div>

      <button className="quit-btn" onClick={onQuit}>
        ← Main Menu
      </button>
    </div>
  );
}
