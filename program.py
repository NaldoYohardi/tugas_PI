while (True):
  try :
    x = int(input("Input : "))
  except TypeError:
    print("Only Integers Are Allowed")
  if x < 0:
    print("Negative")
  if x > 0:
    print("Positive")
  if x == 0:
    print("Zero")
