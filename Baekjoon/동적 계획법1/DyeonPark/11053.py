# https://thinking-developer.tistory.com/164

# 첫 번째 풀이
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

cnts = [[0] * N for _ in range(N)]
for i in range(N):
  cnts[i][i] = 1
  max_val = A[i]
  for j in range(i + 1, N):
    if A[j] > max_val:
      max_val = A[j]
      cnts[i][j] = cnts[i][j-1] + 1
    else:
      cnts[i][j] = cnts[i][j-1]

maximum = 0
for i in range(N):
  maximum = max(maximum, cnts[i][-1])
print(maximum)


# 두 번째 풀이
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
cnts = [0] * N

cnts[0] = 1 
for i in range(1, N):
  maximum = 0
  for j in range(i):
    if A[j] < A[i]:
      maximum = max(maximum, cnts[j])
  cnts[i] = maximum + 1

print(max(cnts))
