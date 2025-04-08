import psycopg2

try:
    conn = psycopg2.connect(
        dbname="course_registration",
        user="postgres",
        password="post34",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
    """)
    tables = cur.fetchall()

    print("🗂️ Tables in the database:")
    for table in tables:
        print(f" - {table[0]}")

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)
