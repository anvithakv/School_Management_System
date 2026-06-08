from tkinter import *
from admin.student_management import open_student_management
from teacher.teacher_management import open_teacher_management
from teacher.attendance import open_attendance
from admin.fee_management import open_fee_management
from admin.complaints import open_complaints
from chats.chat_window import open_chat_window



def open_admin_dashboard():

    dashboard = Toplevel()
    dashboard.title("School Management System")
    dashboard.geometry("1200x700")
    dashboard.configure(bg="#F3F4F6")

    # ================= HEADER =================

    header = Frame(
        dashboard,
        bg="#1E3A8A",
        height=80
    )
    header.pack(fill=X)

    Label(
        header,
        text="SCHOOL MANAGEMENT SYSTEM",
        bg="#1E3A8A",
        fg="white",
        font=("Arial", 22, "bold")
    ).pack(pady=20)

    Label(
        dashboard,
        text="ADMIN PANEL",
        bg="#F3F4F6",
        fg="black",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    Label(
        dashboard,
        text="Welcome administrator!",
        bg="#F3F4F6",
        font=("Arial", 18)
    ).pack(pady=40)

    Button(
        dashboard,
        text="👨‍🎓 Students",
        width=20,
        font=("Arial", 11),
        command=open_student_management
    ).pack(pady=10)

    Button(
        dashboard,
        text="👩‍🏫 Teachers",
        width=20,
        font=("Arial", 11),
        command=open_teacher_management
    ).pack(pady=10)

    Button(
    dashboard,
    text="📅 Attendance",
    width=20,
    font=("Arial", 11),
    command=open_attendance
).pack(pady=10)

    Button(
    dashboard,
    text="💰 Fees",
    width=20,
    font=("Arial",11),
    command=open_fee_management
).pack(pady=10)
    
    Button(
        dashboard,
        text="📝 Complaints",
        width=20,
        font=("Arial", 11),
        command=open_complaints
    ).pack(pady=10)

    Button(
    dashboard,
    text="💬 Chat",
    command=lambda:
    open_chat_window("Admin")
).pack(pady=10)
    
    


