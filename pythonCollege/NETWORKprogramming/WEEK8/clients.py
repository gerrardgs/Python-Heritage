import socket

# Inisialisasi socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan ke server
server_address = ('localhost', 5000)
sock.connect(server_address)

while True:
    # Meminta input dari pengguna
    message = input('Masukkan operasi matematika (contoh "1 + 1") atau ketik "exit" untuk keluar: ')
    
    if message.lower() == 'exit':
        sock.send(message.encode())
        break
    
    # Mengirim pesan ke server
    sock.send(message.encode())
    
    # Menerima pesan balasan dari server
    response = sock.recv(1024).decode()
    print('Result:', response)

# Menutup koneksi dengan server
sock.close()
