N = int(input())
# 빨강, 초록, 파랑
array = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    array[i][0] = min(array[i - 1][1], array[i - 1][2]) + array[i][0]
    array[i][1] = min(array[i - 1][0], array[i - 1][2]) + array[i][1]
    array[i][2] = min(array[i - 1][0], array[i - 1][1]) + array[i][2]

print(min(array[N - 1]))
