import socket

# creating a server with internet and tcp
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created Successfully")

# binding the socket with server
server.bind(('127.0.0.1', 55555))
print("Waiting to the client to connect with the server")

#connecting to the client and its take an argument number of client to connect
server.listen()

#creating the server in infinite loop to connect every client
while True:
    # accecpting the client address to identify
    client, address = server.accept()

    # recieving the name of client and decoding into string from bytes
    name = client.recv(1024).decode()

    # printing message to check who is connect
    print(f"Connected succesfully with {name} whose ip is {address}")

    # sending to the client a successfull connetec to the server
    client.send("Successfully Connected to the server".encode('utf-8'))

    #closing the client server
    client.close()