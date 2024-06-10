import socket
import threading

def handle_client(conn, addr, clients):
    print(f"Client {addr} connected")
    conn.send("Selamat datang di Server...".encode())
    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break
            print(f"Client {addr}: {message.decode()}")
            broadcast(message, conn, clients)
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"Client {addr} disconnected")

def broadcast(message, sender_conn, clients):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))
    s.listen(4)

    print("Proses Empat Koneksi")

    clients = []
    while len(clients) < 4:
        conn, addr = s.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr, clients)).start()

if __name__ == "__main__":
    main()
