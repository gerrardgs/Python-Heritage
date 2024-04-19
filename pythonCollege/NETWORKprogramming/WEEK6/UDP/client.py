import socket

# Server configuration (same as server)
server_ip = "127.0.0.1"
server_port = 20001
buffer_size = 1024

# Create UDP socket
try:
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
except socket.error as err:
    print("Error creating socket:", err)
    exit(1)

# Continuously get user input and send messages
while True:
    try:
        # Get user input for custom message
        custom_message = input("Enter message to send (or 'quit' to exit): ")

        # Check for exit command
        if custom_message.lower() == "quit":
            break

        # Encode message
        bytes_to_send = custom_message.encode()

        # Send message to server
        UDPClientSocket.sendto(bytes_to_send, (server_ip, server_port))

        # Receive response from server (optional)
        # Uncomment if you want the client to wait for a response
        # msg_from_server = UDPClientSocket.recvfrom(buffer_size)
        # print("Message from Server:", msg_from_server[0].decode())
    except socket.error as err:
        print("Error during communication:", err)
        # Handle potential errors (e.g., server unavailable)
        # You might choose to retry or exit gracefully

# Close the socket (optional, will happen automatically on program exit)
UDPClientSocket.close()
print("Client shutting down")
