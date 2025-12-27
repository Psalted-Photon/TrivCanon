import './QuizScore.css';

export default function QuizScore({ score, totalQuestions, results, quizMode, onPlayAgain, onChangeThemes }) {
  const percentage = Math.round((score / totalQuestions) * 100);
  
  const getGrade = () => {
    if (percentage >= 90) return { text: 'Excellent!', emoji: '🌟', color: '#38A169' };
    if (percentage >= 75) return { text: 'Great Job!', emoji: '🎉', color: '#4299E1' };
    if (percentage >= 60) return { text: 'Good Effort!', emoji: '👍', color: '#ED8936' };
    return { text: 'Keep Learning!', emoji: '📚', color: '#E53E3E' };
  };

  const grade = getGrade();
  
  // Determine quiz mode label
  const quizModeLabel = quizMode === '10q' ? '10 Question Quiz' 
    : quizMode === '25q' ? '25 Question Quiz' 
    : quizMode === '50q' ? '50 Question Quiz' 
    : 'Quiz';

  // Calculate stats by theme
  const themeStats = {};
  results.forEach(r => {
    if (!themeStats[r.question.theme]) {
      themeStats[r.question.theme] = { correct: 0, total: 0 };
    }
    themeStats[r.question.theme].total++;
    if (r.isCorrect) {
      themeStats[r.question.theme].correct++;
    }
  });

  return (
    <div className="quiz-score">
      <div className="quiz-mode-header">
        <h2>{quizModeLabel} Complete!</h2>
      </div>
      
      <div className="score-banner" style={{ borderColor: grade.color }}>
        <div className="score-emoji">{grade.emoji}</div>
        <div className="score-text" style={{ color: grade.color }}>{grade.text}</div>
        <div className="score-percentage">{percentage}%</div>
        <div className="score-fraction">
          {score} / {totalQuestions} correct
        </div>
      </div>

      <div className="theme-breakdown">
        <h3>Performance by Theme</h3>
        <div className="theme-stats">
          {Object.entries(themeStats).map(([theme, stats]) => (
            <div key={theme} className="theme-stat">
              <span className="theme-name">{theme}</span>
              <div className="theme-bar-container">
                <div 
                  className="theme-bar-fill" 
                  style={{ 
                    width: `${(stats.correct / stats.total) * 100}%`,
                    background: stats.correct === stats.total ? '#38A169' : '#667EEA'
                  }}
                />
              </div>
              <span className="theme-score">{stats.correct}/{stats.total}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="action-buttons">
        <button className="play-again-btn" onClick={onPlayAgain}>
          🔄 Retry Quiz
        </button>
        <button className="change-themes-btn" onClick={onChangeThemes}>
          🎯 New Quiz
        </button>
      </div>
    </div>
  );
}
