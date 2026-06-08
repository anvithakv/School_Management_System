# ==========================================
# STEP 1 : IMPORT LIBRARIES
# ==========================================

from tkinter import *
from tkinter import ttk

from database import cursor


# ==========================================
# STEP 2 : LOAD ATTENDANCE
# ==========================================

def load_attendance():

    query = """
    SELECT
    attendance_id,
    student_id,
    date,
    status
    FROM attendance
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)


# ==========================================
# STEP 3 : OPEN WINDOW
# ==========================================

def open_view_attendance():

    global tree

    window = Toplevel()

    window.title("View Attendance")
    window.geometry("900x500")

    Label(
        window,
        text="ATTENDANCE RECORDS",
        font=("Arial",20,"bold")
    ).pack(pady=20)

    tree = ttk.Treeview(
        window,
        columns=(
            "ID",
            "Student ID",
            "Date",
            "Status"
        ),
        show="headings"
    )

    tree.heading("ID", text="ID")
    tree.heading("Student ID", text="Student ID")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")

    tree.column("ID", width=80)
    tree.column("Student ID", width=150)
    tree.column("Date", width=200)
    tree.column("Status", width=150)

    tree.pack(
        fill=BOTH,
        expand=True,
        padx=20,
        pady=20
    )

    load_attendance()