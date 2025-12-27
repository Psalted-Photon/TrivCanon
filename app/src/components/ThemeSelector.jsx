import { useState } from 'react';
import './ThemeSelector.css';

const THEMES = [
  { name: "Miracles", icon: "✨🍷", color: "#9F7AEA" },
  { name: "Prophets", icon: "🗣️📜", color: "#4299E1" },
  { name: "Apostles", icon: "🙋‍♂️🙋‍♀️", color: "#48BB78" },
  { name: "Kings & Rulers", icon: "👑🏰", color: "#ED8936" },
  { name: "Women of Faith", icon: "👸🧕", color: "#F56565" },
  { name: "Battles & Conquests", icon: "⚔️🏆", color: "#805AD5" },
  { name: "Parables & Teachings", icon: "💬👨‍🏫", color: "#38B2AC" },
  { name: "Creation & Origins", icon: "🌍🧬", color: "#68D391" },
  { name: "Prophecy & End Times", icon: "📯⚖️", color: "#FC8181" },
  { name: "Journeys & Exile", icon: "🚶🏜️", color: "#F6AD55" },
  { name: "Festivals & Customs", icon: "🎉🕎", color: "#B794F4" },
  { name: "Wisdom & Psalms", icon: "📖🎼", color: "#63B3ED" }
];

export default function ThemeSelector({ onStart, totalQuestions }) {
  const [selectedThemes, setSelectedThemes] = useState(THEMES.map(t => t.name));
  const [difficulty, setDifficulty] = useState('all');
  const [quizMode, setQuizMode] = useState('10q');
  const [rotationMode, setRotationMode] = useState('shuffled');

  const toggleTheme = (themeName) => {
    setSelectedThemes(prev => 
      prev.includes(themeName)
        ? prev.filter(t => t !== themeName)
        : [...prev, themeName]
    );
  };

  const selectAll = () => setSelectedThemes(THEMES.map(t => t.name));
  const deselectAll = () => setSelectedThemes([]);

  const handleStart = () => {
    if (selectedThemes.length > 0) {
      onStart(selectedThemes, rotationMode, difficulty, quizMode);
    }
  };

  return (
    <div className="theme-selector">
      <div className="header">
        <p>Select themes for your quiz</p>
      </div>

      <div className="controls">
        <button onClick={selectAll} className="control-btn">Select All</button>
        <button onClick={deselectAll} className="control-btn">Deselect All</button>
      </div>

      <div className="themes-grid">
        {THEMES.map(theme => (
          <div
            key={theme.name}
            className={`theme-card ${selectedThemes.includes(theme.name) ? 'selected' : ''}`}
            onClick={() => toggleTheme(theme.name)}
            style={{ '--theme-color': theme.color }}
          >
            <div className="theme-icon">{theme.icon}</div>
            <div className="theme-name">{theme.name}</div>
            <div className="checkbox">
              {selectedThemes.includes(theme.name) && '✓'}
            </div>
          </div>
        ))}
      </div>

      <div className="difficulty-filter">
        <h3>Difficulty Level</h3>
        <div className="difficulty-options">
          <label className="difficulty-label">
            <input
              type="radio"
              value="all"
              checked={difficulty === 'all'}
              onChange={(e) => setDifficulty(e.target.value)}
            />
            <span>All</span>
          </label>
          <label className="difficulty-label">
            <input
              type="radio"
              value="easy"
              checked={difficulty === 'easy'}
              onChange={(e) => setDifficulty(e.target.value)}
            />
            <span>Easy</span>
          </label>
          <label className="difficulty-label">
            <input
              type="radio"
              value="medium"
              checked={difficulty === 'medium'}
              onChange={(e) => setDifficulty(e.target.value)}
            />
            <span>Medium</span>
          </label>
          <label className="difficulty-label">
            <input
              type="radio"
              value="hard"
              checked={difficulty === 'hard'}
              onChange={(e) => setDifficulty(e.target.value)}
            />
            <span>Hard</span>
          </label>
        </div>
      </div>

      <div className="quiz-mode-filter">
        <h3>Quiz Mode</h3>
        <div className="quiz-mode-options">
          <label className="quiz-mode-label">
            <input
              type="radio"
              value="10q"
              checked={quizMode === '10q'}
              onChange={(e) => setQuizMode(e.target.value)}
            />
            <span>10 Questions</span>
          </label>
          <label className="quiz-mode-label">
            <input
              type="radio"
              value="25q"
              checked={quizMode === '25q'}
              onChange={(e) => setQuizMode(e.target.value)}
            />
            <span>25 Questions</span>
          </label>
          <label className="quiz-mode-label">
            <input
              type="radio"
              value="50q"
              checked={quizMode === '50q'}
              onChange={(e) => setQuizMode(e.target.value)}
            />
            <span>50 Questions</span>
          </label>
          <label className="quiz-mode-label">
            <input
              type="radio"
              value="endless"
              checked={quizMode === 'endless'}
              onChange={(e) => setQuizMode(e.target.value)}
            />
            <span>Endless</span>
          </label>
        </div>
      </div>

      <div className="rotation-mode">
        <label className="mode-label">
          <input
            type="radio"
            value="ordered"
            checked={rotationMode === 'ordered'}
            onChange={(e) => setRotationMode(e.target.value)}
          />
          <span>Ordered Rotation</span>
        </label>
        <label className="mode-label">
          <input
            type="radio"
            value="shuffled"
            checked={rotationMode === 'shuffled'}
            onChange={(e) => setRotationMode(e.target.value)}
          />
          <span>Shuffled Round-Robin</span>
        </label>
      </div>

      <button 
        className="start-btn" 
        onClick={handleStart}
        disabled={selectedThemes.length === 0}
      >
        Start Quiz ({selectedThemes.length} theme{selectedThemes.length !== 1 ? 's' : ''})
      </button>
    </div>
  );
}
