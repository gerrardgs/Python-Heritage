######################################################
# Nama file: detik_ke_jam.py
######################################################

def main():
   # menampilkan informasi program
   print("Konversi Detik ke Jam\n")

   # input total detik
   totaldetik = int(input("Masukkan detik \t: "))

   # melakukan konversi hh:mm:ss ke detik
   hh = totaldetik // 3600
   sisadetik = totaldetik % 3600
   mm = sisadetik // 60
   ss = sisadetik % 60

   # menampilkan hasil konversi
   print("%d detik sama dengan %d:%d:%d" %
         (totaldetik, hh, mm, ss))

if __name__ == "__main__":
   main()
