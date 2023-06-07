# 소수 확인 모듈
def is_prime_number(n):
  if n == 1 or n == 0:
    return False
  if n == 2:
    return True
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


for _ in range(int(input())):
  n = int(input())

  while not is_prime_number(n):
    n += 1
  print(n)
