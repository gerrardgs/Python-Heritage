######################################################
# Nama file: balok.py
######################################################

def main():
   # menampilkan informasi program
   print("Volume dan Luas Permukaan Balok\n")

   # input panjang, lebar, dan tinggi
   p = float(input("Panjang \t: "))
   l = float(input("Lebar \t: "))
   t = float(input("Panjang \t: "))

   # melakukan perhitungan
   V = p * l * t
   LP = 2 * (p*l + p*t + l*t)

   # menampilkan hasil perhitungan ke layar
   print("\nVolume \t\t:", V)
   print("Luas Permukaan \t:", LP)

if __name__ == "__main__":
   main()
