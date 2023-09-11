n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# [[a, b], [c, d]]
# 첫번째 항 비교해서 오름차순, 같은 수이면 두번째 항 비교
arr.sort()

# a 전봇대 기준으로 정렬하고 난 후,
# b 전봇대에서 증가하는 가장 긴 부분 수열의 길이 x 를 구한다.
#  -> 11053 가장 긴 부분 수열의 길이
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
