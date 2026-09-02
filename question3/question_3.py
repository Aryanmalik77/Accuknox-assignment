import os
import sqlite3
import pandas as pd

def import_csv_to_sqlite():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "users.csv")
    
    if not os.path.exists(csv_path):
        print(f"[Error] CSV file not found at: {csv_path}")
        return
    
    print(f"Reading CSV from: {csv_path}...")
    df = pd.read_csv(csv_path)
    print("\n--- DataFrame Head ---")
    print(df.head())
    print("-" * 30)
    
    db_path = os.path.join(current_dir, "users.db")
    print(f"\nConnecting to SQLite database: {db_path}...")
    conn = sqlite3.connect(db_path)
    
    # Store in users table
    df.to_sql('users', conn, if_exists='replace', index=False)
    # Also save as sentiment_table for backwards compatibility with prompt
    df.to_sql('sentiment_table', conn, if_exists='replace', index=False)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT 5")
    rows = cursor.fetchall()
    
    print("\n--- Retrieved Rows from SQLite (LIMIT 5) ---")
    for row in rows:
        print(f"Name:  {row[0]}")
        print(f"Email: {row[1]}")
        print("-" * 30)
        
    conn.close()
    print("Database connection closed successfully.")

if __name__ == "__main__":
    import_csv_to_sqlite()
