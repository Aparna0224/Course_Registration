from database import get_connection

def login_faculty(faculty_id, name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT faculty_id, name, dep_id FROM faculty WHERE faculty_id=%s AND TRIM(name)=TRIM(%s)",
            (faculty_id, name)
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            print("Checking login for:", faculty_id, name)
            return {
                "faculty_id": result[0],
                "name": result[1],
                "department_id": result[2]
            }
        return None
    except Exception as e:
        print("Faculty login error:", e)
        return None

# def get_faculty_courses(faculty_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT c.course_id, c.name, COUNT(r.student_id) AS student_count
#         FROM faculty_course fc
#         JOIN course c ON fc.course_id = c.course_id
#         LEFT JOIN registration r ON c.course_id = r.course_id
#         WHERE fc.faculty_id = %s
#         GROUP BY c.course_id
#     """, (faculty_id,))
#     results = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return [{"course_id": row[0], "course_name": row[1], "enrolled_students": row[2]} for row in results]

def get_faculty_courses(faculty_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                c.course_id,
                c.course_name,
                COUNT(r.student_id) AS enrolled_students
            FROM 
                course c
            JOIN 
                faculty_course fc ON c.course_id = fc.course_id
            LEFT JOIN 
                registration r ON c.course_id = r.course_id
            WHERE 
                fc.faculty_id = %s
            GROUP BY 
                c.course_id, c.course_name
        """, (faculty_id,))
        
        courses = cursor.fetchall()
        cursor.close()
        conn.close()

        result = []
        for course in courses:
            result.append({
                "course_id": course[0],
                "course_name": course[1],
                "enrolled_students": course[2]
            })
        return result

    except Exception as e:
        print("Error fetching faculty courses:", e)
        return []