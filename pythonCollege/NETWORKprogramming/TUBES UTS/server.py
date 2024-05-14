import socket
import random
import time

# Konfigurasi server
HOST = "localhost"  # Alamat IP server
PORT = 65535  # Port server
BUFFER_SIZE = 1024  # Ukuran buffer data

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

# Daftar kata warna bahasa Inggris
english_colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# Loop utama server
while True:
    # Menunggu pesan dari klien
    data, address = server_socket.recvfrom(BUFFER_SIZE)

    # Menerima nama klien
    client_name = data.decode("utf-8").strip()

    # Memilih kata warna acak
    english_color = random.choice(english_colors)

    # Mengubah kata warna ke bahasa Indonesia
    indonesian_color = {
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "purple": "ungu",
        "orange": "oranye"
    }[english_color]

    # Mengirim kata warna ke klien
    message = f"Tebak warna ini: {english_color}"
    server_socket.sendto(message.encode("utf-8"), address)

    # Menunggu jawaban klien dalam 5 detik
    start_time = time.time()
    while time.time() < start_time + 5:
        try:
            response, address = server_socket.recvfrom(BUFFER_SIZE)
            client_response = response.decode("utf-8").strip()
            break
        except socket.timeout:
            pass

    # Menghitung waktu respons klien
    response_time = time.time() - start_time

    # Mengecek jawaban klien
    if client_response.lower() == indonesian_color:
        feedback = 100
    else:
        feedback = 0

    # Mengirim feedback ke klien
    feedback_message = f"Feedback: {feedback} (Waktu respons: {response_time:.2f} detik)"
    server_socket.sendto(feedback_message.encode("utf-8"), address)

    # Mencetak informasi di server
    print(f"[Klien {client_name}] Jawaban: {client_response}, Feedback: {feedback}")
