# TUGAS BESAR ULANGAN TENGAH SEMESTER - PEMROGRAMAN JARINGAN 2024
- NAMA: Gerrard Sebastian
- KELAS: IF-02-01
- NIM: 1203220018

<br>

# SOAL
![image](https://github.com/gerrardgs/Python-Heritage/assets/114888829/33032c93-3cee-4882-9286-3038d47270bd)

<br>

# JAWABAN
## SERVER PROGRAM:
```python
import socket
import random
import time

def generate_random_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    return random.choice(colors)

def main():
    server_ip = "127.0.0.1"  # Ganti dengan alamat IP server
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print(f"Server berjalan di {server_ip}:{server_port}")

    connected_clients = set()

    while True:
        try:
            data, client_address = server_socket.recvfrom(1024)
            data = data.decode("utf-8")

            if client_address not in connected_clients:
                connected_clients.add(client_address)
                print(f"Klien terhubung dari {client_address}")

            if data == "request_color":
                color = generate_random_color()
                server_socket.sendto(color.encode("utf-8"), client_address)
                print(f"Kirim warna {color} ke {client_address}")

        except KeyboardInterrupt:
            print("\nServer berhenti.")
            break

    server_socket.close()

if __name__ == "__main__":
    main()

```
### Penjelasan:
Berikut Merupakan penjelasan singkat mengenai program Python "SERVER" di atas:
- Program dimulai dengan mengimpor modul `socket`, `random`, dan `time`.
- Lalu Fungsi utama program adalah `main()`.
- Lalu IP server diatur sebagai `"127.0.0.1"` (localhost), dan port server diatur sebagai `12345`.
- Lalu Socket server dibuat menggunakan `socket.AF_INET` untuk alamat IPv4, dan `socket.SOCK_DGRAM` untuk protokol UDP.
- Lalu Server dihubungkan ke alamat IP dan port yang telah ditentukan.
- Lalu Set `connected_clients` yang digunakan untuk melacak klien yang terhubung.
- Lalu Selama program berjalan, maka server akan menerima data dari klien dan memprosesnya.
- Lalu Jika data yang diterima adalah `"request_color"`, maka server menghasilkan warna acak menggunakan fungsi `generate_random_color()`.
- Lalu Warna dikirim kembali ke klien yang meminta.
- Terakhir Jika pengguna menekan tombol `Ctrl+C`, program akan berhenti dan socket server ditutup.

<br>

## CLIENT PROGRAM:
```python
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

```
### Penjelasan:
Berikut adalah penjelasan singkat mengenai program Python "CLIENT" di atas:
- Program dimulai dengan mengimpor modul `socket` dan `time`.
- Lalu Fungsi utama program adalah `main()`.
- Lalu IP server diatur sebagai `"127.0.0.1"` (localhost), dan port server diatur sebagai `12345`.
- Lalu Socket klien dibuat menggunakan `socket.AF_INET` untuk alamat IPv4, dan `socket.SOCK_DGRAM` untuk protokol UDP.
- Lalu Klien mengirim permintaan `"request_color"` ke server.
- Lalu Klien menerima warna dari server, dan mendekode data yang diterima.
- Lalu Klien menampilkan warna yang diterima dari server.
- Lalu Pengguna diminta memasukkan warna dalam bahasa Indonesia.
- Lalu Klien membandingkan jawaban pengguna dengan terjemahan warna Inggris ke bahasa Indonesia.
- Terakhir Jika pengguna menekan `Ctrl+C`, maka program akan berhenti dan socket klien ditutup.

<br>

## HOW THE PROGRAM WORKS?
### Python Server Program:
- Program dimulai dengan menginisialisasi alamat IP server (`server_ip`), dan port server (`server_port`).
- Lalu Socket server dibuat menggunakan `socket.AF_INET` untuk alamat IPv4, dan `socket.SOCK_DGRAM` untuk protokol UDP.
- Lalu Server diikat ke alamat IP dan port yang telah ditentukan menggunakan `server_socket.bind((server_ip, server_port))`.
- Lalu Set `connected_clients` digunakan untuk melacak alamat klien yang terhubung.
- Lalu Selama program berjalan, server menerima data dari klien dan memprosesnya.
- Lalu Jika data yang diterima adalah `"request_color"`, maka server akan memanggil fungsi `generate_random_color()` untuk menghasilkan warna acak.
- Lalu Warna dikirim kembali ke klien yang meminta menggunakan `server_socket.sendto(color.encode("utf-8"), client_address)`.
- Terakhir Jika pengguna menekan `Ctrl+C`, maka program akan berhenti dan socket server ditutup menggunakan `server_socket.close()`.

<br>

### Python Client Program:
- Program dimulai dengan menginisialisasi alamat IP server (`server_ip`) dan port server (`server_port`).
- Lalu Socket klien dibuat menggunakan `socket.AF_INET` untuk alamat IPv4, dan `socket.SOCK_DGRAM` untuk protokol UDP.
- Lalu Klien mengirim permintaan `"request_color"` ke server menggunakan `client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))`.
- Lalu Klien menerima warna dari server dan mendekode data yang diterima menggunakan `color, server_address = client_socket.recvfrom(1024)`.
- Lalu Klien menampilkan warna yang diterima dari server.
- Lalu Pengguna diminta memasukkan warna dalam bahasa Indonesia.
- Lalu Klien membandingkan jawaban pengguna dengan terjemahan warna Inggris ke bahasa Indonesia menggunakan fungsi `english_to_indonesian_color()`.
- Terakhir Jika pengguna menekan `Ctrl+C`, maka program akan berhenti dan socket klien ditutup menggunakan `client_socket.close()`.

<br>

## EXAMPLES OF PROGRAM USE (DOCUMENTATIONS)
