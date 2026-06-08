from tkinter import *
from tkinter.scrolledtext import ScrolledText
import socket
import threading
from tkinter import filedialog
import os
import shutil


def open_chat_window(username):

    window = Toplevel()

    window.title(f"Chat - {username}")
    window.geometry("600x500")

    chat_area = ScrolledText(
        window,
        width=70,
        height=20
    )

    chat_area.pack(
        padx=10,
        pady=10
    )
    

    message_entry = Entry(
        window,
        width=50
    )

    message_entry.pack(
        side=LEFT,
        padx=10,
        pady=10
    )

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        client.connect(
            ("127.0.0.1", 5000)
        )

    except:

        chat_area.insert(
            END,
            "Server Not Running\n"
        )

        return

    def receive_messages():

        while True:

            try:

                message = client.recv(
                    1024
                ).decode()

                chat_area.insert(
                    END,
                    message + "\n"
                )

                chat_area.see(END)

            except:
                break

    thread = threading.Thread(
        target=receive_messages
    )

    thread.daemon = True

    thread.start()
    def share_file():

        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        shared_folder = os.path.join(
            os.getcwd(),
            "shared_files"
        )

        os.makedirs(
            shared_folder,
            exist_ok=True
        )

        destination = os.path.join(
            shared_folder,
            os.path.basename(file_path)
        )
        
        if os.path.exists(destination):

            chat_area.insert(
                END,
                "File already shared.\n"
            )

        else:

            shutil.copy(
                file_path,
                destination
            )
        

        file_message = (
            username +
            " shared file: " +
            os.path.basename(file_path)
        )

        client.send(
            file_message.encode()
        )
        chat_area.insert(
    END,
    file_message + "\n"
        )

        chat_area.see(END)


    def send_message():

        message = message_entry.get()

        if message:

            full_message = (
                username +
                ": " +
                message
            )

            client.send(
                full_message.encode()
            )

            message_entry.delete(
                0,
                END
            )

    Button(
        window,
        text="Send",
        command=send_message
    ).pack(
        side=LEFT,
        padx=10
    )

    Button(
    window,
    text="📁 Share File",
    command=share_file
).pack(
    side=LEFT,
    padx=5
)