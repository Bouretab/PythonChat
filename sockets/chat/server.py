
import threading
import socket

port = int(input("Port : "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen()

clients = []
usernames = []

def broadcast(message, sender):
    author = sender.getpeername()[0]
    for client in clients:
        clientAdress = client.getpeername()[0]
        if author != clientAdress:
            client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode('utf-8'))
            broadcast(message, client)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            print(f'{username} left the chat')
            broadcast(f"{username} left the chat".encode('utf-8'), client)
            usernames.remove(username)
            break

def receive():
    while True:
        client, adress = server.accept()
        print(f"{str(adress)} is connected")

        client.send('NICK'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f'{username} joined the chat')
        broadcast(f'{username} joined the chat'.encode('utf-8'), client)
        client.send('Connected'.encode('utf-8'))

        thread = threading.Thread(target = handle, args = (client,))
        thread.start()

print("Server started")
receive()