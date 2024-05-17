import socket

# Inisialisasi socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket ke alamat dan port tertentu
server_address = ('localhost', 5000)
sock.bind(server_address)

# Menunggu koneksi masuk
sock.listen(1)
print('Menunggu koneksi dari klien...')
while True:
    # Menerima koneksi dari klien
    client_socket, client_address = sock.accept()
    print('Terhubung dengan klien:', client_address)
    
    while True:
        # Menerima pesan dari klien
        data = client_socket.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print('Klien terputus:', client_address)
            break
        
        print('Pesan diterima dari klien:', data)
        
        # Memisahkan operator dan operand
        try:
            operand1, operator, operand2 = data.split()
            operand1 = float(operand1)
            operand2 = float(operand2)
            
            # Melakukan perhitungan matematika
            result = None
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                if operand2 != 0:
                    result = operand1 / operand2
                else:
                    result = 'Error: Division by zero'
            else:
                result = 'Error: Invalid operator'
            
            # Mengonversi hasil ke integer jika hasil adalah bilangan bulat
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            # Mengirim pesan balasan berisi hasil perhitungan ke klien
            response = str(result)
        except ValueError:
            response = 'Error: Invalid input format'
        except Exception as e:
            response = f'Error: {str(e)}'
        
        client_socket.send(response.encode())
    
    # Menutup koneksi dengan klien
    client_socket.close()
