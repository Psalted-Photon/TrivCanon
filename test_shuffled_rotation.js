/**
 * Test to verify shuffled round-robin prevents repeats
 */

// Simulate the shuffled logic
function shuffleArray(array) {
  const shuffled = [...array];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

// Test data
const testQuestions = [
  // Miracles - Easy
  { id: 'MIR-E-0001', theme: 'Miracles', difficulty: 'easy', question: 'Q1' },
  { id: 'MIR-E-0002', theme: 'Miracles', difficulty: 'easy', question: 'Q2' },
  { id: 'MIR-E-0003', theme: 'Miracles', difficulty: 'easy', question: 'Q3' },
  // Miracles - Medium
  { id: 'MIR-M-0001', theme: 'Miracles', difficulty: 'medium', question: 'Q4' },
  { id: 'MIR-M-0002', theme: 'Miracles', difficulty: 'medium', question: 'Q5' },
  // Prophets - Easy
  { id: 'PRO-E-0001', theme: 'Prophets', difficulty: 'easy', question: 'Q6' },
  { id: 'PRO-E-0002', theme: 'Prophets', difficulty: 'easy', question: 'Q7' },
  { id: 'PRO-E-0003', theme: 'Prophets', difficulty: 'easy', question: 'Q8' },
  // Prophets - Medium
  { id: 'PRO-M-0001', theme: 'Prophets', difficulty: 'medium', question: 'Q9' },
  { id: 'PRO-M-0002', theme: 'Prophets', difficulty: 'medium', question: 'Q10' },
  // Apostles - Easy
  { id: 'APO-E-0001', theme: 'Apostles', difficulty: 'easy', question: 'Q11' },
  { id: 'APO-E-0002', theme: 'Apostles', difficulty: 'easy', question: 'Q12' },
  // Apostles - Medium  
  { id: 'APO-M-0001', theme: 'Apostles', difficulty: 'medium', question: 'Q13' },
  { id: 'APO-M-0002', theme: 'Apostles', difficulty: 'medium', question: 'Q14' },
];

const selectedThemes = ['Miracles', 'Prophets', 'Apostles'];
const difficulty = 'all';
const difficultyOrder = ['easy', 'medium', 'hard'];

// Group questions by theme-difficulty combo
const questionsByCombo = new Map();
testQuestions.forEach(q => {
  const key = `${q.theme}-${q.difficulty}`;
  if (!questionsByCombo.has(key)) {
    questionsByCombo.set(key, []);
  }
  questionsByCombo.get(key).push(q);
});

// Simulation state
let usedThemesInCycle = new Set();
let usedDifficultiesInCycle = new Set();
let usedQuestionsPerCombo = new Map();
let shuffledThemes = [];
let shuffledDifficulties = [];
let shuffledQuestionsByCombo = new Map();

function getNextQuestionShuffled() {
  // Step 1: Select theme
  if (shuffledThemes.length === 0 || usedThemesInCycle.size === selectedThemes.length) {
    shuffledThemes = shuffleArray(selectedThemes);
    usedThemesInCycle.clear();
    console.log('  🔄 Theme cycle complete - reshuffled themes:', shuffledThemes);
  }
  
  let selectedTheme = null;
  for (const theme of shuffledThemes) {
    if (!usedThemesInCycle.has(theme)) {
      selectedTheme = theme;
      usedThemesInCycle.add(theme);
      break;
    }
  }
  
  if (!selectedTheme) return null;
  
  // Step 2: Select difficulty
  const availableDifficulties = difficulty === 'all' ? difficultyOrder : [difficulty];
  
  if (shuffledDifficulties.length === 0 || usedDifficultiesInCycle.size === availableDifficulties.length) {
    shuffledDifficulties = shuffleArray(availableDifficulties);
    usedDifficultiesInCycle.clear();
    console.log('  🔄 Difficulty cycle complete - reshuffled difficulties:', shuffledDifficulties);
  }
  
  let selectedDifficulty = null;
  for (const diff of shuffledDifficulties) {
    if (!usedDifficultiesInCycle.has(diff)) {
      selectedDifficulty = diff;
      usedDifficultiesInCycle.add(diff);
      break;
    }
  }
  
  if (!selectedDifficulty) return null;
  
  // Step 3: Select question
  const comboKey = `${selectedTheme}-${selectedDifficulty}`;
  const comboQuestions = questionsByCombo.get(comboKey);
  
  if (!comboQuestions || comboQuestions.length === 0) {
    return getNextQuestionShuffled();
  }
  
  if (!usedQuestionsPerCombo.has(comboKey)) {
    usedQuestionsPerCombo.set(comboKey, new Set());
  }
  
  const usedQuestions = usedQuestionsPerCombo.get(comboKey);
  
  if (usedQuestions.size === comboQuestions.length) {
    usedQuestions.clear();
    shuffledQuestionsByCombo.delete(comboKey);
    console.log(`  🔄 All questions used in ${comboKey} - reshuffling`);
  }
  
  if (!shuffledQuestionsByCombo.has(comboKey)) {
    shuffledQuestionsByCombo.set(comboKey, shuffleArray(comboQuestions));
  }
  
  const shuffledQuestions = shuffledQuestionsByCombo.get(comboKey);
  
  let selectedQuestion = null;
  for (const q of shuffledQuestions) {
    if (!usedQuestions.has(q.id)) {
      selectedQuestion = q;
      usedQuestions.add(q.id);
      break;
    }
  }
  
  return selectedQuestion;
}

console.log('='.repeat(80));
console.log('TESTING SHUFFLED ROUND-ROBIN - NO REPEATS VERIFICATION');
console.log('='.repeat(80));
console.log(`\nTest Setup:`);
console.log(`  Themes: ${selectedThemes.join(', ')}`);
console.log(`  Difficulties: ${difficultyOrder.join(', ')}`);
console.log(`  Total Questions: ${testQuestions.length}`);
console.log(`  Question Combos: ${questionsByCombo.size}`);

console.log('\n' + '-'.repeat(80));
console.log('Getting next 20 questions - watch for patterns:');
console.log('-'.repeat(80));

const results = [];
for (let i = 1; i <= 20; i++) {
  const q = getNextQuestionShuffled();
  if (q) {
    results.push(q);
    console.log(`${i.toString().padStart(2)}. ${q.id.padEnd(12)} | ${q.theme.padEnd(15)} | ${q.difficulty.padEnd(8)} | ${q.question}`);
  }
}

console.log('\n' + '='.repeat(80));
console.log('VERIFICATION CHECKS');
console.log('='.repeat(80));

// Check 1: Count theme appearances in first N questions
const checkSize = Math.min(results.length, selectedThemes.length * 2);
const themeCountsInWindow = {};
selectedThemes.forEach(t => themeCountsInWindow[t] = 0);

for (let i = 0; i < checkSize; i++) {
  themeCountsInWindow[results[i].theme]++;
}

console.log(`\nCheck 1: Theme distribution in first ${checkSize} questions`);
Object.entries(themeCountsInWindow).forEach(([theme, count]) => {
  console.log(`  ${theme}: ${count} times`);
});

const balanced = Object.values(themeCountsInWindow).every(c => c >= 1 && c <= 3);
console.log(`  ✓ Themes ${balanced ? 'are balanced' : 'MAY BE UNBALANCED (acceptable with randomness)'}`);

// Check 2: Look for immediate repeats (same theme back-to-back)
console.log(`\nCheck 2: Looking for back-to-back theme repeats...`);
let backToBackRepeats = 0;
for (let i = 1; i < results.length; i++) {
  if (results[i].theme === results[i-1].theme) {
    console.log(`  ⚠️ Back-to-back repeat at ${i}: ${results[i].theme}`);
    backToBackRepeats++;
  }
}
if (backToBackRepeats === 0) {
  console.log(`  ✓ No back-to-back theme repeats (GOOD!)`);
}

// Check 3: Look for duplicate question IDs
console.log(`\nCheck 3: Looking for duplicate question IDs...`);
const idCounts = {};
results.forEach(q => {
  idCounts[q.id] = (idCounts[q.id] || 0) + 1;
});

const duplicates = Object.entries(idCounts).filter(([id, count]) => count > 1);
if (duplicates.length === 0) {
  console.log(`  ✓ No duplicate questions in sample (GOOD!)`);
} else {
  console.log(`  ✗ Found duplicate questions:`);
  duplicates.forEach(([id, count]) => {
    console.log(`    ${id}: appeared ${count} times`);
  });
}

console.log('\n' + '='.repeat(80));
console.log('SUMMARY');
console.log('='.repeat(80));

const passedChecks = balanced && backToBackRepeats === 0 && duplicates.length === 0;
if (passedChecks) {
  console.log('✓✓✓ SHUFFLED ROUND-ROBIN WORKING CORRECTLY ✓✓✓');
  console.log('\nBehavior confirmed:');
  console.log('  ✓ Themes cycle through before repeating');
  console.log('  ✓ No back-to-back theme repeats');
  console.log('  ✓ No duplicate questions until all are used');
  console.log('  ✓ Questions shuffled for randomness');
} else {
  console.log('⚠️ Some checks did not pass - review output above');
}
