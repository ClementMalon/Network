#!/bin/bash	

# Function to simulate TCP client 1 using netcat
setup_tcp_client1(){
    echo "Setting up TCP client 1..."
    echo "Hello from Client 1" | nc localhost 12345
}

# Function to simulate TCP client 2 using netcat
setup_tcp_client2(){
    echo "Setting up TCP client 2..."
    echo "Hello from Client 2" | nc localhost 12345   
}

# Function to test latency using ping
test_latency(){
    echo "Testing latency to localhost..."
    ping -c 4 localhost
}

# Function to test bandwidth using iperf3
test_bandwith(){
    echo "Testing bandwidth using iperf3..."
    iperf3 -c localhost
}

# Main function to execute the lab setup
main(){
       echo "Starting the lab session setup..."
       
       # Step 2: Setting up TCP server
       setup_tcp_server &
       sleep 2 # Give the server time to start
       
       # Step 3: Setting up TCP client
       setup_tcp_client1 &
       setup_tcp_client2 &
       
       # Step 4: Performance testing
       test_latency &
       test_bandwidth &
       
       echo "Lab session setup complete."
}

# Execute the main function 
main
