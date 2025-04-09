from fastapi import APIRouter, HTTPException, Response, Request
from pydantic import BaseModel
from models.student import (
    login_student,
    register_courses,
    get_registered_courses,
    drop_course,
    get_student_details,
    get_courses_by_department
)

router = APIRouter()

# -------------------- MODELS --------------------

class StudentLogin(BaseModel):
    student_id: str
    dob: str

class RegistrationRequest(BaseModel):
    student_id: str
    course_ids: list[str]
    semester: str

# -------------------- LOGIN --------------------

@router.post("/login")
def student_login(data: StudentLogin, response: Response):
    student = login_student(data.student_id, data.dob)
    if student:
        # Set student_id in cookie
        response.set_cookie(
            key="student_id",
            value=data.student_id,
            httponly=True,
            max_age=86400,  # 1 day
            samesite="Lax"
        )
        return {
            "message": "Login successful",
            "student_id": data.student_id
        }
    raise HTTPException(status_code=401, detail="Invalid credentials")

# -------------------- REGISTER COURSES --------------------

@router.post("/register")
def course_registration(data: RegistrationRequest, request: Request):
    student_id = request.cookies.get("student_id") or data.student_id
    if not student_id:
        raise HTTPException(status_code=401, detail="Student ID missing")

    result = register_courses(student_id, data.course_ids, data.semester)
    if result:
        return {
            "message": "Courses registered",
            "student_id": student_id
        }
    raise HTTPException(status_code=400, detail="Registration failed")

# -------------------- GET REGISTERED COURSES --------------------

@router.get("/{student_id}/courses")
def get_courses(student_id: str, request: Request):
    sid = request.cookies.get("student_id") or student_id
    courses = get_registered_courses(sid)
    if courses:
        return {
            "student_id": sid,
            "courses": courses
        }
    raise HTTPException(status_code=404, detail="No registered courses found")

# -------------------- DROP COURSE --------------------

@router.delete("/{student_id}/register/{course_id}")
def drop_registered_course(student_id: str, course_id: str, request: Request):
    sid = request.cookies.get("student_id") or student_id
    success = drop_course(sid, course_id)
    if success:
        return {
            "message": "Course dropped successfully",
            "student_id": sid
        }
    raise HTTPException(status_code=400, detail="Failed to drop course")

# -------------------- GET STUDENT DETAILS --------------------

@router.get("/{student_id}")
def fetch_student_details(student_id: str, request: Request):
    sid = request.cookies.get("student_id") or student_id
    student = get_student_details(sid)
    if student:
        return {
            "student_id": sid,
            "name": student["name"],
            "email": student["email"],
            "semester": student["current_semester"]
        }
    raise HTTPException(status_code=404, detail="Student not found")

# -------------------- GET OFFERED COURSES BY DEPARTMENT --------------------

@router.get("/{student_id}/offered-courses")
def fetch_offered_courses(student_id: str, request: Request):
    sid = request.cookies.get("student_id") or student_id
    courses = get_courses_by_department(sid)
    if courses is not None:
        return {
            "student_id": sid,
            "offered_courses": courses
        }
    raise HTTPException(status_code=404, detail="Could not find offered courses")
