# Server (server.py)
import socket

def is_palindrome(s):
    # Check if the length of the string is 0 or 1
    if len(s) < 2:
        return True
    # Compare the first and last characters
    if s != s[::-1]:
        return False
    # Recursively check the rest of the string
    return is_palindrome(s[1:-1])

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

            # Cek apakah input merupakan palindrom
            if is_palindrome(message.lower().replace(' ', '')):
                response = "Input merupakan palindrom"
            else:
                response = "Input bukan palindrom"

            # Kirim balasan ke klien
            server_socket.sendto(response.encode('utf-8'), client_address)
            print(f"Pesan dari klien: {message}")
            print(f"Balasan ke klien: {response}")
        except KeyboardInterrupt:
            print("\nServer berhenti.")
            break

if __name__ == "__main__":
    main()
