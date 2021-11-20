#   Voici le chatroom n°1
#   Ce chatroom envoie le message a tout le monde ce qui fait que l'envoyeur voit 2 fois son message





import threading
import socket

host = input('IP : ')
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode('utf-8'))
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            print(f'{username} left the chat')
            broadcast(f"{username} left the chat".encode('utf-8'))
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
        broadcast(f'{username} joined the chat'.encode('utf-8'))
        client.send('Connected'.encode('utf-8'))

        thread = threading.Thread(target = handle, args = (client,))
        thread.start()

print("Server started")
receive()