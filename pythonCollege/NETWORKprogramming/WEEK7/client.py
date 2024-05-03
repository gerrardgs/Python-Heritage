import socket
import os

# Initialize socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)  # Change to appropriate address and port

# Connect to server
client_socket.connect(server_address)

BUFFER_SIZE = 1024

def ls():
    client_socket.send("ls".encode())
    response = client_socket.recv(BUFFER_SIZE).decode()
    print("File list:")
    print(response)

def rm(filename):
    client_socket.send(f"rm {filename}".encode())
    response = client_socket.recv(BUFFER_SIZE).decode()
    print(response)

def download(filename):
    client_socket.send(f"download {filename}".encode())
    with open(filename, 'wb') as file:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            file.write(data)
    print(f"File '{filename}' berhasil diunduh.")

def upload(filename):
    if os.path.exists(filename):
        client_socket.send(f"upload {filename}".encode())
        response = client_socket.recv(BUFFER_SIZE).decode()
        print(response)
        if response.startswith("File dengan nama yang sama sudah ada di server."):
            return
        with open(filename, 'rb') as file:
            while True:
                data = file.read(BUFFER_SIZE)
                if not data:
                    break
                client_socket.send(data)
        print(f"File '{filename}' berhasil diunggah ke server.")
    else:
        print(f"File '{filename}' tidak ditemukan.")

def size(filename):
    client_socket.send(f"size {filename}".encode())
    response = client_socket.recv(BUFFER_SIZE).decode()
    print(response)

def byebye():
    client_socket.send("byebye".encode())
    response = client_socket.recv(BUFFER_SIZE).decode()
    print(response)
    client_socket.close()

def connme():
    client_socket.send("connme".encode())
    response = client_socket.recv(BUFFER_SIZE).decode()
    print(response)

while True:
    command = input("\nMasukkan perintah (ls/rm/download/upload/size/byebye/connme): ").strip()
    if command == "ls":
        ls()
    elif command.startswith("rm "):
        filename = command.split()[1]
        rm(filename)
    elif command.startswith("download "):
        filename = command.split()[1]
        download(filename)
    elif command.startswith("upload "):
        filename = command.split()[1]
        upload(filename)
    elif command.startswith("size "):
        filename = command.split()[1]
        size(filename)
    elif command == "byebye":
        byebye()
        break
    elif command == "connme":
        connme()
    else:
        print("Perintah tidak valid.")
