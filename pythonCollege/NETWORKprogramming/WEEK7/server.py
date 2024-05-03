import socket
import os
import struct
import sys
import time

# Initialize socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)  # Change to appropriate address and port

# Bind socket to server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for connection from the client...")

# Accept connection from client
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

BUFFER_SIZE = 1024

def ls():
    file_list = os.listdir('.')
    response = "\n".join(file_list)
    client_socket.send(response.encode())

def rm(filename):
    if os.path.exists(filename):
        os.remove(filename)
        client_socket.send("File berhasil dihapus.".encode())
    else:
        client_socket.send("File tidak ditemukan.".encode())

def download(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            while True:
                data = file.read(BUFFER_SIZE)
                if not data:
                    break
                client_socket.send(data)
    else:
        client_socket.send("File tidak ditemukan.".encode())

def upload(filename, folder):
    if os.path.exists(os.path.join(folder, filename)):
        client_socket.send("File dengan nama yang sama sudah ada di server.".encode())
    else:
        data = client_socket.recv(BUFFER_SIZE)
        with open(os.path.join(folder, filename), 'wb') as file:
            file.write(data)
        client_socket.send(f"File '{filename}' berhasil disimpan di folder '{folder}'.".encode())

def size(filename):
    if os.path.exists(filename):
        file_size = os.path.getsize(filename) / (1024 * 1024)  # Convert to MB
        client_socket.send(f"Ukuran file {filename}: {file_size:.2f} MB".encode())
    else:
        client_socket.send("File tidak ditemukan.".encode())

def byebye():
    client_socket.send("Terima kasih! Koneksi akan diputus.".encode())
    client_socket.close()
    server_socket.close()
    sys.exit()

def connme():
    client_socket.send("Koneksi tetap terhubung.".encode())

while True:
    try:
        # Receive command from client
        command = client_socket.recv(1024).decode()
        if not command:
            break

        # Process command
        if command == "ls":
            ls()
        elif command.startswith("rm "):
            rm(command.split()[1])
        elif command.startswith("download "):
            filename = command.split()[1]
            download(filename)
        elif command.startswith("upload "):
            filename = command.split()[1]
            folder = "uploads"  # Folder tujuan untuk menyimpan file
            upload(filename, folder)
        elif command.startswith("size "):
            filename = command.split()[1]
            size(filename)
        elif command == "byebye":
            byebye()
        elif command == "connme":
            connme()
        else:
            client_socket.send("Perintah tidak valid.".encode())
    except Exception as e:
        print(f"Error: {e}")
        break
