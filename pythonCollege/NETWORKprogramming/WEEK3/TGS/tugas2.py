# CLIENT

import socket

# Deklarasi variabel
HOST = "localhost"
PORT = 12345

# Membuat socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Menghubungkan ke server
    client_socket.connect((HOST, PORT))
    print(f"Terhubung ke server di {HOST}:{PORT}")

    # Meminta pesan dari pengguna
    pesan = input("Masukkan pesan: ")

    # Mengirim pesan ke server
    client_socket.send(pesan.encode())

    # Menerima pesan balasan dari server
    data = client_socket.recv(1024)
    balasan = data.decode()

    # Menampilkan pesan balasan
    print(f"Pesan balasan: {balasan}")

# Menutup socket
client_socket.close()
