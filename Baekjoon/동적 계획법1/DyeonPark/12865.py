# 참고
# https://howudong.tistory.com/106
# https://youtu.be/rhda6lR5kyQ?si=3q9R4Snmj2JugtmD
# https://claude-u.tistory.com/208


import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
dumps = [list(map(int, input().split())) for _ in range(N)]

# 행(물건) x 열(무게)
dp = [[0 for j in range(K + 1)] for i in range(N + 1)]

for i in range(1, N + 1): # 물건
  weight = dumps[i - 1][0]
  value = dumps[i - 1][1]
  for j in range(1, K + 1): # 무게
    if j < weight: # 담을 수 있는 무게가 담아야하는 무게보다 적은 경우
      dp[i][j] = dp[i - 1][j] # 이전의 값을 그대로 가져온다
    else: # 담을 수 있는 경우
      # 담을 수 있지만 안담는 경우 vs 담는 경우 중 최대값을 저장
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N][K])
