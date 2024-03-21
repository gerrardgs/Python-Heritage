# SERVER

import socket

# Deklarasi variabel
HOST = "localhost"
PORT = 12345

# Membuat socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind socket ke alamat dan port
    server_socket.bind((HOST, PORT))
    # Mendengarkan koneksi dari client
    server_socket.listen()
    print(f"Server sedang berjalan di {HOST}:{PORT}")

    # Menunggu koneksi dari client
    client_socket, client_address = server_socket.accept()
    print(f"Klien terhubung dari {client_address}")

    while True:
        # Menerima pesan dari client
        data = client_socket.recv(1024)
        if not data:
            break
        
        # Menghitung jumlah karakter pada pesan
        jumlah_karakter = len(data.decode())

        # Mengirim pesan balasan berisi jumlah karakter
        balasan = f"Jumlah karakter: {jumlah_karakter}"
        client_socket.send(balasan.encode())

# Menutup socket
client_socket.close()
server_socket.close()
