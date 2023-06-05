def is_decimal(n: int):
  if n == 1:
    return False
  elif n in [2, 3]:
    return True
  
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in nums:
  if is_decimal(i):
    cnt += 1
print(cnt)
