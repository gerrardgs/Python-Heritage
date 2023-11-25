######################################################
# Nama file: eksepsi.py
######################################################

import sys

def main():
   try:
      filename = "contoh.txt" 
      # membuka file
      f = open(filename)	# mungkin akan menimbulkan eksepsi IOError

      # membaca file contoh.txt
      for line in f:
         print(line, end='')

      # menutup file
      f.close()
   except IOError as e:
      print("File '%s' tidak ditemukan" % filename)
      sys.exit()

if __name__ == "__main__":
   main()
