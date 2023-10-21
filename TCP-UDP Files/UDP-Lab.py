# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 16:43:44 2023

@author: clement
"""

import socket
import threading
import time

# Create a UDP socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 12345))

def handle_client(client_address):
    start_time = time.time()
    data, addr = server_socket.recvfrom(1024)
    end_time = time.time()
    latency = end_time - start_time
    print(f"Received {data} from {addr} with latency: {latency} seconds.")
    server_socket.sendto(data, addr)
    
# Main function to handle incoming connections
def main():
    print("Starting ...")
    while True:
        threading.Thread(target=handle_client, args=(server_socket,)).start()


if __name__ == "__main__":
    main()
    
#==============================================================================
 
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to upload a file
def upload_file(filename):
    with open(filename, 'rb') as f:
        data = f.read(1024)
        while data:
            client_socket.sendto(data, ("localhost", 12345))
            data = f.read(1024)

# Function to download a file
def download_file(filename):
    with open(filename, 'wb') as f:
        while True:
            data, addr = client_socket.recvfrom(1024)
            if not data:
                break
            f.write(data)

# Function to calculate throughput, bandwidth and transfer rate
def calculate_metrics(data_size, time_taken):
    throughput = data_size - time_taken
    bandwidth =  data_size - time_taken
    transfer_rate = (data_size * 8) / time_taken
    return throughput, bandwidth, transfer_rate

# UDP server code
def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 12345))
    
    while True:
        start_time = time.time()
        data, addr = server_socket.recvfrom(1024)
        end_time = time.time()
        
        latency = end_time - start_time
        throughput, bandwidth, transfer_rate = calculate_metrics(len(data), latency)
        
        print(f"Received {data} from {addr}")
        print(f"Metrics: Latency={latency}s, Throughput={throughput}B/s, Bandwidth={bandwidth}B/s, TransferRate={transfer_rate}bps")
        
        # Echo back the data to the client
        server_socket.sendto(data, addr)
        
# UDP Client Code for File Upload and Download
def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    
    # Upload a file
    with open("example_upload.txt", 'rb') as f:
        data = f.read(1024)
        while data:
            client_socket.sendto(data, ("localhost", 12345))
            data = f.read(1024)

    # Download a file
    with open("example_upload.txt", 'wb') as f:
        while True:
            data, addr = client_socket.recvfrom(1024)
            if not data:
                break
            f.write(data)
        
# UDP Client Code for Broadcasting
def udp_broadcast_client():
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Broadcast a file
    with open("example_broadcast.txt","rb") as f:
        data = f.read(1024)
        while data:
            broadcast_socket.sendto(data, ('broadcast', 12345))
            data = f.read(1024)  
            
# Main function to run server and client
if __name__ == "__main__":
    threading.Thread(target=udp_server).start()
    threading.Thread(target=udp_client).start()
    threading.Thread(target=udp_broadcast_client).start()
 
    
 
    
 
    
 
    
 
    
 
    
    
    
    
    
    
    
    
    