Here's a clean and professional Markdown version of your **API Endpoints** section. You can include this in your `README.md` file or API documentation.

---

```markdown
## 📡 API Endpoints

### 🧑‍🎓 Student Endpoints

#### 1. Student Login
```http
POST /student/login
```
**Description:** Authenticate a student using `student_id` and `dob`.  
**Body:**
```json
{
  "student_id": "2020CH5801",
  "dob": "2002-03-15"
}
```
**Response:**
```json
{ "message": "Login successful" }
```
**URL:** [http://127.0.0.1:8000/student/login](http://127.0.0.1:8000/student/login)

---

#### 2. Register for Courses
```http
POST /student/register
```
**Description:** Register a student for selected courses.  
**Body:**
```json
{
  "student_id": "2020CH5801",
  "course_ids": ["CS01", "MA01"],
  "semester": "Spring 2025"
}
```
**Response:**
```json
{ "message": "Courses registered" }
```
**URL:** [http://127.0.0.1:8000/student/register](http://127.0.0.1:8000/student/register)

---

#### 3. Get Registered Courses
```http
GET /student/{student_id}/courses
```
**Description:** Fetch all courses a student is registered for.  
**URL Example:** [http://127.0.0.1:8000/student/2020CH5801/courses](http://127.0.0.1:8000/student/2020CH5801/courses)

---

#### 4. Drop a Registered Course
```http
DELETE /student/{student_id}/register/{course_id}
```
**Description:** Drop a course that a student is registered in.  
**URL Example:** [http://127.0.0.1:8000/student/2020CH5801/register/DS01](http://127.0.0.1:8000/student/2020CH5801/register/DS01)

---

#### 5. Fetch Student Details
```http
GET /student/{student_id}
```
**Description:** Retrieve full profile of a student.  
**URL Example:** [http://127.0.0.1:8000/student/2020CH5801](http://127.0.0.1:8000/student/2020CH5801)

---

#### 6. Get Offered Courses by Department
```http
GET /student/{student_id}/offered-courses
```
**Description:** Get a list of department-specific courses offered to a student.  
**URL Example:** [http://127.0.0.1:8000/student/2020IT2910/offered-courses](http://127.0.0.1:8000/student/2020IT2910/offered-courses)

---

### 👨‍🏫 Faculty Endpoints

#### 7. Faculty Login
```http
POST /faculty/login
```
**Description:** Authenticate a faculty member.  
**Body:**
```json
{
  "faculty_id": "FAC5801",
  "name": "Dr. Smith"
}
```
**Response:** Faculty details or authentication error  
**URL:** [http://127.0.0.1:8000/faculty/login](http://127.0.0.1:8000/faculty/login)

---

#### 8. Get Faculty Courses
```http
GET /faculty/{faculty_id}/courses
```
**Description:** Get a list of courses handled by the faculty member.  
**URL Example:** [http://127.0.0.1:8000/faculty/FAC5801/courses](http://127.0.0.1:8000/faculty/FAC5801/courses)
```

---

Let me know if you'd like this included directly in the `README.md` or a separate API documentation file like `API_DOCS.md`.
