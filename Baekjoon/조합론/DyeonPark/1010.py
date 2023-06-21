from itertools import combinations

for _ in range(int(input())):
  N, M = map(int, input().split())

  denom = 1 # 분모
  for i in range(N): 
    denom *= (M-i)
   
  num = 1 # 분모
  for i in range(1, N+1):
    num *= i

  print(int(denom/num))
