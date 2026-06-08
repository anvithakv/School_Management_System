from tkinter import *

from teacher.attendance import open_attendance
from admin.complaints import open_complaints
from chats.chat_window import open_chat_window


def open_teacher_dashboard():

    dashboard = Toplevel()

    dashboard.title("Teacher Dashboard")
    dashboard.geometry("900x600")
    dashboard.configure(bg="#F3F4F6")

    Label(
        dashboard,
        text="TEACHER PANEL",
        font=("Arial", 22, "bold"),
        bg="#1E3A8A",
        fg="white"
    ).pack(fill=X, pady=10)

    Label(
        dashboard,
        text="Welcome Teacher!",
        bg="#F3F4F6",
        font=("Arial", 18)
    ).pack(pady=40)

    Button(
        dashboard,
        text="📅 Mark Attendance",
        width=25,
        command=open_attendance
    ).pack(pady=20)

    Button(
        dashboard,
        text="📝 View Complaints",
        width=25,
        command=open_complaints
    ).pack(pady=20)

    Button(
        dashboard,
        text="💬 Chat",
        width=25,
        command=lambda: open_chat_window("Teacher")
    ).pack(pady=20)

   