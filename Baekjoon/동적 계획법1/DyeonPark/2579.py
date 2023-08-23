# https://thinking-developer.tistory.com/169
import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * N
dp = [0] * N

for i in range(N):
  stairs[i] = int(input())

for i in range(N):
  if i == 0:
    dp[0] = stairs[0]
  elif i == 1:
    dp[1] = stairs[0] + stairs[1]
  else:
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[-1])
