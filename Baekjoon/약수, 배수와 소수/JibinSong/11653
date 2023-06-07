# ### version1 ###
n = int(input())

for i in range(2, n + 1):
  if n == 1:
    break
  while n % i == 0:
    print(i)
    n /= i

### version2 ###
n = int(input())

for i in range(2, int(n**0.5) + 2):
  if n == 1:
    break
  while n % i == 0:
    print(i)
    n //= i # n/=i 하면 오류남 103.0으로 출력됨
if n != 1:
  print(n)
