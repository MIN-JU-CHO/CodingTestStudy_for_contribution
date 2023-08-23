import sys
input = sys.stdin.readline
N = int(input())
S = [ int(input()) for _ in range(N) ]
dp = [0] * N

# 잔개수 2 이하면 모두 더한 값
if N <= 2:
    print(sum(S))

else:
    dp[0] = S[0]
    dp[1] = S[0] + S[1]

    # i-1은 dp값이 아닌 S값이어야 연속 3잔 방지 가능
    for i in range(2, N):
        dp[i] = max(dp[i-3]+S[i-1]+S[i], dp[i-2]+S[i], dp[i-1])

    print(max(dp))
