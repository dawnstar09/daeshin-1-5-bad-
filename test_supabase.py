# -*- coding: utf-8 -*-
# Supabase Connection Test
import psycopg2

DATABASE_URL = "postgresql://postgres:alswn3929!@db.dvipjmroamjznesnohpw.supabase.co:5432/postgres"

print(f"Connecting to: {DATABASE_URL[:50]}...")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Check existing tables
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    
    print("Connection Success!")
    print("Created tables:")
    for table in tables:
        print(f"  - {table[0]}")
    
    conn.close()
    
except Exception as e:
    print(f"Connection Failed: {e}")
