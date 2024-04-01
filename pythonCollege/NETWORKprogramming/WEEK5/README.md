# LAPORAN PRAKTIKUM TUGAS TEORI JARKOM
<br>

<h3>NAMA: Gerrard Sebastian</h3>
<h3>NIM: 1203220018</h3>
<h3>KELAS: IF-02-01</h3>
<br>

# SOAL
1. Buat sebuah program file transfer protocol menggunakan socket programming dengan beberapa perintah dari client seperti berikut:
- ls : ketika client menginputkan command tersebut, maka server akan memberikan daftar file dan folder 
- rm {nama file} : ketika client menginputkan command tersebut, maka server akan menghapus file dengan acuan nama file yang diberikan pada parameter pertama
- download {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan file dengan acuan nama file yang diberikan pada parameter pertama
- upload {nama file} : ketika client menginputkan command tersebut, maka server akan menerima dan menyimpan file dengan acuan nama file yang diberikan pada parameter pertama
- size {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan informasi file dalam satuan MB (Mega bytes) dengan acuan nama file yang diberikan pada parameter pertama
- byebye : ketika client menginputkan command tersebut, maka hubungan socket client akan diputus
- connme : ketika client menginputkan command tersebut, maka hubungan socket client akan terhubung.
<br>

# JAWABAN
<h3>LINK GITHUB: https://bit.ly/TgsTeoriJarkom2 </h3>

<h3><strong>Disclaimer: Program Dibuat Menggunakan Bahasa Python</strong></h3>

### 1.	Server Program
```python
import socket
import os
import struct
import sys
import time

# Initialize socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)  # Change to appropriate address and port

# Bind socket to server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for connection from the client...")

# Accept connection from client
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

BUFFER_SIZE = 1024

def ls():
    file_list = os.listdir('.')
    response = "\n".join(file_list)
    client_socket.send(response.encode())

def rm(filename):
    if os.path.exists(filename):
        os.remove(filename)
        client_socket.send("File berhasil dihapus.".encode())
    else:
        client_socket.send("File tidak ditemukan.".encode())

def download(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            while True:
                data = file.read(BUFFER_SIZE)
                if not data:
                    break
                client_socket.send(data)
    else:
        client_socket.send("File tidak ditemukan.".encode())

def upload(filename):
    data = client_socket.recv(BUFFER_SIZE)
    with open(filename, 'wb') as file:
        file.write(data)
    client_socket.send("File berhasil disimpan.".encode())

def size(filename):
    if os.path.exists(filename):
        file_size = os.path.getsize(filename) / (1024 * 1024)  # Convert to MB
        client_socket.send(f"Ukuran file {filename}: {file_size:.2f} MB".encode())
    else:
        client_socket.send("File tidak ditemukan.".encode())

def byebye():
    client_socket.send("Terima kasih! Koneksi akan diputus.".encode())
    client_socket.close()
    server_socket.close()
    sys.exit()

def connme():
    client_socket.send("Koneksi tetap terhubung.".encode())

while True:
    try:
        # Receive command from client
        command = client_socket.recv(1024).decode()
        if not command:
            break

        # Process command
        if command == "ls":
            ls()
        elif command.startswith("rm "):
            rm(command.split()[1])
        elif command.startswith("download "):
            filename = command.split()[1]
            download(filename)
        elif command.startswith("upload "):
            filename = command.split()[1]
            upload(filename)
        elif command.startswith("size "):
            filename = command.split()[1]
            size(filename)
        elif command == "byebye":
            byebye()
        elif command == "connme":
            connme()
        else:
            client_socket.send("Perintah tidak valid.".encode())
    except Exception as e:
        print(f"Error: {e}")
        break
```
<br>

### Penjelasan:

Import library (Program ini menggunakan beberapa library bawaan Python untuk menjalankan fungsinya. Library tersebut adalah):
- socket: Digunakan untuk membuat koneksi jaringan (socket) antara server dan client.
- os: Digunakan untuk berinteraksi dengan sistem operasi, seperti menampilkan daftar file dan menghapus file.
- struct: (Tidak digunakan pada program ini) Digunakan untuk mengemas dan membongkar struktur data biner.
- sys: Digunakan untuk fungsi terkait sistem, seperti keluar dari program.
- time: (Tidak digunakan pada program ini) Digunakan untuk fungsi terkait waktu.

<br>

Variable dan Inisialisasi:
- server_socket: Variabel ini menyimpan socket server yang digunakan untuk mendengarkan koneksi dari client.
- server_address: Variabel ini berisi alamat dan port server, dalam contoh ini localhost (alamat lokal) dan port 12345. dapat diubah ke alamat dan port yang sesuai dengan kebutuhan.
- BUFFER_SIZE: Variabel ini menentukan ukuran buffer yang digunakan untuk mengirim dan menerima data antar client dan server. nilainya adalah 1024 byte.

<br>

Fungsi-fungsi pada Program (Program ini memiliki beberapa fungsi yang menangani berbagai perintah dari client):
- ls(): Fungsi ini menampilkan daftar file dan folder yang ada di direktori server. Daftar file tersebut dikirimkan ke client.
- rm(filename): Fungsi ini menghapus file yang ditentukan oleh filename dari server. Jika file berhasil dihapus, pesan konfirmasi dikirim ke client. Sebaliknya, pesan pemberitahuan file tidak ditemukan dikirim ke client.
- download(filename): Fungsi ini mengirimkan file yang ditentukan oleh filename dari server ke client. Isi file dibaca per BUFFER_SIZE byte dan dikirimkan ke client secara bertahap. Jika file tidak ditemukan, pesan pemberitahuan dikirim ke client.
- upload(filename): Fungsi ini menerima file yang dikirimkan oleh client dan menyimpannya di server dengan nama filename. Data file diterima per BUFFER_SIZE byte dan ditulis ke file baru di server. Setelah selesai, pesan konfirmasi dikirim ke client.
- size(filename): Fungsi ini menghitung ukuran file yang ditentukan oleh filename di server. Ukuran file dikonversi ke Megabyte (MB) dan kemudian dikirimkan ke client. Jika file tidak ditemukan, pesan pemberitahuan dikirim ke client.
- byebye(): Fungsi ini menutup koneksi antara server dan client, serta menutup socket server. Program server kemudian berhenti.
- connme(): Fungsi ini mengirim pesan ke client bahwa koneksi masih terhubung dan server siap menerima perintah selanjutnya.
Looping dan Penanganan Perintah

<br>

Program menggunakan loop while True untuk terus menerus menerima perintah dari client. Didalam loop:
- Program menerima perintah dari client menggunakan client_socket.recv(1024).decode().
- Perintah tersebut kemudian diproses menggunakan pernyataan if dan elif untuk menentukan fungsi mana yang akan dipanggil sesuai dengan perintah.
- Jika perintah valid, fungsi terkait akan dipanggil untuk melakukan aksi yang sesuai.
- Jika perintah tidak valid, pesan pemberitahuan dikirim ke client.
- Loop akan terus berjalan sampai client mengirimkan perintah byebye untuk memutuskan koneksi.

<br>

### 2.	Client Program
```python
import socket

# Initialize socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)  # Change to appropriate address and port

# Connect to server
client_socket.connect(server_address)
print(f"Connected to server {server_address}")

def send_command(command):
    # Send command to server
    client_socket.send(command.encode())

    # Process response from server
    response = client_socket.recv(1024).decode()
    print(response)

while True:
    try:
        # Input command from user
        command = input("Masukkan perintah (ls/rm/download/upload/size/byebye/connme): ")

        # Send command to server and receive response
        send_command(command)

        if command == "byebye":
            break
    except Exception as e:
        print(f"Error: {e}")
        break

# Close socket
client_socket.close()
```
<br>

### Penjelasan:

Import library (Program ini hanya menggunakan library socket dari Python. Library ini digunakan untuk membuat koneksi jaringan (socket) antara client dan server).

<br>

Variable dan Inisialisasi:
- client_socket: Variabel ini menyimpan socket client yang digunakan untuk terhubung ke server.
- server_address: Variabel ini berisi alamat dan port server, dalam contoh ini localhost (alamat lokal) dan port 12345. dapat diubah ke alamat dan port server yang ingin dihubungi.

<br>

Fungsi send_command(command):
- Fungsi ini digunakan untuk mengirim perintah ke server dan menerima respon dari server
- Perintah (command) yang diberikan user diubah menjadi format bytecode menggunakan command.encode().
- Perintah tersebut kemudian dikirim ke server menggunakan client_socket.send().
- Fungsi ini kemudian menunggu respon dari server menggunakan client_socket.recv(1024).decode(). Respon tersebut berupa pesan berbentuk string yang kemudian ditampilkan ke user menggunakan print().

<br>

Looping dan Input Perintah (Program menggunakan loop while True untuk terus menerus meminta user memasukkan perintah. Didalam loop):
- Program meminta user untuk memasukkan perintah menggunakan input(). 
- Perintah yang valid adalah ls, rm, download, upload, size, byebye, dan connme.
- Perintah tersebut kemudian dikirim ke server beserta proses penerimaannya ditangani oleh fungsi send_command(command).
- Jika perintah yang dimasukkan adalah byebye, loop akan berhenti dan koneksi ke server akan ditutup.
- Program menggunakan blok try dan except untuk menangani kemungkinan error yang terjadi saat komunikasi dengan server.

<br>

### Konklusi:

Program server dan client merupakan dua program yang saling terkait dan bekerja sama untuk menyediakan layanan transfer data dan manajemen file. Server bertindak sebagai penyedia sumber daya dan menerima koneksi dari client, sedangkan client bertindak sebagai pengguna yang berinteraksi dengan server dan mengirimkan perintah.

Kedua program ini memiliki fungsi dan fitur yang berbeda. Server dapat melakukan berbagai operasi seperti menampilkan daftar file, menghapus file, mengirim dan menerima file, serta mengecek ukuran file. Sedangkan client dapat memasukkan perintah, mengirim perintah ke server, menerima respon dari server, dan menutup koneksi dengan server.

Program server dan client memiliki beberapa keuntungan, seperti memudahkan transfer file dan sumber daya, memungkinkan akses terpusat ke data, serta meningkatkan keamanan dan kontrol akses. Namun, program ini juga memiliki kekurangan, seperti membutuhkan koneksi jaringan yang stabil, server dapat menjadi target serangan cyber, dan konfigurasi server bisa rumit.

Program server dan client dapat digunakan dalam berbagai aplikasi, seperti penyimpanan cloud, berbagi file antar perangkat, kolaborasi tim, backup data, dan remote access. Dengan memahami cara kerja program-program ini, dapat dimanfaatkan dengan lebih efektif untuk berbagai kebutuhan.

Kesimpulannya, program server dan client merupakan alat yang penting untuk transfer data dan manajemen file. Dengan memahami cara kerja dan fitur-fiturnya, dapat digunakan untuk berbagai kebutuhan dan meningkatkan efisiensi dan kolaborasi.

<br>

# CARA MENGGUNAKAN TIAP FITUR YANG TERSEDIA (7 FITUR)


<br>

### OUTPUT PROGRAM
#### SERVER:
![server](https://github.com/gerrardgs/Python-Heritage/assets/114888829/aabf8202-d953-41f9-98ad-0bd994dcceb4)

<br>

#### CLIENT:
![5 features exclude down and up](https://github.com/gerrardgs/Python-Heritage/assets/114888829/27b84b35-f3bc-4494-8afb-7be793d3dccd)

<br>

![download](https://github.com/gerrardgs/Python-Heritage/assets/114888829/15bc7adb-2d45-4178-861a-3b94746c908f)

<br>

![upload](https://github.com/gerrardgs/Python-Heritage/assets/114888829/a5b03fbc-751a-4e39-9aa1-4b6370bd9099)
