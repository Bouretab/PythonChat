import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host, port = '127.0.0.1', 4000
server.bind((host, port))
server.listen(4)
client_connected = True 
socket_objs = [server]

print('Welcome in the chat')

while client_connected:
    liste_lu, liste_acce_Ecrit, exception = select.select(socket_objs, [], socket_objs)

    for socket_obj in liste_lu:
        if socket_obj is server:
            client, adress = server.accept()
            socket_objs.append(client)

        else:
            recv_data = socket_obj.recv(128).decode("utf-8")

            if recv_data:
                print(recv_data)

            else:
                socket_objs.remove(socket_obj)
                print("A user left the chat")
                print(f'{len(socket_objs) - 1} users are in the chat')