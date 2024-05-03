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
        
