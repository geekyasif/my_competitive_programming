import socket

#creating socket for client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting client by passing ip and port
client.connect(('127.0.0.1',55555))

# asking name from client to specify
name = input("Enter you name : ")

#sending the name in bytes
client.send(bytes(name,'utf-8'))

#recieving massge from server
message = client.recv(1024)

#decoding the message
print(message.decode())

#closing the connection
client.close()