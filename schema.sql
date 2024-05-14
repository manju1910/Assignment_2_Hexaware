CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),   
    last_name VARCHAR(50),
    date_of_birth VARCHAR(20),
    email VARCHAR(100),
    phone_number VARCHAR(20)
);


CREATE TABLE Teacher (
    teacher_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);


CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);


CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);



CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    student_id INT,
    amount INT,
    payment_date VARCHAR (50),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);
