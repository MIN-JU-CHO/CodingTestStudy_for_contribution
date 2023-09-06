# 문제 해설 링크 : https://velog.io/@cuppizza/백준-1904-01타일-파이썬-C
import sys
input = sys.stdin.readline
N = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746
print(dp[N])
