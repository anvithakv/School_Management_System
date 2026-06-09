# 🎓 School Management System

## 📌 Project Overview

The School Management System is a desktop application developed using **Python Tkinter** and **MySQL**. It provides an efficient way to manage students, teachers, attendance, fees, complaints, real-time communication, file sharing, and notifications within a school environment.

The system follows **Object-Oriented Programming (OOP)** principles and uses **Socket Programming** and **Threading** to implement real-time chat functionality.

---

## 🚀 Features

### 🔐 Login System

* Secure user login
* Role-based access

  * Admin
  * Teacher
  * Student

### 👨‍🎓 Student Management

* Add students
* Update student details
* Delete students
* View student records

### 👩‍🏫 Teacher Management

* Add teachers
* Update teacher details
* Delete teachers
* View teacher records

### 📅 Attendance Management

* Mark student attendance
* View attendance records
* Present/Absent status tracking

### 💰 Fee Management

* Add fee records
* View fee details
* Track payment status

### 📝 Complaint Management

* Students can submit complaints
* Admin can view and resolve complaints

### 💬 Real-Time Chat System

* Admin, Teacher, and Student communication
* Socket-based messaging
* Multi-user chat support
* Threading for simultaneous message handling

### 📁 File Sharing

* Share files through the chat module
* Shared files are stored in a common folder
* Supports educational document sharing

### 🔔 Notifications

* User notifications through Tkinter message boxes
* Notifications for attendance, fees, and complaints

---

## 🛠 Technologies Used

* Python
* Tkinter
* MySQL
* Socket Programming
* Threading
* Object-Oriented Programming (OOP)

---


## 🗄 Database Tables

* users
* students
* teachers
* attendance
* fees
* complaints
*  notifications
---

## ▶️ How to Run

### 1. Install Python

Download and install Python 3.x.

### 2. Install MySQL

Install MySQL Server and create the required database and tables.

### 3. Configure Database

Update the database credentials in:

```python
database.py
```

### 4. Start Chat Server

Run:

```bash
python server.py
```

### 5. Run Application

Run:

```bash
python main.py
```

---

## 🔄 OOP Concepts Used

* Classes and Objects
* Inheritance
* Encapsulation
* Modular Programming

---

## 🌐 Socket Programming

The chat system uses:

* TCP Sockets
* Client-Server Architecture
* Real-Time Communication

---

## 🧵 Threading

Threading is used to:

* Receive messages continuously
* Prevent GUI freezing
* Enable multiple users to communicate simultaneously

---



## 🎯 Future Enhancements

* Email Notifications
* Report Generation
* Exam Management
* Timetable Management
* Cloud Database Integration

