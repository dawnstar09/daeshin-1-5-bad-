import psycopg2
import urllib.parse

# Correct connection details from Supabase
password = urllib.parse.quote_plus("alswn3929!")
DATABASE_URL = f"postgresql://postgres:{password}@db.dvipjmroamjznesnohpw.supabase.co:5432/postgres"

print("Testing Supabase connection with correct details...")
print(f"Host: db.dvipjmroamjznesnohpw.supabase.co")
print(f"Port: 5432")
print(f"Database: postgres")
print(f"User: postgres")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Test the connection
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"\n✅ Connection successful!")
    print(f"PostgreSQL version: {version[0][:80]}...")
    
    # Check tables
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    
    print(f"\n📋 Found {len(tables)} tables:")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Test one of our tables
    if tables:
        cursor.execute("SELECT COUNT(*) FROM yaja_students;")
        count = cursor.fetchone()
        print(f"\n📊 yaja_students table has {count[0]} records")
    
    conn.close()
    print("\n🎉 Database connection test completed successfully!")
    
except Exception as e:
    print(f"\n❌ Connection failed: {e}")
    print("Please check if:")
    print("1. Password is correct")
    print("2. Network connection is stable")
    print("3. Supabase project is active")
