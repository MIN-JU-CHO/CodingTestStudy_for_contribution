# https://velog.io/@cuppizza/%EB%B0%B1%EC%A4%80-2579-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
input = sys.stdin.readline
N = int(input())
S = [ int(input()) for _ in range(N) ]
dp = [0] * N

# 계단 2 이하면 모두 더한 값
if N <= 2:
    print(sum(S))

else:
    dp[0] = S[0]
    dp[1] = S[0] + S[1]

    # i-1은 dp값이 아닌 S값이어야 연속 3계단 방지 가능
    for i in range(2, N):
        dp[i] = max(dp[i-3]+S[i-1]+S[i], dp[i-2]+S[i])

    print(dp[-1])
