# solved : 18m
# https://thinking-developer.tistory.com/171

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [0] * N
dp[0] = max(-(sys.maxsize), nums[0])

for i in range(1, N):
  dp[i] = max(nums[i], dp[i - 1] + nums[i])

print(max(dp))
