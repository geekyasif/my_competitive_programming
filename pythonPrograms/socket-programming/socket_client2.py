import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
name = input("Enter the name :")
client.send(bytes(name,encoding='utf-8'))
message = client.recv(1024)
print(message.decode())
client.close()