# Return factorial of input n
def factorial(n):
  if type(n) == int and n > 1:
    f = n
    for i in range(1, n):
      f *= i
    return f
  elif n == 1 or n == 0:
    return 1
  else:
    return -1
