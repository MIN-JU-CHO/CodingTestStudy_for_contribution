n = int(input())
arr = list(map(int, input().split()))

# 각 원소까지 갔을 때의 최대값
dp = arr

for i in range(1, n):
  dp[i] = max(dp[i], dp[i]+dp[i-1])

print(max(dp))
