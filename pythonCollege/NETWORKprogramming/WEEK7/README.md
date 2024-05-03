# TUGAS "TEORI" LANJUTAN DARI WEEK 5: https://bit.ly/TgsTeoriJarkom2
- NAMA        : GERRARD SEBASTIAN
- KELAS       : 1203220018
- PRODI       : INFORMATIKA
- ANGKATAN    : 2022
- MATKUL      : PEMROGRAMAN JARINGAN ~ TEORI
- PERIHAL     : MENGUMPULKAN TUGAS 3 (LANJUTAN DARI TUGAS 2 DENGAN TAMBAHAN SOAL)

<br>

## DISCLAIMER !!!
Program Masih Sangat Sering Mengalami Bug, Sehingga Program Tidak Dapat Didokumentasikan Sepenuhnya, Jadi Tugas ini akan ditekankan kembali di bagian penjelasan (yang seharusnya ditampilkan di dokumentasi tetapi karena adanya bug, maka akan dijelaskan saja untuk implementasi fitur-fiturnya yang ada.

<br>

# SOAL TAMBAHAN
![Screenshot 2024-05-02 202749](https://github.com/gerrardgs/Python-Heritage/assets/114888829/56b55772-3c0d-45dd-9d88-6ef6a127455e)

<br>

# JAWABAN
## Server Program:
```python
import socket
import sys
import time
import os
import struct

print("\nMenunggu koneksi client...\n")

TCP_IP = "127.0.0.1"
TCP_PORT = 1456
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

print("\n Koneksi terhubung dengan alamat : {}".format(addr))

# buat fungsi upload {nama file} : ketika client menginputkan command tersebut, maka server akan menerima dan menyimpan file dengan acuan nama file yang diberikan pada parameter pertama
def upld():
    conn.send(b"1")
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_length).decode()

    # Check if the file already exists
    original_file_name = file_name
    counter = 1
    while os.path.exists(file_name):
        # If the file exists, append a number to the file name
        file_name = f"{os.path.splitext(original_file_name)[0]}_{counter}{os.path.splitext(original_file_name)[1]}"
        counter += 1

    conn.send(b"1")
    file_size = struct.unpack("i", conn.recv(4))[0]
    start_time = time.time()
    print(f"Menerima file: {file_name}")
    content = open(file_name, "wb")
    l = conn.recv(BUFFER_SIZE)
    while l:
        content.write(l)
        l = conn.recv(BUFFER_SIZE)
    content.close()
    conn.send(struct.pack("f", time.time() - start_time))
    conn.send(struct.pack("i", file_size))
    print("File berhasil diterima")
    return

# buat fungsi list_files : ketika client menginputkan command tersebut, maka server akan memberikan list file yang ada pada server
def list_files():
    print("Listing files...")
    listing = os.listdir(os.getcwd())
    conn.send(struct.pack("i", len(listing)))
    total_directory_size = 0
    for i in listing:
        conn.send(struct.pack("i", sys.getsizeof(i)))
        conn.send(i.encode())
        conn.send(struct.pack("i", os.path.getsize(i)))
        total_directory_size += os.path.getsize(i)
        conn.recv(BUFFER_SIZE)
    conn.send(struct.pack("i", total_directory_size))
    conn.recv(BUFFER_SIZE)
    print("File berhasil dilisting")
    return

# buat fungsi download {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan file dengan acuan nama file yang diberikan pada parameter pertama
def dwld():
    conn.send(b"1")
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_length).decode()
    if os.path.isfile(file_name):
        conn.send(struct.pack("i", os.path.getsize(file_name)))
    else:
        print("Nama file tidak benar")
        conn.send(struct.pack("i", -1))
        return
    conn.recv(BUFFER_SIZE)
    start_time = time.time()
    print("Mengirim file...")
    content = open(file_name, "rb")
    l = content.read(BUFFER_SIZE)
    while l:
        conn.send(l)
        l = content.read(BUFFER_SIZE)
    content.close()
    conn.recv(BUFFER_SIZE)
    conn.send(struct.pack("f", time.time() - start_time))
    print("File berhasil dikirim")
    return

# buat fungsi delf : ketika client menginputkan command tersebut, maka server akan menghapus file dengan acuan nama file yang diberikan pada parameter pertama
def delf():
    conn.send(b"1")
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_length).decode()
    if os.path.isfile(file_name):
        conn.send(struct.pack("i", 1))
    else:
        conn.send(struct.pack("i", -1))
    confirm_delete = conn.recv(BUFFER_SIZE).decode()
    if confirm_delete == "Y":
        try:
            os.remove(file_name)
            conn.send(struct.pack("i", 1))
        except:
            print("Gagal menghapus {}".format(file_name))
            conn.send(struct.pack("i", -1))
    else:
        print("Fitur delete ditinggalkan klien!")
        return

# buat fungsi size {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan informasi file dalam satuan MB (Mega bytes) dengan acuan nama file yang diberikan pada parameter pertama
def get_file_size():
    conn.send(b"1")
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_length).decode()
    if os.path.isfile(file_name):
        conn.send(struct.pack("i", os.path.getsize(file_name)))
    else:
        conn.send(struct.pack("i", -1))
    return

# buat fungsi quit : ketika client menginputkan command byebye, maka server akan menutup koneksi dengan client
def quit():
    conn.send(b"1")
    conn.close()
    s.close()
    os.execl(sys.executable, sys.executable, *sys.argv)

while True:
    print("\n\nMenunggu Instruksi...")
    data = conn.recv(BUFFER_SIZE).decode()
    print("\nInstruksi Diterima: {}".format(data))
    if data == "upload":
        upld()
    elif data == "ls":
        list_files()
    elif data == "download":
        dwld()
    elif data == "rm":
        delf()
    elif data == "size":
        get_file_size()
    elif data == "byebye":
        quit()
    data = None

```
### Penjelasan:
Program Python ini merupakan program server yang berjalan pada komputer dan dapat diakses oleh client (program lain) melalui jaringan. Server ini dapat menerima instruksi dari client berupa perintah upload, list_files, download, delete (disingkat delf), size, dan quit. 

Ketika client memberikan instruksi upload, server akan menerima dan menyimpan file yang dikirimkan client. Instruksi list_files akan membuat server mengirimkan daftar file yang ada di server beserta ukurannya kepada client. Perintah download digunakan client untuk meminta file tertentu dari server. Server akan mengirimkan file tersebut jika tersedia. Instruksi delf digunakan untuk menghapus file tertentu di server. Namun, penghapusan hanya akan dilakukan jika client mengkonfirmasi persetujuan. Perintah size akan meminta server untuk memberikan informasi ukuran file tertentu dalam satuan Megabyte (MB). Terakhir, instruksi quit akan memutuskan koneksi antara server dan client, serta mengakhiri program server. 

<br>

## Client Program:
```python
import socket
import sys
import os
import struct
import time

TCP_IP = "127.0.0.1"
TCP_PORT = 1456
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# buat fungsi connme : ketika client menginputkan command tersebut, maka client akan terhubung dengan server
def connme():
    # melakukan percobaan koneksi ke server
    try:
        # jika berhasil, maka akan menampilkan pesan "Koneksi berhasil!"
        s.connect((TCP_IP, TCP_PORT))
        print("Terhubung ke Server")
    except:
        # jika gagal, maka akan menampilkan pesan "Koneksi gagal! Pastikan server telah dijalankan dan port yang digunakan benar"
        print("Menghubungkan Gagal! Pastikan server berjalan dan konfigurasi port benar!")


# buat fungsi upld(parameter) : ketika client menginputkan command tersebut, maka server akan menerima dan menyimpan file dengan acuan nama file yang diberikan pada parameter pertama
def upld(file_name):
    try:
        s.send(b"upload")
    except:
        print("Tidak dapat membuat permintaan server. Pastikan Koneksi Telah Terhubung (HINT 2).")
        return
    try:
        # mengirimkan pesan ke server bahwa client akan mengirimkan file
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = os.path.getsize(file_name)
        s.send(struct.pack("i", file_size))
        start_time = time.time()
        print("Mengirim File...")
        content = open(file_name, "rb")
        l = content.read(BUFFER_SIZE)
        while l:
            s.send(l)
            l = content.read(BUFFER_SIZE)
        content.close()
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("f", time.time() - start_time))
        print("File Berhasil Dikirim")
        return
    except:
        print("File Tidak Dapat Dikirim")
        return

# buat fungsi list_files : ketika client menginputkan command tersebut, maka server akan memberikan list file yang ada pada server
def list_files():
    try:
        s.send(b"ls")
    except:
        print("Tidak dapat membuat permintaan server. Pastikan Koneksi Telah Terhubung (HINT 2).")
        return
    try:
        # program untuk menerima pesan dari server berupa jumlah file yang ada pada server
        number_of_files = struct.unpack("i", s.recv(4))[0]
        for i in range(int(number_of_files)):
            file_name_size = struct.unpack("i", s.recv(4))[0]
            file_name = s.recv(file_name_size).decode()
            file_size = struct.unpack("i", s.recv(4))[0]
            print("\t{} - {}b".format(file_name, file_size))
            s.send(b"1")
        total_directory_size = struct.unpack("i", s.recv(4))[0]
        print("Total ukuran direktori: {}b".format(total_directory_size))
    except:
        print("Tidak dapat memberikan list")
        return
    try:
        s.send(b"1")
        return
    except:
        print("Tidak bisa mendapatkan konfigurasi final dari server")
        return

# buat fungsi download {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan file dengan acuan nama file yang diberikan pada parameter pertama
def dwld(file_name):
    try:
        s.send(b"download")
    except:
        print("Tidak dapat membuat permintaan server. Pastikan Koneksi Telah Terhubung (HINT 2).")
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = struct.unpack("i", s.recv(4))[0]
        if file_size == -1:
            print("File tidak benar. Pastikan nama file terinput dengan benar")
            return
    except:
        print("Gagal mengecek File")
    try:
        s.send(b"1")
        output_file = open(file_name, "wb")
        bytes_received = 0
        print("\nMengunduh...")
        while bytes_received < file_size:
            l = s.recv(BUFFER_SIZE)
            output_file.write(l)
            bytes_received += BUFFER_SIZE
        output_file.close()
        print("Unduhan berjalan dengan sukses {}".format(file_name))
        s.send(b"1")
        print("Time elapsed: {}s\nFile size: {}b".format(file_size))
    except:
        print("Gagal mengunduh file")
        return
    return

# buat fungsi delf(parameter) : ketika client menginputkan command tersebut, maka server akan menghapus file dengan acuan nama file yang diberikan pada parameter pertama
def delf(file_name):
    try:
        s.send(b"rm")
        s.recv(BUFFER_SIZE)
    except:
        print("Tidak dapat membuat permintaan server. Pastikan Koneksi Telah Terhubung (HINT 2).")
        return
    try:
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
    except:
        print("Tidak dapat mengirimkan detail File")
        return
    try:
        file_exists = struct.unpack("i", s.recv(4))[0]
        if file_exists == -1:
            print("File yang dicari tidak ada dalam server")
            return
    except:
        print("Tidak dapat menentukan keberadaan file")
        return
    try:
        confirm_delete = input("Apakah anda yakin ingin menghapus file {}? (Y/N)\n".format(file_name)).upper()
        while confirm_delete != "Y" and confirm_delete != "N" and confirm_delete != "YES" and confirm_delete != "NO":
            print("Perintah salah! coba lagi.")
            confirm_delete = input("Apakah anda yakin ingin menghapus file {}? (Y/N)\n".format(file_name)).upper()
    except:
        print("Tidak dapat mengonfirmasi status penghapusan")
        return
    try:
        if confirm_delete == "Y" or confirm_delete == "YES":
            s.send(b"Y")
            delete_status = struct.unpack("i", s.recv(4))[0]
            if delete_status == 1:
                print("File berhasil dihapus")
                return
            else:
                print("File gagal dihapus")
                return
        else:
            s.send(b"N")
            print("Pengguna meninggalkan fitur")
            return
    except:
        print("Tidak dapat menghapus file")
        return

# buat fungsi size {nama file} : ketika client menginputkan command tersebut, maka server akan memberikan informasi file dalam satuan MB (Mega bytes) dengan acuan nama file yang diberikan pada parameter pertama
def get_file_size(file_name):
    try:
        s.send(b"size")
    except:
        print("Tidak dapat membuat permintaan server. Pastikan Koneksi Telah Terhubung (HINT 2).")
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = struct.unpack("i", s.recv(4))[0]
        if file_size == -1:
            print("File tidak benar. Pastikan nama file terinput dengan benar")
            return
    except:
        print("Gagal mengecek program")
    try:
        s.send(b"1")
        print("File size: {} MB".format(file_size / 1024 / 1024))
        return
    except:
        print("Tidak bisa mendapatkan konfigurasi final dari server")
        return

def quit():
    s.send(b"byebye")
    s.recv(BUFFER_SIZE)
    s.close()
    print("Server connection ended")
    return

print("HINT 1: Download and Upload are Using <file_path>")
print("HINT 2: connme first before run another command")

while True:
    prompt = input("\nMasukkan Command: ls/rm/size/download/upload/byebye/connme: ")
    if prompt[:6].lower() == "connme":
        connme()
    elif prompt[:6].lower() == "upload":
        upld(prompt[7:])
    elif prompt.lower() == "ls":
        list_files()
    elif prompt[:8].lower() == "download":
        dwld(prompt[9:])
    elif prompt[:2].lower() == "rm":
        delf(prompt[3:])
    elif prompt[:4].lower() == "size":
        get_file_size(prompt[5:])
    elif prompt.lower() == "byebye":
        quit()
        break
    else:
        print("Perintah tidak dikenali, silahkan coba lagi")
```
### Penjelasan:
Menghubungkan ke server: Client dapat terhubung ke server menggunakan perintah `connme`. Perintah ini akan mencoba melakukan koneksi ke server dengan alamat IP dan port yang ditentukan. Jika koneksi berhasil, client akan menampilkan pesan "Terhubung ke Server". Menampilkan daftar file: Client dapat melihat daftar file yang ada di server menggunakan perintah `ls`. Perintah ini akan mengirimkan permintaan ke server, dan server akan merespon dengan daftar nama file, ukuran file, dan total ukuran direktori. Mengunggah file: Client dapat mengunggah file ke server menggunakan perintah `upload` diikuti dengan nama file. Perintah ini akan mengirimkan file ke server, dan server akan menyimpannya di direktori yang ditentukan. Mengunduh file: Client dapat mengunduh file dari server menggunakan perintah `download` diikuti dengan nama file. Perintah ini akan meminta file dari server, dan server akan mengirimkan file tersebut ke client. Menghapus file: Client dapat menghapus file dari server menggunakan perintah `rm` diikuti dengan nama file. Perintah ini akan mengirimkan permintaan ke server untuk menghapus file, dan server akan menghapusnya jika file tersebut ada. Melihat ukuran file: Client dapat melihat ukuran file di server menggunakan perintah `size` diikuti dengan nama file. Perintah ini akan mengirimkan permintaan ke server untuk mendapatkan ukuran file, dan server akan merespon dengan informasi ukuran file dalam satuan MB. Menutup koneksi: Client dapat menutup koneksi ke server menggunakan perintah `byebye`. Perintah ini akan mengirimkan pesan ke server untuk menutup koneksi, dan program client akan keluar.

Program client ini menggunakan loop `while True` untuk terus menerus meminta input dari user. User dapat memasukkan perintah yang ingin dijalankan, dan program akan memproses perintah tersebut. Jika user memasukkan perintah yang tidak dikenali, program akan menampilkan pesan "Perintah tidak dikenali, silahkan coba lagi". Perlu diingat bahwa client harus terhubung ke server sebelum dapat menjalankan perintah apa pun . 

<br>

## Penjelasan Tambahan
- TASK 1 = program dalam bentuk input berupa "path args", ketika pengguna memasukkan command "download <file_path>" maka file yang didownload akan langsung tersimpan dalam folder didalam penyimpanan laptop/pc.
- TASK 2 = ketika pengguna memasukkan command download <file_path>, ketika download tersebut sukses atau berhasil, maka program wajib menampilkan indikator "File Berhasil Disimpan" dan tambahan nama file yang disimpan beserta size nya dalam format 'BYTES' (Berlaku Hanya Dalam command Download).
- TASK 3 = ketika pengguna memasukkan command upload <file_path> dengan format yang sama dan diulang sebanyak 2 kali bahkan lebih (contohnya adalah upload E:\VSCODE\CODINGAN KULIAH\SMT4\README.txt), yang dimasukkan sebanyak 2 kali bahkan lebih, maka program secara otomatis akan menduplikat file yang diupload beserta isinya (contoh ketika pengguna mengupload file path "E:\VSCODE\CODINGAN KULIAH\SMT4\README.txt" dan menjalankan command tersebut di client sebanyak 2 kali, maka file "README.txt" akan terduplikat dan bertambah menjadi "README_(1).txt" dan nomor tersebut akan terus bertambah sesuai dengan seberapa banyak user mengulangi command yang sama (Berlaku Hanya Dalam command Upload)

<br>

## CARA MENGGUNAKAN PROGRAM
1.  Buka terminal dan jalankan program server. Gunakan perintah berikut:

```
python server_program.py
```

2.  Pastikan server berjalan dengan benar. Anda akan melihat pesan "Menunggu koneksi client..." di terminal.

Menjalankan Client:

1.  Buka terminal lain dan jalankan program client. Gunakan perintah berikut:

```
python client_program.py
```

2.  Hubungkan ke server. Gunakan perintah berikut:

```
connme
```

3.  Setelah terhubung, Anda dapat menggunakan perintah-perintah berikut untuk melakukan operasi pada file:
- ls: Menampilkan daftar file di server.
- upload <file path>: Mengunggah file ke server. Ganti `<file path>` dengan <file path> yang ingin Anda unggah.
- download <file path>: Mengunduh file dari server. Ganti `<file path>` dengan <file path> yang ingin Anda unduh.
- rm <nama file>: Menghapus file dari server. Ganti `<nama file>` dengan nama file yang ingin Anda hapus.
- size <nama file>: Melihat ukuran file di server. Ganti `<nama file>` dengan nama file yang ingin Anda ketahui ukurannya.
- byebye: Menutup koneksi ke server dan keluar dari program client.

Contoh Penggunaan:

1.  Unggah file bernama "README.md" ke server:

```
upload E:\VSCODE\CODINGAN KULIAH\SMT4\README.md
```

2.  Lihat daftar file di server:

```
ls
```

3.  Unduh file bernama "README.md" dari server:

```
download E:\VSCODE\CODINGAN KULIAH\SMT4\README.md
```

4.  Hapus file bernama "README.md" dari server:

```
rm README.md
```

5.  Lihat ukuran file bernama "README.md" di server:

```
size README.md
```

6.  Tutup koneksi ke server dan keluar dari program client:

```
byebye
```

<br>

# OUTPUT PROGRAM (DOCUMENTATION)
## No. 1 - 3
![Screenshot 2024-05-04 013427](https://github.com/gerrardgs/Python-Heritage/assets/114888829/07cccad1-78c9-4c73-a6aa-975eebc12b6e)

<br>

![Screenshot 2024-05-04 013440](https://github.com/gerrardgs/Python-Heritage/assets/114888829/a1a0550f-6248-4fb7-9c4b-f8676b7aba90)

<br>

![Screenshot 2024-05-04 013518](https://github.com/gerrardgs/Python-Heritage/assets/114888829/84e935fe-4ea8-4120-bb13-2af631f7e37d)
