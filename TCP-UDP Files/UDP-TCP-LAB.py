# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:43:44 2023

@author: clement
"""

#!/usr/bin/env python3

import socket
import threading
import time

# UDP Server Code
def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 12345))

    print("UDP server started")

    while True:
        start_time = time.time()
        data, address = server_socket.recvfrom(1024)
        end_time = time.time()
        latency = end_time - start_time
        print(f"Received message: {data.decode()} from {address} with latency: {latency} seconds.")

        response = "Hello, Client!"
        server_socket.sendto(response.encode(), address)

# UDP Client Code
def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello, Server!"

    client_socket.sendto(message.encode(), ("localhost", 12345))

    data, address = client_socket.recvfrom(1024)
    print(f"Received response: {data.decode()} from {address}")

# TCP Server Code
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5)

    print("TCP server started")

    while True:
        client_socket, address = server_socket.accept()
        print(f"New connection from {address}")

        message = "Hello, Client!"
        client_socket.send(message.encode())

        data = client_socket.recv(1024)
        print(f"Received message: {data.decode()} from {address}")

        client_socket.close()

# TCP Client Code
def tcp_client(client_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(("localhost", 12345))

    data = client_socket.recv(1024)
    print(f"Received message: {data.decode()} from server")

    client_socket.sendall(f"Client {client_id}: Hello, Server!".encode())

    client_socket.close()

def main():
    # Create threads for UDP server and client
    udp_server_thread = threading.Thread(target=udp_server)
    udp_client_thread = threading.Thread(target=udp_client)

    # Create threads for TCP server and client
    tcp_server_thread = threading.Thread(target=tcp_server)
    tcp_client_thread = threading.Thread(target=tcp_client,args=[1])
    tcp_client_thread_2 = threading.Thread(target=tcp_client,args=[2])

    # Start the threads
    udp_server_thread.start()
    udp_client_thread.start()
    tcp_server_thread.start()
    tcp_client_thread.start()
    tcp_client_thread_2.start()

    # Wait for the threads to finish
    udp_server_thread.join()
    udp_client_thread.join()
    tcp_server_thread.join()
    tcp_client_thread.join()
    tcp_client_thread_2.join()

if __name__ == '__main__':
    main()