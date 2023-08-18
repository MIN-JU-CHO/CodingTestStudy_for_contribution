N = int(input())
S = [int(input()) for _ in range(N)]

# dp 리스트 : 각 인덱스까지의 최대 값 저장
dp = [0] * N

if N <= 2:
    print(sum(S))
else:
    dp[0] = S[0]
    dp[1] = S[0] + S[1]
    for i in range(2, N):
        dp[i] = max(dp[i - 3] + S[i - 1] + S[i], dp[i - 2] + S[i])
    print(dp[-1])

# dp[i-3] + S[i-1] + S[i] : X O O
# dp[i-2] + S[i] : O X O
