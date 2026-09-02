import requests
import sqlite3
import os

def fetch_and_store_books():
    # Use Open Library API for reliable unauthenticated REST access
    query = "harry+potter"
    url = f"https://openlibrary.org/search.json?q={query}"
    
    print(f"Fetching books from: {url}...")
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    
    items = data.get('docs', [])
    print(f"Retrieved {len(items)} books from API.\n")
    
    # Store in SQLite database in the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "books_data.db")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id TEXT PRIMARY KEY,
        title TEXT,
        author TEXT,
        year TEXT
    )
    """)
    
    # Store first 10 books
    for item in items[:10]:
        book_id = item.get('key', 'Unknown')
        title = item.get('title', 'Unknown')
        
        if 'author_name' in item:
            author = ", ".join(item['author_name'])
        else:
            author = 'Unknown'
            
        if 'first_publish_year' in item:
            year = str(item['first_publish_year'])
        else:
            year = 'Unknown'
            
        cursor.execute("INSERT OR REPLACE INTO books VALUES (?, ?, ?, ?)", (book_id, title, author, year))
    
    conn.commit()
    
    # Retrieve and display data from the database
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    
    print("--- Stored Books in SQLite Database ---")
    for row in rows:
        print(f"ID:     {row[0]}")
        print(f"Title:  {row[1]}")
        print(f"Author: {row[2]}")
        print(f"Year:   {row[3]}")
        print("-" * 40)
        
    conn.close()

if __name__ == "__main__":
    fetch_and_store_books()
