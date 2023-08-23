# https://thinking-developer.tistory.com/168
import sys
input = sys.stdin.readline

N = int(input())
wines, dp = [], [0] * N
for _ in range(N):
  wines.append(int(input()))

for i in range(N):
  if i == 0:
    dp[i] = wines[i]
  elif i == 1:
    dp[i] = dp[i - 1] + wines[i]
  elif i == 2:
    dp[i] = max(dp[i - 1], max(wines[i - 1] + wines[i], dp[i - 2] + wines[i]))
  else:
    dp[i] = max(dp[i - 1], max( dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i]))
      
print(dp[-1])
