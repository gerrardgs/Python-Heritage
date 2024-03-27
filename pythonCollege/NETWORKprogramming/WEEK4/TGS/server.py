# Server (server.py)
import socket

def main():
    # Inisialisasi socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('0.0.0.0', 12345)  # Ganti dengan alamat dan port yang sesuai

    # Bind socket ke alamat dan port
    server_socket.bind(server_address)
    print(f"Server berjalan di {server_address[0]}:{server_address[1]}")

    while True:
        try:
            # Terima pesan dari klien
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode('utf-8')

            # Hitung jumlah karakter pada pesan
            character_count = len(message)

            # Kirim balasan ke klien
            server_socket.sendto(str(character_count).encode('utf-8'), client_address)
            print(f"Pesan dari klien: {message}")
            print(f"Jumlah karakter: {character_count}")
        except KeyboardInterrupt:
            print("\nServer berhenti.")
            break

if __name__ == "__main__":
    main()
