######################################################
# Nama file: dictionary-modify1.py
######################################################

def main():
   d = {'satu':10, 'dua':20, 'tiga':30}

   # elemen dictionary sebelum diubah
   print("Elemen dictionary sebelum diubah: ")
   print(d)

   # mengubah nilai elemen d['satu']
   d['satu'] = 60

   # menambah elemen d['Satu']
   d['Satu'] = 130

   # elemen dictionary setelah diubah
   print("\nElemen dictionary setelah diubah: ")
   print(d)

if __name__ == "__main__":
   main()
