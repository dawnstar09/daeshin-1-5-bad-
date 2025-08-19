import psycopg2

# Try direct connection parameters instead of URL
try:
    conn = psycopg2.connect(
        host="db.dvipjmroamjznesnohpw.supabase.co",
        port=5432,
        database="postgres",
        user="postgres",
        password="alswn3929!"
    )
    
    cursor = conn.cursor()
    
    # Test the connection
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"✅ Connection successful!")
    print(f"PostgreSQL version: {version[0][:80]}...")
    
    # Check tables
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    
    print(f"\n📋 Found {len(tables)} tables:")
    for table in tables:
        print(f"  - {table[0]}")
    
    conn.close()
    print("\n🎉 Database connection successful!")
    
except Exception as e:
    print(f"❌ Connection failed: {e}")
