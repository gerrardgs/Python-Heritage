import socket
import time

def english_to_indonesian_color(english_color):
    color_mapping = {
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "purple": "ungu",
        "orange": "oranye"
    }
    return color_mapping.get(english_color.lower(), "tidak dikenali")

def main():
    server_ip = "127.0.0.1"  # Ganti dengan alamat IP server
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        try:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))
            color, server_address = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Warna yang diterima: {color}")

            # Klien memiliki waktu 5 detik untuk merespons
            response = input("Masukkan warna dalam bahasa Indonesia: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban benar! Nilai feedback: 100")
            else:
                print("Jawaban salah. Nilai feedback: 0")

            time.sleep(10)  # Tunggu 10 detik sebelum mengirim permintaan lagi

        except KeyboardInterrupt:
            print("\nKlien berhenti.")
            break

    client_socket.close()

if __name__ == "__main__":
    main()
