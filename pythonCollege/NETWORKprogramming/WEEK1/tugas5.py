def cetak_bilangan_prima(n):
  """
  Fungsi ini mencetak bilangan prima dari 1 hingga n.

  Args:
    n: Bilangan bulat positif.
  """

  # Buat list untuk menyimpan bilangan prima
  bilangan_prima = []

  # Periksa setiap bilangan dari 2 hingga n
  for i in range(2, n + 1):
    # Periksa apakah bilangan tersebut prima
    is_prima = True
    for j in range(2, i):
      if i % j == 0:
        is_prima = False
        break

    # Jika bilangan prima, tambahkan ke list
    if is_prima:
      bilangan_prima.append(i)

  # Cetak list bilangan prima
  print("Bilangan prima dari 1 hingga {}: {}".format(n, bilangan_prima))

# Minta user memasukkan nilai n
n = int(input("Masukkan nilai n: "))

# Cetak bilangan prima
cetak_bilangan_prima(n)
