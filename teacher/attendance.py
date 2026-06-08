# ==========================================
# STEP 1 : IMPORT REQUIRED LIBRARIES
# ==========================================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from database import cursor, conn


# ==========================================
# STEP 2 : LOAD STUDENTS FROM DATABASE
# ==========================================

def load_students():

    cursor.execute(
        "SELECT student_id, name FROM students"
    )

    students = cursor.fetchall()

    student_dict.clear()

    student_names = []

    for student_id, name in students:

        student_dict[name] = student_id
        student_names.append(name)

    student_combo["values"] = student_names


# ==========================================
# STEP 3 : MARK ATTENDANCE
# ==========================================

def mark_attendance():

    student_name = student_combo.get()

    if not student_name:
        messagebox.showerror(
            "Error",
            "Please Select a Student"
        )
        return

    student_id = student_dict[student_name]

    attendance_date = date_entry.get()

    status = status_var.get()

    query = """
    INSERT INTO attendance
    (student_id,date,status)
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            student_id,
            attendance_date,
            status
        )
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Attendance Marked Successfully"
    )

    load_attendance()


# ==========================================
# STEP 4 : LOAD ATTENDANCE RECORDS
# ==========================================

def load_attendance():

    for row in tree.get_children():
        tree.delete(row)

    query = """
    SELECT
    attendance.attendance_id,
    students.name,
    attendance.date,
    attendance.status
    FROM attendance
    JOIN students
    ON attendance.student_id =
    students.student_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)


# ==========================================
# STEP 5 : CREATE ATTENDANCE WINDOW
# ==========================================

def open_attendance():

    global student_combo
    global date_entry
    global status_var
    global tree
    global student_dict

    student_dict = {}

    window = Toplevel()

    window.title("Attendance Management")
    window.geometry("1000x600")
    window.configure(bg="#F3F4F6")

    # ==========================================
    # STEP 6 : CREATE TITLE
    # ==========================================

    Label(
        window,
        text="ATTENDANCE MANAGEMENT",
        font=("Arial",20,"bold"),
        bg="#F3F4F6"
    ).pack(pady=20)

    # ==========================================
    # STEP 7 : CREATE FORM FRAME
    # ==========================================

    form_frame = Frame(
        window,
        bg="white",
        bd=2,
        relief="raised"
    )

    form_frame.pack(
        pady=10,
        padx=20,
        fill=X
    )

    # ==========================================
    # STEP 8 : STUDENT COMBOBOX
    # ==========================================

    Label(
        form_frame,
        text="Student",
        bg="white",
        font=("Arial",12)
    ).grid(row=0,column=0,padx=10,pady=10)

    student_combo = ttk.Combobox(
        form_frame,
        width=30
    )

    student_combo.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # ==========================================
    # STEP 9 : DATE ENTRY
    # ==========================================

    Label(
        form_frame,
        text="Date",
        bg="white",
        font=("Arial",12)
    ).grid(row=1,column=0,padx=10,pady=10)

    date_entry = Entry(
        form_frame,
        width=33
    )

    date_entry.grid(
        row=1,
        column=1
    )

    date_entry.insert(
        0,
        str(date.today())
    )

    # ==========================================
    # STEP 10 : ATTENDANCE STATUS
    # ==========================================

    status_var = StringVar()

    status_var.set("Present")

    Radiobutton(
        form_frame,
        text="Present",
        variable=status_var,
        value="Present",
        bg="white"
    ).grid(row=2,column=0,pady=10)

    Radiobutton(
        form_frame,
        text="Absent",
        variable=status_var,
        value="Absent",
        bg="white"
    ).grid(row=2,column=1,pady=10)

    # ==========================================
    # STEP 11 : MARK ATTENDANCE BUTTON
    # ==========================================

    Button(
        form_frame,
        text="Mark Attendance",
        bg="#2563EB",
        fg="white",
        command=mark_attendance
    ).grid(
        row=3,
        column=0,
        columnspan=2,
        pady=10
    )

    # ==========================================
    # STEP 12 : CREATE TREEVIEW
    # ==========================================

    tree = ttk.Treeview(
        window,
        columns=("ID","Student","Date","Status"),
        show="headings"
    )

    tree.heading("ID", text="ID")
    tree.heading("Student", text="Student")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")

    tree.pack(
        fill=BOTH,
        expand=True,
        padx=20,
        pady=20
    )

    # ==========================================
    # STEP 13 : LOAD DATA
    # ==========================================

    load_students()
    load_attendance()