from fastapi import FastAPI
from routes import student, faculty
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Or replace with your frontend URL e.g. ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],  # or ["POST", "GET", "OPTIONS"]
    allow_headers=["*"],
)
app.include_router(student.router, prefix="/student", tags=["Student"])
app.include_router(faculty.router, prefix="/faculty", tags=["Faculty"])

@app.get("/")
def read_root():
    return {"message": "Student Course Registration System"}
