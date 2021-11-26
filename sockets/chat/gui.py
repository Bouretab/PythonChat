from tkinter import *
import socket
import threading

host, port = (input('IP : '), int(input('Port : ')))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
username = input('Username : ')
message_row = 0

window = Tk()

window.title("Netchat")
window.geometry("480x300")
window.minsize(300,300)
window.iconbitmap("logo.ico")
window.config(background = '#000000')
#window.attributes('-alpha',0.1) #Rend la fênetre transparante

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(username.encode('utf-8'))
            else:
                new_message = Label(messages, text = message, font=('Consolas', 10), fg=('#ffffff')).grid(row=message_row ,column=0)
                message_row = message_row
        except:
            print('An error occured')
            client.close()
            break

def write():
    while True:
        message = f'{username} : {"test"}'
        client.send(message.encode('utf-8'))

def test():
    global entry
    print(entry.get())

input = Frame(window, bg='#000000', bd=1, relief=SUNKEN)
entry = Entry(input, bg='#000000', fg='#ffffff', font='Arial' ).grid(row = 0, column = 0)
bouton = Button(input, text="Envoyer", font=("arial"), bg='#000000', fg='#ffffff', command = test).grid(row = 0, column = 1 )
input.grid(row = 1, column = 0)

messages = Frame(window, bg='#000000', bd=1, relief=SUNKEN)

window.mainloop()

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()

