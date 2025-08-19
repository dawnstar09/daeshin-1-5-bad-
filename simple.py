import psycopg2

try:
    conn = psycopg2.connect("postgresql://postgres:alswn3929!@db.dvipjmroamjznesnohpw.supabase.co:5432/postgres")
    cursor = conn.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    print("SUCCESS! Tables:")
    for table in tables:
        print(f"  - {table[0]}")
    conn.close()
except Exception as e:
    print(f"ERROR: {e}")
