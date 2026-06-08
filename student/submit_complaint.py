from tkinter import *
from tkinter import messagebox


from database import cursor, conn


def submit_complaint():

    complaint = complaint_text.get(
        "1.0",
        END
    )

    if complaint.strip() == "":
        return

    # Temporary Student ID
    student_id = 2

    query = """
    INSERT INTO complaints
    (student_id,complaint,status)
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            student_id,
            complaint,
            "Pending"
        )
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Complaint Submitted"
    )

    complaint_text.delete(
        "1.0",
        END
    )


def open_submit_complaint():

    global complaint_text

    window = Toplevel()

    window.title("Submit Complaint")
    window.geometry("600x400")

    Label(
        window,
        text="Enter Complaint",
        font=("Arial",15,"bold")
    ).pack(pady=10)

    complaint_text = Text(
        window,
        width=50,
        height=10
    )

    complaint_text.pack(pady=10)

    Button(
        window,
        text="Submit",
        command=submit_complaint
    ).pack(pady=10)