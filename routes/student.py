from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.student import login_student, register_courses,get_registered_courses,  drop_course,get_student_details,get_courses_by_department

router = APIRouter()

class StudentLogin(BaseModel):
    student_id: str
    dob: str

@router.post("/login")
def student_login(data: StudentLogin):
    if login_student(data.student_id, data.dob):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


class RegistrationRequest(BaseModel):
    student_id: str
    course_ids: list[str]
    semester: str

@router.post("/register")
def course_registration(data: RegistrationRequest):
    result = register_courses(data.student_id, data.course_ids, data.semester)
    if result:
        return {"message": "Courses registered"}
    raise HTTPException(status_code=400, detail="Registration failed")

@router.get("/{student_id}/courses")
def get_courses(student_id: str):
    courses = get_registered_courses(student_id)
    if courses:
        return courses
    raise HTTPException(status_code=404, detail="No registered courses found")

@router.delete("/{student_id}/register/{course_id}")
def drop_registered_course(student_id: str, course_id: str):
    success = drop_course(student_id, course_id)
    if success:
        return {"message": "Course dropped successfully"}
    raise HTTPException(status_code=400, detail="Failed to drop course")


@router.get("/{student_id}")
def fetch_student_details(student_id: str):
    student = get_student_details(student_id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")


@router.get("/{student_id}/offered-courses")
def fetch_offered_courses(student_id: str):
    courses = get_courses_by_department(student_id)
    if courses is not None:
        return courses
    raise HTTPException(status_code=404, detail="Could not find offered courses")