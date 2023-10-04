n = int(input())
d = [[0 for _ in range(10)] for _ in range(n)]
d[0][1:] = [1 for _ in range(9)]
# 0이 맨 앞에 올 수 없다.
# d[0][0] = 0
# print(d)
'''
[
  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
'''

for i in range(n - 1):
  for j in range(10):
    if j == 0:
      # 이후 값만
      d[i + 1][j + 1] += d[i][j]
    elif j == 9:
      # 이전 값만
      d[i + 1][j - 1] += d[i][j]
    else:
      # 이후, 이전 값
      d[i + 1][j - 1] += d[i][j]
      d[i + 1][j + 1] += d[i][j]

print(sum(d[-1]) % 1000000000)
