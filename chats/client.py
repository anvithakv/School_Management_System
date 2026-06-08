import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

print("Connected To Server")


# =========================
# RECEIVE MESSAGES
# =========================

def receive_messages():

    while True:

        try:

            message = client.recv(
                1024
            ).decode()

            print("\nAdmin:", message)

        except:
            break


# =========================
# START THREAD
# =========================

thread = threading.Thread(
    target=receive_messages
)

thread.daemon = True
thread.start()


# =========================
# SEND MESSAGES
# =========================

while True:

    message = input()

    client.send(
        message.encode()
    )