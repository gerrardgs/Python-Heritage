# LAPORAN PRAKTIKUM TUGAS 2
## NAMA: Gerrard Sebastian
## NIM: 1203220018
## KELAS: IF-02-01

# SOAL
1.	Membuat sebuah program server yang dapat menerima koneksi dari klien menggunakan protokol TCP. Server ini akan menerima pesan dari klien dan mengirimkan pesan balasan berisi jumlah karakter pada pesan tersebut. Gunakan port 12345 untuk server. Membuat analisa dari hasil program tersebut
2.	Membuat sebuah program klien yang dapat terhubung ke server yang telah dibuat pada soal nomor 1. Klien ini akan mengirimkan pesan ke server berupa inputan dari pengguna dan menampilkan pesan balasan jumlah karakter yang diterima dari server. Membuat analisa dari hasil program tersebut

# JAWABAN
## LINK GITHUB: https://bit.ly/TugasProJarWeek3Gerrard 

### 1.	Server Program

Penjelasan:
-	Impor Modul Socket: Modul socket diimpor untuk menyediakan akses ke API soket BSD.
-	Deklarasi Variabel: Variabel HOST dan PORT dideklarasikan untuk menentukan alamat dan port tempat server akan berjalan.
-	Membuat Socket Server: with statement digunakan untuk memastikan bahwa soket ditutup dengan benar setelah blok kode selesai. Socket dibuat dengan socket.socket(socket.AF_INET, socket.SOCK_STREAM) yang menunjukkan penggunaan IPv4 dan protokol TCP.
-	Binding: Socket server diikat ke alamat dan port yang ditentukan dengan server_socket.bind((HOST, PORT)).
-	Listening: Server mulai mendengarkan koneksi masuk dengan server_socket.listen().
-	Menerima Koneksi: Server menerima koneksi dari klien dengan client_socket, client_address = server_socket.accept() dan mencetak alamat klien yang terhubung.
-	Loop Penerimaan Pesan: Server memasuki loop tak terbatas di mana ia menerima pesan dari klien dengan data = client_socket.recv(1024). Jika tidak ada data, loop akan dihentikan.
-	Menghitung Jumlah Karakter: Server menghitung jumlah karakter dalam pesan yang diterima dan menyusun balasan.
-	Mengirim Balasan: Server mengirimkan balasan ke klien dengan client_socket.send(balasan.encode()).
-	Menutup Socket: Setelah selesai, soket klien dan server ditutup.






### 2.	Client Program
 
Penjelasan:
-	Impor Modul Socket: Sama seperti server, modul socket diimpor.
-	Deklarasi Variabel: Variabel HOST dan PORT dideklarasikan untuk menentukan alamat dan port server.
-	Membuat Socket Klien: Socket klien dibuat dan dihubungkan ke server dengan client_socket.connect((HOST, PORT)).
-	Mengirim Pesan: Klien meminta input dari pengguna dan mengirim pesan ke server dengan client_socket.send(pesan.encode()).
-	Menerima Balasan: Klien menerima balasan dari server dan mendekodenya.
-	Menampilkan Balasan: Klien mencetak balasan yang diterima dari server.
-	Menutup Socket: Soket klien ditutup setelah selesai.

Konklusi: Program diatas memungkinkan komunikasi dua arah antara server dan klien. Server menerima pesan dari klien, lalu menghitung jumlah karakter, dan mengirimkan informasi tersebut kembali ke klien. Klien mengirimkan pesan ke server dan menampilkan balasan yang diterima. Penggunaan with statement memastikan bahwa soket ditutup dengan benar, serta menghindari kebocoran sumber daya. Program diatas harus dijalankan dalam lingkungan yang mendukung protokol TCP dan memungkinkan koneksi soket (dedicated terminal).

### OUTPUT PROGRAM (SOAL NO. 1 & 2)
SERVER:
 
CLIENT:
 
