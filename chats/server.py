import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((HOST, PORT))
server.listen()

clients = []

print("Server Started...")


def broadcast(message):

    for client in clients:

        try:
            client.send(message)

        except:
            pass


def handle_client(client):

    while True:

        try:

            message = client.recv(1024)

            broadcast(message)

        except:

            clients.remove(client)

            client.close()

            break


while True:

    client, address = server.accept()

    print("Connected:", address)

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()