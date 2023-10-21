# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 00:54:01 2023

@author: cleme
"""

import socket
import threading
import time
import subprocess

# This function sets up a TCP server.
def setup_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost',12345))
    server_socket.listen(10)
    print("TCP server set up on port 12345.")
    
# This function handles individual client connections.
def handle_client(client_socket):
    client_socket.sendall(b"Server: Hello, Client!")
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    client_socket.close()

# This function sets up a TCP client.
def setup_tcp_client(client_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost",12345))
    client_socket.sendall(f"Client {client_id}: Hello, Server!".encode())
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    client_socket.close()
    
# These functions test latency and bandwidth by running shell commands using the subprocess module.
def test_latency():
    print("Testing latency to localhost ...")
    subprocess.run(["ping","-c","4","localhost"])

def test_bandwidth():
    print("Testing bandwidth using iperf3 ...")
    subprocess.run(["iperf3","-c","localhost"])

# This function measures the data transfer rate.
def measure_transfer_rate():
    start_time = time.time()
    threads = []
    for i in range(1, 11):
        thread = threading.Thread(target=setup_tcp_client, args=(i,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Data transfer time: {elapsed_time} seconds.")
    
def main():
    print("Starting the lab session setup ...")
    server_thread = threading.Thread(target=setup_tcp_server)
    server_thread.daemon = True
    server_thread.start()
    client_thread = threading.Thread(target=setup_tcp_client(3))
    client_thread.daemon = True
    client_thread.start()
    # time.sleep(2)
    # measure_transfer_rate()
    # test_latency()
    # test_bandwidth()
    print("Lab session setup complete.")
    
if __name__ == "__main__":
    main()











    