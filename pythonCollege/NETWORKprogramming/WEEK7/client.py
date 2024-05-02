import socket

# Initialize socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)  # Change to appropriate address and port

# Connect to server
client_socket.connect(server_address)
print(f"Connected to server {server_address}")

def send_command(command):
    # Send command to server
    client_socket.send(command.encode())

    # Process response from server
    response = client_socket.recv(1024).decode()
    print(response)

while True:
    try:
        # Input command from user
        command = input("Masukkan perintah (ls/rm/download/upload/size/byebye/connme): ")

        # Send command to server and receive response
        send_command(command)

        if command == "byebye":
            break
    except Exception as e:
        print(f"Error: {e}")
        break

# Close socket
client_socket.close()
