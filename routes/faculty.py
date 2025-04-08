from fastapi import APIRouter, HTTPException
from models.faculty import login_faculty, get_faculty_courses,get_faculty_courses
from pydantic import BaseModel

router = APIRouter()

class FacultyLoginRequest(BaseModel):
    faculty_id: str
    name: str

@router.post("/login")
def faculty_login(payload: FacultyLoginRequest):
    data = login_faculty(payload.faculty_id, payload.name)
    if data:
        return data
    raise HTTPException(status_code=401, detail="Invalid faculty credentials")

# @router.get("/courses/{faculty_id}")
# def faculty_courses(faculty_id: str):
#     return get_faculty_courses(faculty_id)

@router.get("/{faculty_id}/courses")
def faculty_courses(faculty_id: str):
    return get_faculty_courses(faculty_id)

