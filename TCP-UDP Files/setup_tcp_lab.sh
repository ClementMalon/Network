#!/bin/bash	

# Function to set up TCP server using netcat
setup_tcp_server(){
    echo "Setting up TCP server on port 12345 using netcat..."
    nc -l 12345
}

# Function to install xinetd for multi-threaded TCP server
install_xinetd(){
    echo "Installing xinetd..."
    sudo apt update
    sudo apt install -y xinetd
}

# Main function to execute the lab setup
main(){
    echo "Starting the lab session setup..."
    
    # Step 2: Setting up TCP server
    setup_tcp_server &
    
    # Step 5: Install xinedtd 
    install_xinetd
    
    echo "Lab session setup complete."
}

# Execute the main function 
main