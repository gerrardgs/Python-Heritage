######################################################
# Nama file: akarpersamaan.py
######################################################

import sys		# untuk fungsi exit()
import math		# untuk fungsi sqrt()

def main():
   # menampilkan judul program
   print("Akar-akar Persamaan Kuadrat")

   # meminta user memasukkan koefisien persamaan
   a = int(input("\nMasukkan a: "))
   b = int(input("Masukkan b: "))
   c = int(input("Masukkan c: "))

   # menghitung diskriminan
   D = (b*b) - (4*a*c)

   if D < 0:
      print("Akar-akar imajiner")
      sys.exit(1)  # keluar program
   elif D == 0:
      x1 = (-b + math.sqrt(D)) / (2*a)
      x2 = x1
   else:
      x1 = (-b + math.sqrt(D)) / (2*a)
      x2 = (-b - math.sqrt(D)) / (2*a)

   # menampilkan hasil
   print("\nx1 = %d" %x1)
   print("x2 = %d" % x2)

if __name__ == "__main__":
   main()
