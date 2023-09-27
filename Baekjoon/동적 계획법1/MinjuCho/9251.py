# 풀이 참고 링크: https://velog.io/@cuppizza/백준-9251-LCS-파이썬-C
import sys
input = sys.stdin.readline
A = ' ' + input().strip()
B = ' ' + input().strip()
dp = [[0 for _ in range(len(B))] for _ in range(len(A))]

# Bottom Up
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
