INSERT INTO department (dep_id, dep_name, num_courses, num_professors) VALUES
('CS54', 'Computer Science', 12, 15),
('EE32', 'Electrical Engineering', 10, 12),
('ME21', 'Mechanical Engineering', 8, 10),
('CE45', 'Civil Engineering', 9, 11),
('EC31', 'Electronics and Communication', 11, 13),
('IT29', 'Information Technology', 10, 14),
('BT36', 'Biotechnology', 6, 8),
('AE27', 'Aerospace Engineering', 7, 9),
('CH58', 'Chemical Engineering', 9, 10),
('MT49', 'Mechatronics', 8, 9);

select * from department;

INSERT INTO student (student_id, name, dep_id, phone, email, dob, current_semester) VALUES
('2020CH5801', 'Zachary Graves', 'CH58', '544-073-0589', 'lucasyoung@yahoo.com', '2004-04-08', 5),
('2020AE2702', 'Nicole Johnston', 'AE27', '126-365-4883', 'swilson@gmail.com', '2000-08-30', 4),
('2021CE4503', 'Robert Williams', 'CE45', '117-443-6359', 'crawfordtravis@gmail.com', '2002-08-06', 4),
('2021CH5804', 'Charles Sanchez', 'CH58', '823-904-7820', 'leejonathan@gmail.com', '2002-09-01', 7),
('2022CS5405', 'Jessica Reid', 'CS54', '639-732-9834', 'williamska@gmail.com', '2005-01-04', 3),
('2022BT3606', 'Kelly Sutton', 'BT36', '574-702-1144', 'joseph10@gmail.com', '2000-09-21', 2),
('2023CS5407', 'Richard Carter', 'CS54', '634-365-3847', 'david93@gmail.com', '2005-02-02', 1),
('2023AE2708', 'Gary Mitchell', 'AE27', '353-547-7740', 'jefferyanderson@gmail.com', '2002-10-24', 1),
('2022CH5809', 'Michael Mccarthy', 'CH58', '832-643-1045', 'muellerkrystal@gmail.com', '2000-12-14', 7),
('2020IT2910', 'Teresa Martin', 'IT29', '387-529-5910', 'phillipspatrick@gmail.com', '2002-06-19', 8),
('2022CH5811', 'Melissa Goodwin', 'CH58', '430-384-1813', 'williamscrystal@gmail.com', '2000-06-30', 2),
('2020CS5412', 'Stacey Garcia', 'CS54', '826-927-3374', 'hendersonmary@gmail.com', '2002-02-13', 3),
('2022ME2113', 'Teresa Spencer', 'ME21', '218-173-3484', 'bondjoseph@gmail.com', '2005-02-15', 7),
('2022CH5814', 'Chris Moore', 'CH58', '332-454-4189', 'james46@gmail.com', '2005-03-03', 2),
('2020CH5815', 'Christine Hodge', 'CH58', '350-589-6457', 'johnsontimothy@gmail.com', '2002-02-24', 4),
('2021IT2916', 'William Rodriguez', 'IT29', '511-931-0984', 'natalie39@gmail.com', '2000-04-13', 6),
('2022ME2117', 'Angela Parker', 'ME21', '855-219-8366', 'bruce68@gmail.com', '2001-01-28', 1),
('2020BT3618', 'Gina Elliott', 'BT36', '315-208-0886', 'brian90@gmail.com', '2000-10-02', 1),
('2023ME2119', 'Jon Rivera', 'ME21', '393-924-1870', 'rogersmatthew@gmail.com', '2001-11-01', 1),
('2020AE2720', 'Julia Graham', 'AE27', '666-355-4326', 'dianadominguez@gmail.com', '2003-10-14', 7);

select * from student;

INSERT INTO course (course_id, course_name, dept_id, credit) VALUES
('DS01', 'Data Structures', 'IT29', 5),
('DC02', 'Digital Circuits', 'CE45', 3),
('TD03', 'Thermodynamics', 'CE45', 5),
('FM04', 'Fluid Mechanics', 'IT29', 3),
('SP05', 'Signal Processing', 'CS54', 4),
('OS06', 'Operating Systems', 'EE32', 4),
('GN07', 'Genetics', 'BT36', 4),
('AD08', 'Aerodynamics', 'BT36', 3),
('OC09', 'Organic Chemistry', 'CH58', 4),
('RB10', 'Robotics', 'CS54', 4);

INSERT INTO course (course_id, course_name, dept_id, credit) VALUES
('AI11', 'Artificial Intelligence', 'CS54', 5),
('ML12', 'Machine Learning', 'CS54', 4),
('DB13', 'Database Systems', 'IT29', 4),
('CN14', 'Computer Networks', 'IT29', 3),
('SD15', 'Structural Design', 'CE45', 4),
('HM16', 'Hydraulic Machinery', 'CE45', 3),
('PS17', 'Power Systems', 'EE32', 5),
('ED18', 'Electronic Devices', 'EE32', 4),
('GE19', 'Genomics', 'BT36', 3),
('BC20', 'Biochemistry', 'CH58', 5);

select * from course;

INSERT INTO faculty (faculty_id, name, dep_id, courses_handled) VALUES
('FAC5801', 'Jonathan Jones', 'CH58', 3),
('FAC5402', 'Joshua White', 'CS54', 3),
('FAC2703', 'Craig Roberts', 'AE27', 3),
('FAC5404', 'David Hall', 'CS54', 1),
('FAC5805', 'Raymond Mendoza', 'CH58', 1),
('FAC5406', 'Robert Hall', 'CS54', 2),
('FAC2707', 'Paul Hines', 'AE27', 4),
('FAC5408', 'Michele Perez', 'CS54', 4),
('FAC5809', 'Kelly Campbell', 'CH58', 2),
('FAC2710', 'Jacob Collins', 'AE27', 3);
select * from faculty;


INSERT INTO faculty_course (faculty_id, course_id) VALUES
-- Jonathan Jones (3 courses)
('FAC5801', 'OC09'),
('FAC5801', 'GN07'),
('FAC5801', 'TD03'),

-- Joshua White (3 courses)
('FAC5402', 'DS01'),
('FAC5402', 'SP05'),
('FAC5402', 'RB10'),

-- Craig Roberts (3 courses)
('FAC2703', 'AD08'),
('FAC2703', 'FM04'),
('FAC2703', 'GN07'),

-- David Hall (1 course)
('FAC5404', 'SP05'),

-- Raymond Mendoza (1 course)
('FAC5805', 'OC09'),

-- Robert Hall (2 courses)
('FAC5406', 'DS01'),
('FAC5406', 'OS06'),

-- Paul Hines (4 courses)
('FAC2707', 'TD03'),
('FAC2707', 'FM04'),
('FAC2707', 'AD08'),
('FAC2707', 'GN07'),

-- Michele Perez (4 courses)
('FAC5408', 'SP05'),
('FAC5408', 'RB10'),
('FAC5408', 'OS06'),
('FAC5408', 'DS01'),

-- Kelly Campbell (2 courses)
('FAC5809', 'OC09'),
('FAC5809', 'GN07'),

-- Jacob Collins (3 courses)
('FAC2710', 'AD08'),
('FAC2710', 'TD03'),
('FAC2710', 'FM04');



select * from faculty_course;

select current_user;

select * from registration;


