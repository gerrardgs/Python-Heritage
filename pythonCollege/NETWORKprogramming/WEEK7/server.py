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
