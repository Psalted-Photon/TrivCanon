"""Download Bible data sources from GitHub repositories."""

import urllib.request
import sys
from pathlib import Path

def download_file(url, filepath):
    """Download file with progress indicator."""
    print(f"Downloading {filepath.name}...", end=" ", flush=True)
    try:
        urllib.request.urlretrieve(url, filepath)
        size = filepath.stat().st_size
        print(f"✓ ({size:,} bytes)")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    """Download all required data files."""
    print("="*60)
    print("Bible Trivia Data Downloader")
    print("="*60)
    
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)
    
    files = [
        {
            "url": "https://raw.githubusercontent.com/scrollmapper/bible_databases/master/formats/sqlite/KJV.db",
            "path": data_dir / "bible.db",
            "description": "scrollmapper Bible database (KJV translation)"
        },
        {
            "url": "https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/people.json",
            "path": data_dir / "people.json",
            "description": "Theographic people data"
        },
        {
            "url": "https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/places.json",
            "path": data_dir / "places.json",
            "description": "Theographic places data"
        },
        {
            "url": "https://raw.githubusercontent.com/robertrouse/theographic-bible-metadata/master/json/events.json",
            "path": data_dir / "events.json",
            "description": "Theographic events data"
        }
    ]
    
    print("\nDownloading data sources:\n")
    
    success_count = 0
    for file_info in files:
        if download_file(file_info["url"], file_info["path"]):
            success_count += 1
    
    print("\n" + "="*60)
    if success_count == len(files):
        print("✓ All data files downloaded successfully!")
        print(f"✓ Files saved to: {data_dir}")
    else:
        print(f"⚠ Downloaded {success_count}/{len(files)} files")
        print("Some files failed to download. Please retry.")
        sys.exit(1)
    print("="*60)

if __name__ == "__main__":
    main()
