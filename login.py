from tkinter import *
from tkinter import messagebox

from database import cursor
from admin.admin_dashboard import open_admin_dashboard
from student.student_dashboard import open_student_dashboard
from teacher.teacher_dashboard import open_teacher_dashboard

def login():

    username = username_entry.get()
    password = password_entry.get()

    query = """
    SELECT role
    FROM users
    WHERE username=%s
    AND password=%s
    """

    cursor.execute(
        query,
        (username,password)
    )

    result = cursor.fetchone()

    if result:

        role = result[0]

        if role == "admin":
            open_admin_dashboard()

        elif role == "teacher":
             open_teacher_dashboard()
            

        elif role == "student":
            open_student_dashboard()
               
        else:
             messagebox.showerror(
            "Error",
            "Invalid Credentials"
        )


def open_login():

    global username_entry
    global password_entry

    root = Tk()

    root.title("School Management System")
    root.geometry("500x350")

    Label(
        root,
        text="LOGIN",
        font=("Arial",20,"bold")
    ).pack(pady=20)

    Label(root,text="Username").pack()

    username_entry = Entry(root,width=30)
    username_entry.pack(pady=5)

    Label(root,text="Password").pack()

    password_entry = Entry(
        root,
        width=30,
        show="*"
    )
    password_entry.pack(pady=5)

    Button(
        root,
        text="Login",
        command=login,
        width=20
    ).pack(pady=20)

    root.mainloop()