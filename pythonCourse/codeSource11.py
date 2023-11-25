######################################################
# Nama file: dictionary-modify.py
######################################################

def main():
   d = {'satu':10, 'dua':20, 'tiga':30}

   # elemen dictionary sebelum diubah
   print("Elemen dictionary sebelum diubah: ")
   print(d)

   # mengubah nilai elemen d['satu'] dan d['tiga']
   d['satu'] = 60
   d['tiga'] = 90

   # elemen dictionary setelah diubah
   print("\nElemen dictionary setelah diubah: ")
   print(d)

if __name__ == "__main__":
   main()
