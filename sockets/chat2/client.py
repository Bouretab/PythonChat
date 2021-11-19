import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = '127.0.0.1', 4000
client_socket.connect((host, port))
name = input("Username : ")

if __name__ == "__main__":

    while True:

        message = input(f"{name} : ")
        client_socket.send(f"{name} : {message}".encode("utf-8"))