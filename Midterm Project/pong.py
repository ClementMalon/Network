import socket
import time 

# Server configuration
server_ip = "localhost"
server_port = 12345

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server is listening on {server_ip}:{server_port}")

# Accept incoming connections
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    
    if not data:
        break
    
    print(f"Received: {data}")

    # Send a response back to the client (pong)
    response = "Pong"
    client_socket.send(response.encode('utf-8'))

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
