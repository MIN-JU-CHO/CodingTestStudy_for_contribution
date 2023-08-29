import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [0] * (K+1)
for _ in range(N):
    w, v = map(int, input().split())
    # 더 큰 weight 입력 예외처리
    if w > K:
        continue
    # DP 1차원 배열 끝부터
    for j in range(K, 0, -1):
        if j+w<=K and dp[j] != 0:
            # weight 확인, dp값 존재하면 -> 해당 자리와 새 값 비교
            #print("j+w=",j,'+',w,"=",j+w, ", dp[j+w] =", dp[j+w],  ", dp[j] =", dp[j],"v=", v)
            dp[j+w] = max(dp[j+w], dp[j]+v)
    # 자기 자리 max update
    dp[w] = max(dp[w], v)
print(max(dp))
