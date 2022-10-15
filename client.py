import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.8.104" #127.0.0.1
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(12).decode(FORMAT))

send("Hello World!")
a = input()
send("Hello Everyone!")
a = input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE)