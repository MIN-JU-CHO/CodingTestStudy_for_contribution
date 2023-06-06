def small_decimal(n: int):
  while True:

    if n in [0, 1]:
      n += 1
      continue
    elif n in [2, 3]:
      return n

    is_decimal = True
    for i in range(2, int(n**(1/2))+1):
      if n % i == 0:
        is_decimal = False
        break

    if is_decimal:
      return n

    n += 1


tc = int(input())

for _ in range(tc):
  n = int(input())
  print(small_decimal(n))
