"""Inspect Bible database schema."""

import sqlite3
from pathlib import Path

db_path = Path("data/bible.db")
conn = sqlite3.connect(str(db_path))

print("="*60)
print("Bible Database Schema")
print("="*60 + "\n")

# Get all tables
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
tables = [row[0] for row in cursor.fetchall()]

print(f"Tables found: {len(tables)}\n")

for table in tables:
    print(f"\n📋 Table: {table}")
    print("-" * 60)
    
    # Get schema
    cursor = conn.execute(f"PRAGMA table_info({table})")
    columns = cursor.fetchall()
    
    print("Columns:")
    for col in columns:
        col_id, name, col_type, not_null, default, pk = col
        print(f"  {name:20} {col_type:15} {'PK' if pk else ''}")
    
    # Get sample row count
    cursor = conn.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"\nRow count: {count:,}")
    
    # Get sample row
    if count > 0:
        cursor = conn.execute(f"SELECT * FROM {table} LIMIT 1")
        sample = cursor.fetchone()
        if sample:
            print("\nSample row:")
            col_names = [col[1] for col in columns]
            for i, val in enumerate(sample):
                if val is not None:
                    val_str = str(val)[:50]
                    print(f"  {col_names[i]}: {val_str}")

conn.close()
