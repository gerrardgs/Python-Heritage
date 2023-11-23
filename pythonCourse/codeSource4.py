######################################################
# Nama file: bitwise.py
######################################################

def main():
   x = 120	# dalam bentuk biner: 01111000
   y = 127	# dalam bentuk biner: 01111111

   # menampilkan nilai x dan y
   print("x: \t " + str(x))
   print("y: \t " + str(y))

   print("\nBitwise AND")
   print("x&y \t: " + str(x&y))

   print("\nBitwise OR")
   print("x | y \t: " + str(x | y))

   print("\nBitwise XOR")
   print("x ^ y \t: " + str(x ^ y))

   print("\nBitwise NOT")
   print("~x \t: " + str(~x))
   print("~y \t: " + str(~y))
   print("\nBitwise SHIFT LEFT")
   print("x << 1 \t: " + str(x <<1))
   print("y << 1 \t: " + str(y << 1))

   print("\nBitwise SHIFT RIGHT")
   print("x >> 1 \t: " + str(x >> 1))
   print("y >> 1 \t: " + str(y >> 1))

if __name__ == "__main__":
   main()
