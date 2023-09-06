# 메모리 초과
n = int(input())

dp = [0] * n

if n >= 1:
  dp[0] = 1
if n >= 2:
  dp[1] = 2
if n >= 3:
  for i in range(2, n):
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[-1] % 15746)

#
n = int(input())

dp = [0] * n
if n >= 1:
  dp[0] = 1
if n >= 2:
  dp[1] = 2
if n >= 3:
  for i in range(2, n):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[-1])
