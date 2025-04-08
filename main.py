from fastapi import FastAPI
from routes import student, faculty

app = FastAPI()

app.include_router(student.router, prefix="/student", tags=["Student"])
app.include_router(faculty.router, prefix="/faculty", tags=["Faculty"])

@app.get("/")
def read_root():
    return {"message": "Student Course Registration System"}
