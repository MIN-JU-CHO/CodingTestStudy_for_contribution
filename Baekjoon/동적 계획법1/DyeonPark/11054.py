# solved : 30m

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

up = [0] * N
down = [0] * N

up[0] = 1
down[-1] = 1

# up case
for i in range(1, N):
  maximum = 0
  for j in range(i):
    if A[j] < A[i]:
      maximum = max(maximum, up[j])
  up[i] = maximum + 1

# down case
for i in range(N - 1, -1, -1):
  maximum = 0
  for j in range(N - 1, i, -1):
    if A[j] < A[i]:
      maximum = max(maximum, down[j])
  down[i] = maximum + 1
  
# get total
maximum = 0
for i in range(N):
  maximum = max(maximum, up[i] + down[i] - 1)

print(maximum)
