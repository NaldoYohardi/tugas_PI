while (a != 'x'):
a = int(input("Masukkan Angka : "))
if a < 0:
  print("Angka Negatif")
elif a > 0:
  print("Angka Positif")
elif a == 0:
  print("Angka yang anda Masukkan nol")
elif a == 'x':
  print("Exit Program")
  break
else: 
  print("Error Input")
