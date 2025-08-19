# 임시 테스트용 파일
import psycopg2

# 여기에 수정된 연결 문자열을 넣어서 테스트하세요
# 예시: postgresql://postgres:MySecurePass123!@db.abcdefghijk.supabase.co:5432/postgres
DATABASE_URL = "postgresql://postgres:alswn3929!@db.dvipjmroamjznesnohpw.supabase.co:5432/postgres"

print(f"연결 시도: {DATABASE_URL[:50]}...")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # 테이블 목록 확인
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()
    
    print("✅ 연결 성공!")
    print("생성된 테이블들:")
    for table in tables:
        print(f"  - {table[0]}")
    
    conn.close()
    
except Exception as e:
    print(f"❌ 연결 실패: {e}")
    print("확인사항:")
    print("1. 비밀번호가 정확한지")
    print("2. 문자열에 오타가 없는지")
    print("3. [YOUR-PASSWORD] 부분을 실제 비밀번호로 바꿨는지")
