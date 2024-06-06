import socket
import threading
import os
import time

BUFFER_SIZE = 24 * 1024 * 1024  # 24 MB

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break

            if message == b"FILE_TRANSFER_COMPLETE":
                print("File transfer complete.")
            elif message.startswith(b"file:"):
                _, sender, filename = message.decode().split(":", 2)
                threading.Thread(target=receive_file, args=(client_socket, filename)).start()
            else:
                try:
                    print(message.decode())
                except UnicodeDecodeError:
                    print("Received non-text data")
        except Exception as e:
            print(f"An error occurred while receiving messages: {e}")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        print("\nMenu:")
        print("1. Send a Unicast Message")
        print("2. Send a Multicast Message")
        print("3. Send a Broadcast Message")
        print("4. Send a File")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            recipient = input("Enter the username to send a message to: ")
            message = input("Enter your message: ")
            client_socket.send(f"unicast:{recipient}:{message}".encode())
            
        elif choice == "2":
            recipients = input("Enter the usernames to send a message to (comma-separated): ")
            message = input("Enter your message: ")
            client_socket.send(f"multicast:{recipients}:{message}".encode())
            
        elif choice == "3":
            message = input("Enter your broadcast message: ")
            client_socket.send(f"broadcast:{message}".encode())
            
        elif choice == "4":
            recipient = input("Enter the username to send a file to: ")
            filename = input("Enter the filename: ")

            if os.path.isfile(filename):
                client_socket.send(f"file:{recipient}:{filename}".encode())
                send_file(client_socket, filename)
            else:
                print(f"File {filename} not found. Please check the file path and try again.")
            
        elif choice == "5":
            client_socket.close()
            break
        else:
            print("Invalid choice. Please try again.")

def send_file(client_socket, file_path):
    try:
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(BUFFER_SIZE)
                if not data:
                    break
                client_socket.sendall(data)
                time.sleep(0.01)  # Introduce a small delay to avoid sending data too quickly
            client_socket.send(b"FILE_TRANSFER_COMPLETE")
    except Exception as e:
        print(f"Error sending file {file_path}: {e}")

def receive_file(client_socket, filename):
    try:
        with open(f"received_{os.path.basename(filename)}", 'wb') as file:
            while True:
                data = client_socket.recv(BUFFER_SIZE)
                if data == b"FILE_TRANSFER_COMPLETE":
                    print(f"Received file {os.path.basename(filename)}")
                    break
                file.write(data)
        print(f"File {os.path.basename(filename)} successfully received and saved.")
    except Exception as e:
        print(f"An error occurred while receiving file {filename}: {e}")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.169.13.13', 11005))

    username = input("Enter your username: ")
    client_socket.send(username.encode())

    response = client_socket.recv(1024).decode()
    if response == "Username already taken. Disconnecting.":
        print(response)
        client_socket.close()
    else:
        print(response)
        threading.Thread(target=receive_messages, args=(client_socket,)).start()
        send_messages(client_socket)

if __name__ == "__main__":
    start_client()
