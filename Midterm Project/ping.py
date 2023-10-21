import socket
import time
import pandas as pd

# Import data from excel file
df = pd.read_excel('./SensorData.xlsx')
values = df['Enclosed Wheel Rotation Data'].values
rotation = 0
turn = 0

# Server configuration
server_ip = "localhost"
server_port = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Packet loss Handling Method
client_socket.settimeout(5)

# Connect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to {server_ip}:{server_port}")

while True:
    # Measure the time before sending a "Ping" message
    start_time = time.time()
    
    # Send a "Ping" message to the server
    message = "Ping"
    client_socket.send(message.encode('utf-8'))
    
    # Change rotation/turn values
    if rotation < 9:
        rotation += 1
    else:
        rotation = 0
        turn += 1
    
    try:
        # Receive the "Pong" response with the timeout
        data = client_socket.recv(1024).decode('utf-8')
        
        # Measure the time after receiving the "Pong" response
        end_time = time.time()

        # Calculate the Round Trip Time (RTT) in milliseconds
        rtt_ms = (end_time - start_time) * 1000
        print(f"Received: {data}, RTT: {rtt_ms:.2f} ms")

    except socket.timeout:
        print("Timeout: No response received within the specified timeout.")
    
    # Wait for user input to continue
    input("Press Enter to send another ping...")

# Close the client socket
client_socket.close()
