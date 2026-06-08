from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from database import cursor, conn

def add_teacher():

    name = name_entry.get()
    subject = subject_entry.get()
    phone = phone_entry.get()

    query = """
    INSERT INTO teachers
    (name,subject,phone)
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (name,subject,phone)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Teacher Added Successfully"
    )

    load_teachers()


def load_teachers():

    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM teachers")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)


def select_teacher(event):

    selected = tree.focus()

    if not selected:
        return

    data = tree.item(selected)

    values = data["values"]

    if not values:
        return

    name_entry.delete(0, END)
    subject_entry.delete(0, END)
    phone_entry.delete(0, END)

    name_entry.insert(0, values[1])
    subject_entry.insert(0, values[2])
    phone_entry.insert(0, values[3])



def update_teacher():

    selected = tree.focus()

    if not selected:
        messagebox.showerror(
            "Error",
            "Please select a teacher"
        )
        return

    data = tree.item(selected)

    values = data["values"]

    if not values:
        return

    teacher_id = values[0]

    query = """
    UPDATE teachers
    SET
    name=%s,
    subject=%s,
    phone=%s
    WHERE teacher_id=%s
    """

    cursor.execute(
        query,
        (
            name_entry.get(),
            subject_entry.get(),
            phone_entry.get(),
            teacher_id
        )
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Teacher Updated Successfully"
    )

    load_teachers()

def delete_teacher():

    selected = tree.focus()

    if not selected:
        messagebox.showerror(
            "Error",
            "Please select a teacher"
        )
        return

    data = tree.item(selected)

    values = data["values"]

    if not values:
        return

    teacher_id = values[0]

    cursor.execute(
        "DELETE FROM teachers WHERE teacher_id=%s",
        (teacher_id,)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Teacher Deleted Successfully"
    )

    load_teachers()


def open_teacher_management():

    global name_entry
    global subject_entry
    global phone_entry
    global tree

    window = Toplevel()

    window.title("Teacher Management")
    window.geometry("850x550")


    Label(window,text="Name").grid(
        row=0,column=0,padx=10,pady=10
    )

    name_entry = Entry(window,width=30)
    name_entry.grid(row=0,column=1)

    Label(window,text="Subject").grid(
        row=1,column=0
    )

    subject_entry = Entry(window,width=30)
    subject_entry.grid(row=1,column=1)

    Label(window,text="Phone").grid(
        row=2,column=0
    )

    phone_entry = Entry(window,width=30)
    phone_entry.grid(row=2,column=1)


    Button(
        window,
        text="Add Teacher",
        command=add_teacher
    ).grid(row=3,column=0,pady=10)

    Button(
        window,
        text="Update Teacher",
        command=update_teacher
    ).grid(row=3,column=1,pady=10)

    Button(
        window,
        text="Delete Teacher",
        command=delete_teacher
    ).grid(row=3,column=2,pady=10)


    tree = ttk.Treeview(
        window,
        columns=(
            "ID",
            "Name",
            "Subject",
            "Phone"
        ),
        show="headings"
    )

    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Subject", text="Subject")
    tree.heading("Phone", text="Phone")

    tree.grid(
        row=4,
        column=0,
        columnspan=5,
        padx=20,
        pady=20
    )

    tree.bind(
        "<<TreeviewSelect>>",
        select_teacher
    )

    load_teachers()

    
