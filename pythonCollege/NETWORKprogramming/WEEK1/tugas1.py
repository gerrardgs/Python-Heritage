def hitung_huruf(kata):
  """
  Menghitung jumlah huruf dalam sebuah kata.

  Args:
    kata: Sebuah string yang mewakili kata yang ingin dihitung jumlah hurufnya.

  Returns:
    Jumlah huruf dalam kata.
  """
  jumlah_huruf = 0
  for huruf in kata:
    if huruf.isalpha():
      jumlah_huruf += 1
  return jumlah_huruf

# Meminta pengguna untuk memasukkan kata
kata = input("Masukkan kata: ")

# Menghitung jumlah huruf dalam kata
jumlah_huruf = hitung_huruf(kata)

# Menampilkan hasil
print(f"Jumlah huruf dalam kata '{kata}' adalah {jumlah_huruf}")
