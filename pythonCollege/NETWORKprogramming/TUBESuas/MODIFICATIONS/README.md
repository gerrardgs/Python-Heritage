## KETERANGAN: Program dapat dilihat di file `server.py` dan `client.py`

<br>

# HOSTING STEP-BY-STEP
1. daftarkan kelompok anda
2. akses server:

`ssh progjar@10.169.13.13` ( jaringan intranet, wifi tel-u connect / telkomuniv )

`ssh progjar@showcase.ittsby.id -p10000` ( jaringan publik)

password: `progjarIF24`

3. masuk ke folder kelompok kalian
`cd kelompokXX`

4. lanjut silahkan clone repository final project 
`git clone XXXXXX`

6. set port ke port yang telah ditentukan di `app.py`
7. jalankan flask dengan python bukan dengan flask run

`python3 app.py`

9. jika menggunakan socket, maka:

set port ke port yang telah ditentukan di `server.py`

10. jalankan `python3 server.py`
11. close terminal 
 
12. jika menggunakan flask, maka:

akses di browser kesayangan kalian

`https://showcase.ittsby.id/IF24-Progjar/kelompokXX/`

jika menggunakan telu-connect maka akses

`http://10.169.13.13/IF24-Progjar/kelompokXX/`

jika menggunakan socket

rubah client connect ke socket `10.169.13.13` port nya sesuai kelompok

jangan lupa rubah XX dengan nomor kelompok kalian

<br>

# DATA
- KELOMPOK: 5
- DOMAIN: `https://showcase.ittsby.id/IF24-Progjar/kelompok5/`
- IP: http://10.169.13.13/IF24-Progjar/kelompok5/
- PORT: 11005
- HOST: 10.169.13.13
