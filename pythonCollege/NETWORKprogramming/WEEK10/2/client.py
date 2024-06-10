import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host, port))

print("Menyambungkan ke Server")

message = s.recv(1024).decode()
print("Pesan dari server: ", message)

while True:
    try:
        message = s.recv(1024).decode()
        print("Server atau Client lain: ", message)
        new_message = input("Masukkan Pesan: ").encode()
        s.send(new_message)
        print("Pesan Terkirim")
    except:
        print("Koneksi terputus")
        s.close()
        break
