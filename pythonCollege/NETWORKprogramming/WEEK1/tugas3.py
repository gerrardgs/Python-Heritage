def fahrenheit_ke_celsius(fahrenheit):
  """
  Mengubah suhu Fahrenheit ke Celsius.

  Args:
    fahrenheit: Suhu dalam Fahrenheit.

  Returns:
    Suhu dalam Celsius.
  """
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

def celsius_ke_fahrenheit(celsius):
  """
  Mengubah suhu Celsius ke Fahrenheit.

  Args:
    celsius: Suhu dalam Celsius.

  Returns:
    Suhu dalam Fahrenheit.
  """
  fahrenheit = (celsius * 9 / 5) + 32
  return fahrenheit

def main():
  """
  Fungsi utama program.
  """
  # Mendapatkan pilihan konversi dari pengguna
  while True:
    pilihan = input("Masukkan pilihan konversi (F/C): ").upper()
    if pilihan in ("F", "C"):
      break
    else:
      print("Pilihan tidak valid. Masukkan F untuk konversi Fahrenheit ke Celsius atau C untuk konversi Celsius ke Fahrenheit.")

  # Mendapatkan nilai suhu dari pengguna
  while True:
    try:
      suhu = float(input("Masukkan nilai suhu: "))
      break
    except ValueError:
      print("Nilai suhu tidak valid. Masukkan angka.")

  # Melakukan konversi suhu
  if pilihan == "F":
    celsius = fahrenheit_ke_celsius(suhu)
    print(f"{suhu} derajat Fahrenheit sama dengan {celsius:.2f} derajat Celsius.")
  else:
    fahrenheit = celsius_ke_fahrenheit(suhu)
    print(f"{suhu} derajat Celsius sama dengan {fahrenheit:.2f} derajat Fahrenheit.")

if __name__ == "__main__":
  main()
