# idea: https://st-lab.tistory.com/136


# arr = [1 5 2 1 4 3 4 5 2 1]
def ascending(i):  # i = 4
  if i == 0:  # 맨 앞은 무조건 1개이기 때문
    return
  else:
    for j in range(i - 1, -1, -1):  # 3, 2, 1, 0
      if arr[j] < arr[i]:  # arr[4] = 4
        # j = 1, arr[0]=1 <= arr[1]=5 ->
        dp_a[i] = max(dp_a[i], dp_a[j] + 1)


def descending(i):
  if i == n:
    return
  for j in range(i + 1, n):
    if arr[i] > arr[j]:
      dp_d[i] = max(dp_d[i], dp_d[j] + 1)


n = int(input())  # n = 10
arr = list(map(int, input().split()))  # 1 5 2 1 4 3 4 5 2 1

# 1로 초기화한 이유는 본인을 기본적으로 세기 위함
dp_a = [1] * n
dp_d = [1] * n
result = []
# print(arr)
for i in range(n):
  ascending(i)

for i in range(n, -1, -1):
  descending(i)

for i, j in zip(dp_a, dp_d):
  result.append(i + j - 1)

print(max(result))
