-- 1. Department
CREATE TABLE department (
    dep_id VARCHAR(10) PRIMARY KEY,
    dep_name VARCHAR(100) NOT NULL,
    num_courses INT DEFAULT 0,
    num_professors INT DEFAULT 0
);

-- 2. Student
CREATE TABLE student (
    student_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dep_id VARCHAR(10) REFERENCES department(dep_id) ON DELETE SET NULL,
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    dob DATE,
    current_semester VARCHAR(10)
);

-- 3. Course
CREATE TABLE course (
    course_id VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    dept_id VARCHAR(10) REFERENCES department(dep_id) ON DELETE SET NULL,
    credit INT CHECK (credit >= 1)
);


-- 4. Faculty
CREATE TABLE faculty (
    faculty_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dep_id VARCHAR(10) REFERENCES department(dep_id) ON DELETE SET NULL,
    courses_handled INT DEFAULT 0
);


-- 5. Registration
CREATE TABLE registration (
    registration_id SERIAL PRIMARY KEY,
    student_id VARCHAR(10) REFERENCES student(student_id) ON DELETE CASCADE,
    course_id VARCHAR(10) REFERENCES course(course_id) ON DELETE CASCADE,
    semester VARCHAR(10) NOT NULL,
    registration_date DATE DEFAULT CURRENT_DATE,
    CONSTRAINT unique_registration UNIQUE(student_id, course_id, semester)
);

-- 6. FacultyCourse (optional for future scope)
CREATE TABLE faculty_course (
    id SERIAL PRIMARY KEY,
    faculty_id VARCHAR(10) REFERENCES faculty(faculty_id) ON DELETE CASCADE,
    course_id VARCHAR(10) REFERENCES course(course_id) ON DELETE CASCADE
);