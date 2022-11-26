# importing socket
import socket

#  datetime module imported
from datetime import datetime
now = datetime.now().time()
current_time=str(now)

# creating socket object
server = socket.socket()
print("Socket Created")

# binding socket with localhost
server.bind(('localhost',9999))
server.listen()
print("waiting for connections...")
while True:

    # server accept client address
    client, addr = server.accept()

# recieving address
name = client.recv(1024).decode()
print("connected with", addr,'\n'+name)

# server sending current time to client
client.send(bytes('You Connected with server at :'+current_time+' Time',
'utf-8'))
client.close()
