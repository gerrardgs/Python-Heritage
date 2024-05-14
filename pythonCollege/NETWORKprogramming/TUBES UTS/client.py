import socket
import time

# Konfigurasi klien
HOST = "localhost"  # Alamat IP server
PORT = 65535  # Port server
BUFFER_SIZE = 1024  # Ukuran buffer data

# Membuat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Menentukan nama klien
client_name = input("Masukkan nama Anda: ")

# Mengirimkan nama klien ke server
client_socket.sendto(client_name.encode("utf-8"), (HOST, PORT))

# Loop utama klien
while True:
    # Menerima pesan dari server
    data, address = client_socket.recvfrom(BUFFER_SIZE)
    message = data.decode("utf-8")

    # Menampilkan pesan dan meminta jawaban klien
    print(f"\n{message}")
    client_response = input("Masukkan jawaban Anda: ")

    # Mengirimkan jawaban klien ke server
    client_socket.sendto(client_response.encode("utf-8"), address)

    # Menerima feedback dari server
    data, address = client_socket.recvfrom(BUFFER_SIZE)
    feedback_message = data.decode("utf-8")
    print(feedback_message)
