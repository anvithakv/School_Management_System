# ==========================================
# STEP 1 : IMPORT REQUIRED LIBRARIES
# ==========================================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from database import cursor, conn


# ==========================================
# STEP 2 : LOAD COMPLAINTS
# ==========================================

def load_complaints():

    for row in tree.get_children():
        tree.delete(row)

    query = """
    SELECT
    complaints.complaint_id,
    students.name,
    complaints.complaint,
    complaints.status
    FROM complaints
    JOIN students
    ON complaints.student_id = students.student_id
    """
    

    cursor.execute(query)

    rows = cursor.fetchall()

    print("ROWS:", rows)

    for row in rows:
        tree.insert("", END, values=row)


# ==========================================
# STEP 3 : RESOLVE COMPLAINT
# ==========================================

def resolve_complaint():

    selected = tree.focus()

    if not selected:

        messagebox.showerror(
            "Error",
            "Please Select Complaint"
        )

        return

    data = tree.item(selected)

    values = data["values"]

    complaint_id = values[0]

    query = """
    UPDATE complaints
    SET status='Resolved'
    WHERE complaint_id=%s
    """

    cursor.execute(
        query,
        (complaint_id,)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Complaint Resolved"
    )

    load_complaints()


# ==========================================
# STEP 4 : CREATE WINDOW
# ==========================================

def open_complaints():

    global tree

    window = Toplevel()

    window.title("Complaints Management")
    window.geometry("1000x600")
    window.configure(bg="#F3F4F6")
    
    # ==========================================
    # STEP 5 : TITLE
    # ==========================================

    Label(
        window,
        text="COMPLAINTS MANAGEMENT",
        font=("Arial",20,"bold"),
        bg="#F3F4F6"
    ).pack(pady=20)

    # ==========================================
    # STEP 6 : RESOLVE BUTTON
    # ==========================================

    Button(
        window,
        text="Resolve Complaint",
        bg="#2563EB",
        fg="white",
        font=("Arial",10,"bold"),
        command=resolve_complaint
    ).pack(pady=10)

    # ==========================================
    # STEP 7 : TREEVIEW STYLE
    # ==========================================

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Treeview",
        rowheight=30,
        font=("Arial",11)
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial",12,"bold")
    )

    # ==========================================
    # STEP 8 : TREEVIEW
    # ==========================================
    tree = ttk.Treeview(
    window,
    columns=(
        "ID",
        "Student",
        "Complaint",
        "Status"
    ),
    show="headings"
)
    

    tree.heading("ID", text="ID")
    tree.heading("Student", text="Student")
    tree.heading("Complaint", text="Complaint")
    tree.heading("Status", text="Status")

    tree.column("ID", width=80)
    tree.column("Student", width=200)
    tree.column("Complaint", width=500)
    tree.column("Status", width=150)

    

    tree.pack(
        fill=BOTH,
        expand=True,
        padx=20,
        pady=20
    )
   


    # ==========================================
    # STEP 9 : LOAD COMPLAINTS
    # ==========================================

    load_complaints()