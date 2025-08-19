import os
from flask import Flask
import psycopg2
import psycopg2.extras

# Set the environment variable
os.environ['DATABASE_URL'] = "postgresql://postgres:alswn3929!@db.dvipjmroamjznesnohpw.supabase.co:5432/postgres"

app = Flask(__name__)

def get_db_connection():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
        return conn, 'postgres'
    return None, None

@app.route('/test-db')
def test_db():
    try:
        conn, db_type = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            tables = cursor.fetchall()
            
            conn.close()
            
            return {
                'status': 'success',
                'database': db_type,
                'version': version['version'][:100],
                'tables': [table['table_name'] for table in tables]
            }
        else:
            return {'status': 'error', 'message': 'No database connection'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    print("Testing database connection via Flask...")
    with app.test_client() as client:
        response = client.get('/test-db')
        print(response.get_json())
