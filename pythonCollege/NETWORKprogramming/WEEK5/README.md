# LAPORAN PRAKTIKUM TUGAS TEORI JARKOM
<br>

<h3>NAMA: Gerrard Sebastian</h3>
<h3>NIM: 1203220018</h3>
<h3>KELAS: IF-02-01</h3>
<br>

# SOAL
1. Buat sebuah program file transfer protocol menggunakan socket programming dengan beberapa perintah dari client seperti berikut:
- ls : ketika client menginputkan command tersebut, maka server akan memberikan daftar file dan folder 
- rm {nama file} : ketika client menginputkan command tersebut, maka server akan menghapus file dengan acuan nama file yang diberikan pada parameter pertama
- download {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan file dengan acuan nama file yang diberikan pada parameter pertama
- upload {nama file} : ketika client menginputkan command tersebut, maka server akan menerima dan menyimpan file dengan acuan nama file yang diberikan pada parameter pertama
- size {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan informasi file dalam satuan MB (Mega bytes) dengan acuan nama file yang diberikan pada parameter pertama
- byebye : ketika client menginputkan command tersebut, maka hubungan socket client akan diputus
- connme : ketika client menginputkan command tersebut, maka hubungan socket client akan terhubung.
<br>

# JAWABAN
<h3>LINK GITHUB: https://bit.ly/TgsTeoriJarkom2 </h3>

<h3><strong>Disclaimer: Program Dibuat Menggunakan Bahasa Python</strong></h3>

### 1.	Server Program
```python
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

def upload(filename):
    data = client_socket.recv(BUFFER_SIZE)
    with open(filename, 'wb') as file:
        file.write(data)
    client_socket.send("File berhasil disimpan.".encode())

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
            upload(filename)
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
```
<br>

Penjelasan:


<br>

### 2.	Client Program
```python
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
```
<br>

Penjelasan:


<br>

### Konklusi:


<br>

# CARA MENGGUNAKAN TIAP FITUR YANG TERSEDIA (7 FITUR)


<br>

### OUTPUT PROGRAM
#### SERVER:
![server](https://github.com/gerrardgs/Python-Heritage/assets/114888829/aabf8202-d953-41f9-98ad-0bd994dcceb4)

<br>

#### CLIENT:
![5 features exclude down and up](https://github.com/gerrardgs/Python-Heritage/assets/114888829/27b84b35-f3bc-4494-8afb-7be793d3dccd)

<br>

![download](https://github.com/gerrardgs/Python-Heritage/assets/114888829/15bc7adb-2d45-4178-861a-3b94746c908f)

<br>

![upload](https://github.com/gerrardgs/Python-Heritage/assets/114888829/a5b03fbc-751a-4e39-9aa1-4b6370bd9099)
