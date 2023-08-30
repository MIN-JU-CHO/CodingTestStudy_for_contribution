# N : 물품 개수 , K : 버틸 수 있는 무게
N, K = map(int, input().split())

# # [[0] : W무게 , [1] : V가치
items = [(0, 0)]
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

# 행 : N+1개, 열 : K+1개
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = items[i][0]
        v = items[i][1]

        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[-1][-1])
