# ==========================================
# STEP 1 : IMPORT REQUIRED LIBRARIES
# ==========================================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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
# STEP 3 : ADD FEE RECORD
# ==========================================

def add_fee():

    student_name = student_combo.get()

    if not student_name:
        messagebox.showerror(
            "Error",
            "Please Select Student"
        )
        return

    student_id = student_dict[student_name]

    amount = amount_entry.get()

    if not amount:
        messagebox.showerror(
            "Error",
            "Enter Fee Amount"
        )
        return

    status = status_var.get()

    query = """
    INSERT INTO fees
    (student_id,amount,status)
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            student_id,
            amount,
            status
        )
    )

    conn.commit()

   


    messagebox.showinfo(
        "Success",
        "Fee Added Successfully"
    )

    load_fees()


# ==========================================
# STEP 4 : LOAD FEES INTO TREEVIEW
# ==========================================

def load_fees():

    for row in tree.get_children():
        tree.delete(row)

    query = """
    SELECT
    fees.fee_id,
    students.name,
    fees.amount,
    fees.status
    FROM fees
    JOIN students
    ON fees.student_id =
    students.student_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", END, values=row)


# ==========================================
# STEP 5 : CREATE FEE MANAGEMENT WINDOW
# ==========================================

def open_fee_management():

    global student_combo
    global amount_entry
    global status_var
    global tree
    global student_dict

    student_dict = {}

    window = Toplevel()

    window.title("Fee Management")
    window.geometry("1000x600")
    window.configure(bg="#F3F4F6")

    # ==========================================
    # STEP 6 : PAGE TITLE
    # ==========================================

    Label(
        window,
        text="FEE MANAGEMENT",
        font=("Arial", 20, "bold"),
        bg="#F3F4F6"
    ).pack(pady=20)

    # ==========================================
    # STEP 7 : FORM FRAME
    # ==========================================

    form_frame = Frame(
        window,
        bg="white",
        bd=2,
        relief="raised"
    )

    form_frame.pack(
        padx=20,
        pady=10,
        fill=X
    )

    # ==========================================
    # STEP 8 : STUDENT COMBOBOX
    # ==========================================

    Label(
        form_frame,
        text="Student",
        bg="white",
        font=("Arial", 12)
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

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
    # STEP 9 : AMOUNT ENTRY
    # ==========================================

    Label(
        form_frame,
        text="Amount",
        bg="white",
        font=("Arial", 12)
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    amount_entry = Entry(
        form_frame,
        width=33
    )

    amount_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    # ==========================================
    # STEP 10 : STATUS RADIO BUTTONS
    # ==========================================

    status_var = StringVar()

    status_var.set("Pending")

    Radiobutton(
        form_frame,
        text="Paid",
        variable=status_var,
        value="Paid",
        bg="white"
    ).grid(
        row=2,
        column=0,
        pady=10
    )

    Radiobutton(
        form_frame,
        text="Pending",
        variable=status_var,
        value="Pending",
        bg="white"
    ).grid(
        row=2,
        column=1,
        pady=10
    )

    # ==========================================
    # STEP 11 : ADD FEE BUTTON
    # ==========================================

    Button(
        form_frame,
        text="Add Fee",
        bg="#2563EB",
        fg="white",
        font=("Arial", 10, "bold"),
        command=add_fee
    ).grid(
        row=3,
        column=0,
        columnspan=2,
        pady=10
    )

    # ==========================================
    # STEP 12 : TREEVIEW STYLE
    # ==========================================

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Treeview",
        rowheight=30,
        font=("Arial", 11)
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial", 12, "bold")
    )

    # ==========================================
    # STEP 13 : CREATE TREEVIEW
    # ==========================================

    tree = ttk.Treeview(
        window,
        columns=(
            "ID",
            "Student",
            "Amount",
            "Status"
        ),
        show="headings"
    )

    tree.heading("ID", text="ID")
    tree.heading("Student", text="Student")
    tree.heading("Amount", text="Amount")
    tree.heading("Status", text="Status")

    tree.column("ID", width=80)
    tree.column("Student", width=250)
    tree.column("Amount", width=150)
    tree.column("Status", width=150)

    tree.pack(
        fill=BOTH,
        expand=True,
        padx=20,
        pady=20
    )

    # ==========================================
    # STEP 14 : LOAD DATA
    # ==========================================

    load_students()
    load_fees()