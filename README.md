# Student Course Registration Backend

Backend for managing student and faculty course registrations using Python and PostgreSQL.

Here's a complete `README.md` tailored for your [Course_Registration](https://github.com/Aparna0224/Course_Registration/tree/main) project based on the backend and frontend logic you've shared:

---

```markdown
# 🎓 Course Registration System

A full-stack academic course registration system built using **FastAPI**, **MongoDB**, and **React**. This system allows students to register for offered courses, view registrations, and drop courses. Faculty can log in and view the courses they offer.

---

## 🚀 Features

- 👨‍🎓 Student login & course registration
- 🧾 View registered and offered courses
- 📤 Drop registered courses
- 👨‍🏫 Faculty login & view assigned courses
- 🗃️ MongoDB for persistent storage
- ⚡ FastAPI backend with clean API design
- 🖥️ React-based frontend (under development)

---

## 🛠 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Frontend     | React              |
| Backend      | FastAPI            |
| Database     | MongoDB            |
| API Testing  | Postman            |
| Deployment   | Local / Cloud-ready |

---

## 📂 Project Structure

```
Course_Registration/
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── routers/
│   │   ├── student.py          # Student-related routes
│   │   └── faculty.py          # Faculty-related routes
│   ├── models/                 # Pydantic models
│   ├── services/               # Business logic functions
│   └── utils/                  # Helper modules
├── frontend/                   # React app (in progress)
├── README.md
```

---

## 📡 API Endpoints Overview

### Student Endpoints

| Method | Endpoint                                              | Description                          |
|--------|--------------------------------------------------------|--------------------------------------|
| POST   | `/student/login`                                       | Student login                        |
| POST   | `/student/register`                                    | Register for courses                 |
| GET    | `/student/{student_id}/courses`                        | Get registered courses               |
| DELETE | `/student/{student_id}/register/{course_id}`           | Drop a registered course             |
| GET    | `/student/{student_id}`                                | Fetch student details                |
| GET    | `/student/{student_id}/offered-courses`                | View department-offered courses      |

### Faculty Endpoints

| Method | Endpoint                              | Description              |
|--------|----------------------------------------|--------------------------|
| POST   | `/faculty/login`                      | Faculty login            |
| GET    | `/faculty/{faculty_id}/courses`       | View faculty's courses   |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Aparna0224/Course_Registration.git
cd Course_Registration
```

---

### 2. Setup Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows

pip install -r requirements.txt
uvicorn main:app --reload
```

Ensure MongoDB is running locally or replace the URI with your cloud cluster.

---

### 3. (Optional) Setup Frontend

Coming soon. You can begin development in the `frontend/` folder using:

```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 API Testing

You can test all endpoints using Postman or directly via the FastAPI docs:

```
http://localhost:8000/docs
```

---

