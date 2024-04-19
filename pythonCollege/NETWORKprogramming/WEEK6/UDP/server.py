import socket

# Server configuration
local_ip = "127.0.0.1"
local_port = 20001
buffer_size = 1024

# Create UDP socket
try:
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
except socket.error as err:
    print("Error creating socket:", err)
    exit(1)

# Bind to IP and port
try:
    UDPServerSocket.bind((local_ip, local_port))
    print("UDP server up and listening on", local_ip, ":", local_port)
except socket.error as err:
    print("Error binding:", err)
    exit(1)

# Continuously receive and process messages
while True:
    try:
        # Receive data from client
        bytes_address_pair = UDPServerSocket.recvfrom(buffer_size)
        message = bytes_address_pair[0].decode()  # Decode received message
        address = bytes_address_pair[1]

        # Print client message and IP
        print("Message from Client:", message)
        print("Client IP Address:", address)

        # Prepare server response (customizable)
        server_msg = f"Hello UDP Client! You sent: {message}"
        bytes_to_send = server_msg.encode()

        # Send response to client
        UDPServerSocket.sendto(bytes_to_send, address)
    except socket.error as err:
        print("Error during communication:", err)
        # Handle potential errors (e.g., lost connection, invalid data)
        # You might choose to continue listening or close the socket

# Close the socket (optional, will happen automatically on program exit)
UDPServerSocket.close()
print("Server shutting down")
