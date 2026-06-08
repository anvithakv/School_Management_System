# ==========================================
# STEP 1 : IMPORT MODULES
# ==========================================

from tkinter import *

from student.view_attendance import open_view_attendance
from student.view_fees import open_view_fees
from student.submit_complaint import open_submit_complaint
from chats.chat_window import open_chat_window

# ==========================================
# STEP 2 : STUDENT DASHBOARD
# ==========================================

def open_student_dashboard():

    dashboard = Toplevel()

    dashboard.title("Student Dashboard")
    dashboard.geometry("1000x600")
    dashboard.configure(bg="#F3F4F6")

    # ==========================================
    # HEADER
    # ==========================================

    header = Frame(
        dashboard,
        bg="#1E3A8A",
        height=80
    )

    header.pack(fill=X)

    Label(
        header,
        text="STUDENT PANEL",
        bg="#1E3A8A",
        fg="white",
        font=("Arial",20,"bold")
    ).pack(pady=20)

  

    Button(
        dashboard,
        text="📅 View Attendance",
        width=20,
        command=open_view_attendance
    ).pack(pady=15)

    Button(
        dashboard,
        text="💰 View Fees",
        width=20,
        command=open_view_fees
    ).pack(pady=15)

    Button(
        dashboard,
        text="📝 Submit Complaint",
        width=20,
        command=open_submit_complaint
    ).pack(pady=15)
    
    Button(
    dashboard,
    text="💬 Chat",
    command=lambda:
    open_chat_window("Student")
).pack(pady=10)
    

   