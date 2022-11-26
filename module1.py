# importing socket
import socket

# importing datetime module
from datetime import datetime
now = datetime.now().time()
current_time=str(now)

# create socket object for client
client = socket.socket()

# taking user name as input
name = input("Enter Your Name\n")

# connecting client to localhost
client.connect(('localhost',9999))

# client send their name and current time to server side
client.send(bytes('Current Client Name is '+name+'\nClient Connected to Server at '+current_time+' Time', 'utf-8'))
print(client.recv(1024).decode())
