# Corrected Bible Data Source URLs

## Summary
All data sources successfully downloaded with corrected URLs.

## Issue Resolution

### Problems Found:
1. **scrollmapper/bible_databases** - Incorrect file path
   - ❌ Old: `https://raw.githubusercontent.com/scrollmapper/bible_databases/master/bible.db`
   - ✅ New: `https://raw.githubusercontent.com/scrollmapper/bible_databases/master/formats/sqlite/KJV.db`
   - **Note**: No single `bible.db` file exists. The repository has individual translation files in `formats/sqlite/` directory.

2. **robertrouse/theographic-bible-metadata** - Wrong branch name
   - ❌ Old branch: `main`
   - ✅ Correct branch: `master`

## Working URLs

### 1. Bible Database (SQLite format)
**URL**: `https://raw.githubusercontent.com/scrollmapper/bible_databases/master/formats/sqlite/KJV.db`
- **Repository**: scrollmapper/bible_databases
- **Branch**: master
- **Path**: formats/sqlite/KJV.db
- **Format**: SQLite database
- **Translation**: King James Version (KJV)
- **Size**: ~4.75 MB
- **Alternative translations available**: WEB.db, ASV.db, BBE.db, etc. (140 translations total)

### 2. Theographic People Data
**URL**: `https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/people.json`
- **Repository**: robertrouse/theographic-bible-metadata
- **Branch**: master (NOT main)
- **Path**: json/people.json
- **Format**: JSON
- **Size**: ~5.08 MB
- **Description**: Comprehensive catalog of every individual mentioned by name in the Bible

### 3. Theographic Places Data
**URL**: `https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/places.json`
- **Repository**: robertrouse/theographic-bible-metadata
- **Branch**: master (NOT main)
- **Path**: json/places.json
- **Format**: JSON
- **Size**: ~2.37 MB
- **Description**: Geographic locations mentioned in the Bible with coordinates

### 4. Theographic Events Data
**URL**: `https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/events.json`
- **Repository**: robertrouse/theographic-bible-metadata
- **Branch**: master (NOT main)
- **Path**: json/events.json
- **Format**: JSON
- **Size**: ~1.74 MB
- **Description**: Timeline of Biblical events

## Verification

All URLs tested and verified working on December 25, 2025:
- ✅ bible.db (KJV.db) - Downloaded successfully (4,751,360 bytes)
- ✅ people.json - Downloaded successfully (5,078,768 bytes)
- ✅ places.json - Downloaded successfully (2,374,841 bytes)
- ✅ events.json - Downloaded successfully (1,738,924 bytes)

## Alternative Bible Translations Available

The scrollmapper/bible_databases repository provides 140 different Bible translations in SQLite format. To use a different translation, replace `KJV.db` in the URL with any of these:

**Popular English translations**:
- `KJV.db` - King James Version (1769)
- `KJVA.db` - King James Version with Apocrypha
- `ASV.db` - American Standard Version (1901)
- `BBE.db` - Bible in Basic English (1949/1964)
- `Darby.db` - Darby Bible (1889)
- `Webster.db` - Webster Bible
- `YLT.db` - Young's Literal Translation (1898)

Full list available at: https://github.com/scrollmapper/bible_databases/tree/master/formats/sqlite

## Download Method

These URLs work with:
- `urllib` (Python)
- `curl` (command line)
- `wget` (command line)
- Direct browser download
- Any HTTP GET request

Example with curl:
```bash
curl -o bible.db https://raw.githubusercontent.com/scrollmapper/bible_databases/master/formats/sqlite/KJV.db
curl -o people.json https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/people.json
curl -o places.json https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/places.json
curl -o events.json https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/events.json
```

## Repository Information

### scrollmapper/bible_databases
- **Full URL**: https://github.com/scrollmapper/bible_databases
- **License**: MIT
- **Stars**: 1.4k+
- **Formats**: MySQL, SQLite, CSV, JSON, YAML, TXT, MD
- **Translations**: 140 different Bible versions
- **Default Branch**: master

### robertrouse/theographic-bible-metadata
- **Full URL**: https://github.com/robertrouse/theographic-bible-metadata
- **License**: CC-BY-SA-4.0
- **Stars**: 270+
- **Description**: Knowledge graph of the Bible
- **Default Branch**: master
- **Files**: books.json, chapters.json, easton.json, events.json, people.json, peopleGroups.json, periods.json, places.json, verses.json
