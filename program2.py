x = ''
y = ''

while (y != 'n'):
  try:
    x = int(input("Input : "))
  except:
    print("Error - Input Integers Only !")
    continue
  if x > 0:
    print("Positive")
  elif x < 0:
    print("Negative")
  elif x == 0:
    print("Zero")
    
  y = input("Continue ? y/n : ")
  
