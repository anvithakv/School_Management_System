CREATE DATABASE school_management_system;
USE school_management_system;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100),
    role ENUM('admin','teacher','student')
);

INSERT INTO users(username,password,role)
VALUES
('admin','admin123','admin'),
('teacher1','teacher123','teacher'),
('student1','student123','student');

CREATE TABLE students(
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    class_name VARCHAR(50),
    phone VARCHAR(20),
    address TEXT
);

CREATE TABLE teachers(
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE attendance(
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE,
    status ENUM('Present','Absent'),
    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
);

CREATE TABLE fees(
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(10,2),
    status ENUM('Paid','Pending'),
    FOREIGN KEY(student_id)
    REFERENCES students(student_id)
);

CREATE TABLE complaints(
    complaint_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    complaint TEXT,
    status ENUM('Pending','Resolved')
);


CREATE TABLE notifications(
    notification_id INT PRIMARY KEY AUTO_INCREMENT,
    message VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

