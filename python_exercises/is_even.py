# Return True if input number is even, return False if odd, return -1 if input is not a number
def is_even(n):
  if type(n) == int:
    if n & 1: # Bitwise AND 1
      return False # Odd
    else:
      return True # Even
  else:
    return -1