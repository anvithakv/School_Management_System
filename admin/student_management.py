from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from database import cursor, conn

#student function

def add_student():

    name = name_entry.get()
    class_name = class_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    query = """
    INSERT INTO students
    (name,class_name,phone,address)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (name,class_name,phone,address)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student Added Successfully"
    )

    load_students()

    #load students into treeview

def load_students():

    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("",END,values=row)

#delete student

def delete_student():

    selected = tree.focus()

    if not selected:
        messagebox.showerror(
            "Error",
            "Please select a student"
        )
        return

    data = tree.item(selected)

    values = data["values"]

    if not values:
        return

    student_id = values[0]

    cursor.execute(
        "DELETE FROM students WHERE student_id=%s",
        (student_id,)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student Deleted Successfully"
    )

    load_students()

#select students

def select_student(event):

    selected = tree.focus()

    data = tree.item(selected)

    values = data["values"]

    if values:

        name_entry.delete(0,END)
        class_entry.delete(0,END)
        phone_entry.delete(0,END)
        address_entry.delete(0,END)

        name_entry.insert(0,values[1])
        class_entry.insert(0,values[2])
        phone_entry.insert(0,values[3])
        address_entry.insert(0,values[4])

#update students

def update_student():

    selected = tree.focus()

    if not selected:
        messagebox.showerror(
            "Error",
            "Please select a student"
        )
        return

    data = tree.item(selected)

    values = data["values"]

    if not values:
        return

    student_id = values[0]

    query = """
    UPDATE students
    SET
    name=%s,
    class_name=%s,
    phone=%s,
    address=%s
    WHERE student_id=%s
    """

    cursor.execute(
        query,
        (
            name_entry.get(),
            class_entry.get(),
            phone_entry.get(),
            address_entry.get(),
            student_id
        )
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Student Updated Successfully"
    )

    load_students()

def open_student_management():

    global name_entry
    global class_entry
    global phone_entry
    global address_entry
    global tree

    window = Toplevel()

    window.title("Student Management")
    window.geometry("900x600")

    Label(window,text="Name").grid(row=0,column=0,padx=10,pady=10)

    name_entry = Entry(window,width=30)
    name_entry.grid(row=0,column=1)

    Label(window,text="Class").grid(row=1,column=0)

    class_entry = Entry(window,width=30)
    class_entry.grid(row=1,column=1)

    Label(window,text="Phone").grid(row=2,column=0)

    phone_entry = Entry(window,width=30)
    phone_entry.grid(row=2,column=1)

    Label(window,text="Address").grid(row=3,column=0)

    address_entry = Entry(window,width=30)
    address_entry.grid(row=3,column=1)

    Button(
        window,
        text="Add Student",
        command=add_student
    ).grid(row=4,column=0,pady=10)

    Button(
        window,
        text="Update Student",
        command=update_student
    ).grid(row=4,column=1,pady=10)

    Button(
        window,
        text="Delete Student",
        command=delete_student
    ).grid(row=4,column=2,pady=10)

    tree = ttk.Treeview(
        window,
        columns=(
            "ID",
            "Name",
            "Class",
            "Phone",
            "Address"
        ),
        show="headings"
    )

    tree.heading("ID",text="ID")
    tree.heading("Name",text="Name")
    tree.heading("Class",text="Class")
    tree.heading("Phone",text="Phone")
    tree.heading("Address",text="Address")

    tree.grid(
        row=5,
        column=0,
        columnspan=5,
        padx=20,
        pady=20
    )

    tree.bind(
        "<<TreeviewSelect>>",
        select_student
    )

    load_students()
