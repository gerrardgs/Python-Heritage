######################################################
# Nama file: faktorial.py
######################################################

import sys

def main():
   # menampilkan judul program
   print("Nilai Faktorial Bilangan")

   # meminta user memasukkan bilangan 
   # yang akan dihitung faktorialnya
   n = int(input("\nMasukkan bilangan: "))

   if n < 0:
      print("\nBilangan tidak boleh negatif")
      sys.exit(1)

   faktorial = 1  # mula-mula faktorial bernilai 1

   # menghitung faktorial
   print("%d! = " % n, end='')
   i = n
   while i >= 1:
      if i != 1:
         print("%d x " % i, end='')
      else:
         print("%d = " % i, end='')
      faktorial *= i;
      i -= 1;	# decrement

   # menampilkan hasil
   print(faktorial)

if __name__ == "__main__":
   main()
