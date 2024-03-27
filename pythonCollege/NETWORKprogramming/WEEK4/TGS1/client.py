# Klien (client.py)
import socket

def main():
    # Inisialisasi socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 12345)  # Ganti dengan alamat dan port server

    while True:
        try:
            # Input dari pengguna
            message = input("Masukkan angka: ")

            # Kirim pesan ke server
            client_socket.sendto(message.encode('utf-8'), server_address)

            # Terima balasan dari server
            response, _ = client_socket.recvfrom(1024)
            print(f"Balasan dari server: {response.decode('utf-8')}")
        except KeyboardInterrupt:
            print("\nKlien berhenti.")
            break

if __name__ == "__main__":
    main()
