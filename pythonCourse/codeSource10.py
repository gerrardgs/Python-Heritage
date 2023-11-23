######################################################
# Nama file: dictionary-delete.py
######################################################

def main():
   d = {'satu':10, 'dua':20, 'tiga':30}
   
   # elemen dictionary sebelum dihapus
   print("Elemen dictionary sebelum dihapus: ")
   print(d)

   # menghapus nilai elemen d['satu'] dan d['tiga']
   del d['satu']
   del d['tiga']

   # elemen dictionary setelah dihapus
   print("\nElemen dictionary setelah dihapus: ")
   print(d)

if __name__ == "__main__":
   main()
