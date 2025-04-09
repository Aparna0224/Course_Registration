from fastapi import APIRouter, HTTPException, Response, Request
from models.faculty import login_faculty, get_faculty_courses
from pydantic import BaseModel

router = APIRouter()

class FacultyLoginRequest(BaseModel):
    faculty_id: str
    name: str

@router.post("/login")
def faculty_login(payload: FacultyLoginRequest, response: Response):
    data = login_faculty(payload.faculty_id, payload.name)
    if data:
        # ✅ Set faculty_id in a cookie
        response.set_cookie(
            key="faculty_id",
            value=payload.faculty_id,
            httponly=True,
            max_age=86400,  # 1 day
            samesite="Lax"
        )
        return data

    raise HTTPException(status_code=401, detail="Invalid faculty credentials")


@router.get("/{faculty_id}/courses")
def faculty_courses(faculty_id: str):
    return get_faculty_courses(faculty_id)
