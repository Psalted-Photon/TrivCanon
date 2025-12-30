import './QuizQuestion.css';

// Helper function to convert theme name to logo filename
const getThemeLogoNoText = (themeName) => {
  const logoMap = {
    "Miracles": "miraclesnotext.png",
    "Prophets": "prophetsnotext.png",
    "Apostles": "apostlesnotext.png",
    "Kings & Rulers": "kings-rulersnotext.png",
    "Women of Faith": "women-of-faithnotext.png",
    "Battles & Conquests": "battles-conquestsnotext.png",
    "Parables & Teachings": "parables-teachingsnotext.png",
    "Creation & Origins": "creation-originsnotext.png",
    "Prophecy & End Times": "prophecy-end-timesnotext.png",
    "Journeys & Exile": "journeys-exilenotext.png",
    "Festivals & Customs": "festivals-customsnotext.png",
    "Wisdom & Psalms": "wisdom-psalmsnotext.png"
  };
  return logoMap[themeName] || null;
};

export default function QuizQuestion({ question, questionNumber, totalQuestions, onAnswer, onQuit }) {
  const themeLogo = getThemeLogoNoText(question.theme);

  return (
    <div className="quiz-question">
      {/* Large background medallion watermark */}
      {themeLogo && (
        <div className="question-background-medallion">
          <img 
            src={`/images/LogosNoText/${themeLogo}`} 
            alt=""
            className="background-medallion-image"
          />
        </div>
      )}

      <div className="question-header">
        <span className="theme-badge">
          {themeLogo && (
            <img 
              src={`/images/LogosNoText/${themeLogo}`} 
              alt={question.theme}
              className="theme-badge-logo"
              onError={(e) => {
                e.target.style.display = 'none';
                e.target.nextElementSibling.style.display = 'inline';
              }}
            />
          )}
          <span className="theme-badge-text" style={{ display: themeLogo ? 'none' : 'inline' }}>
            {question.theme}
          </span>
        </span>
      </div>

      <div className="question-meta">
        <div className="theme-name-display">
          {question.theme}
        </div>
        <span className="question-counter">
          Question {questionNumber} of {totalQuestions}
        </span>
      </div>

      <div className="progress-bar">
        <div 
          className="progress-fill" 
          style={{ width: `${(questionNumber / totalQuestions) * 100}%` }}
        />
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
