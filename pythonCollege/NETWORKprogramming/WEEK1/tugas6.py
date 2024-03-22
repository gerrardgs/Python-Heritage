def main():
  n = int(input("Masukkan nilai n: "))

  for i in range(1, n + 1):
    if i % 3 == 0 and i % 4 == 0:
      print("OKYES")
    elif i % 3 == 0:
      print("OK")
    elif i % 4 == 0:
      print("YES")
    else:
      print(i)

if __name__ == "__main__":
  main()
