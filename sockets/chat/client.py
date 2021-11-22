import socket
import threading

host, port = (input('IP : '), int(input('Port : ')))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
username = input('Username : ')

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(username.encode('utf-8'))
            else:
                print(message)

        except:
            print('An error occured')
            client.close()
            break

def write():
    while True:
        message = f'{username} : {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()