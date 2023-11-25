######################################################
# Nama file: file1.py
######################################################

def main():
   # membuat file
   f = open("sample1.txt", "w")

   # menulis ke dalam file
   f.write("Referensi Pemrograman Python\n")
   f.write("Budi Raharjo\n")
   f.write("Penerbit INFORMATIKA\n")
   f.close()

   # membaca file sample1.txt
   for line in open("sample1.txt"):
      print(line, end='')

if __name__ == "__main__":
    main()
