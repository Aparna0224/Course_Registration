from database import get_connection

def login_student(student_id, dob):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
    "SELECT student_id, name, email, dep_id, current_semester FROM student WHERE student_id=%s AND dob=%s",
    (student_id, dob)
)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return {
    "student_id": result[0],
    "name": result[1],
    "email": result[2],
    "department_id": result[3],  # from dep_id
    "current_semester": result[4]
    }
    return None

def register_courses(student_id, course_ids, semester):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        for course_id in course_ids:
            print(f"Inserting: {student_id} - {course_id} - {semester}")
            cursor.execute(
                "INSERT INTO registration (student_id, course_id, semester) VALUES (%s, %s, %s)",
                (student_id, course_id, semester)
            )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Registration error:", e)
        return False


def get_registered_courses(student_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.course_id, c.course_name, r.semester, r.registration_date
            FROM registration r
            JOIN course c ON r.course_id = c.course_id
            WHERE r.student_id = %s
        """, (student_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return [
            {
                "course_id": row[0],
                "course_name": row[1],
                "semester": row[2],
                "registration_date": str(row[3])
            } for row in result
        ]
    except Exception as e:
        print("Fetch registered courses error:", e)
        return []



def drop_course(student_id, course_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM registration WHERE student_id = %s AND course_id = %s",
            (student_id, course_id)
        )
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected > 0
    except Exception as e:
        print("Error dropping course:", e)
        return False
    

def get_student_details(student_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT student_id, name, email, dep_id, current_semester FROM student WHERE student_id=%s",
            (student_id,)
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return {
                "student_id": result[0],
                "name": result[1],
                "email": result[2],
                "department_id": result[3],
                "current_semester": result[4]
            }
        return None
    except Exception as e:
        print("Error fetching student details:", e)
        return None

def get_courses_by_department(student_id):
    try:
        student = get_student_details(student_id)
        if not student:
            return None

        department_id = student["department_id"]  # Correct key

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT course_id, course_name FROM course WHERE dept_id = %s",
            (department_id,)
        )
        courses = cursor.fetchall()
        cursor.close()
        conn.close()

        return [{"course_id": row[0], "course_name": row[1]} for row in courses]
    except Exception as e:
        print("Error fetching department courses:", e)
        return None