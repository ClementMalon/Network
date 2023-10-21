#!/bin/bash	

# Function to set up TCP server using netcat
setup_tcp_server(){
    echo "Setting up TCP server on port 12345 using netcat..."
    { echo "Server: Hello, Client!"; cat; } | nc -l 12345
}

# Function to simulate TCP client 1 using netcat
setup_tcp_client1(){
    echo "Setting up TCP client1..."
    { echo "Client 1: Hello, Server!"; cat; } | nc localhost 12345 > client1_output.txt
}

# Function to simulate TCP client 2 using netcat
setup_tcp_client2(){
    echo "Setting up TCP client2..."
    { echo "Client 2: Hello, Server!"; cat; } | nc localhost 12345 > client2_output.txt
}

# Function to test latency using ping
test_latency(){
    echo "Testing latency to localhost..."
    ping -c 4 localhost
}

# Function to test bandwidth using iperf3
test_bandwidth(){
    echo "Testing bandwidth using iperf3..."
    iperf3 -c localhost
}

# Function to measure data transfer rate between server and clients
measure_transfer_rate(){
    start_time=$(date + %s%N)
    setup_tcp_client1 &
    setup_tcp_client2 & 
    end_time=$(date + %s%N)
    elapsed_time=$((end_time - start_time))
    elapsed_time_in_seconds=$(echo "scale=9; $elapsed_time / 1000000000" | bc)
    echo "Data transfer time: $elapsed_time_in_seconds seconds"
}

# Main function to execute the lab setup
main(){
    echo "Starting the lab session setup..."
    
    # Step 1: Setting up TCP server
    setup_tcp_server &
    sleep 2 # Give the server time to start_time
    
    # Step 2: Measure data transfer rate
    measure_transfer_rate
    
    # Step 3: Performance testing
    test_latency
    test_bandwidth
    
    echo "Lab session setup complete."
}

# Execute the main function 
main










