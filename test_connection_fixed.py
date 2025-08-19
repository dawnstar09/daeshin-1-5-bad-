import psycopg2
import urllib.parse

# URL encode the password to handle special characters
password = urllib.parse.quote_plus("alswn3929!")
DATABASE_URL = f"postgresql://postgres:{password}@db.dvipjmroamjznesnohpw.supabase.co:5432/postgres"

print("Testing Supabase connection...")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Test the connection
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"✅ Connection successful!")
    print(f"PostgreSQL version: {version[0][:50]}...")
    
    # Check tables
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    
    print(f"\n📋 Found {len(tables)} tables:")
    for table in tables:
        print(f"  - {table[0]}")
    
    conn.close()
    
except Exception as e:
    print(f"❌ Connection failed: {e}")
