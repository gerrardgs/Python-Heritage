# Server (server.py)
import socket

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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

            # Cek apakah input merupakan bilangan prima
            try:
                number = int(message)
                if is_prime(number):
                    response = "Bilangan prima"
                else:
                    response = "Bukan bilangan prima"
            except ValueError:
                response = "Input bukan angka"

            # Kirim balasan ke klien
            server_socket.sendto(response.encode('utf-8'), client_address)
            print(f"Pesan dari klien: {message}")
            print(f"Balasan ke klien: {response}")
        except KeyboardInterrupt:
            print("\nServer berhenti.")
            break

if __name__ == "__main__":
    main()
