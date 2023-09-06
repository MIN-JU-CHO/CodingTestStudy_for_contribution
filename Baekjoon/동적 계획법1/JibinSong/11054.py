# https://st-lab.tistory.com/136
def count_less(i):
  for j in range(i, 0, -1):
    if arr[j] <= arr[i]:
      dp_r[i] = max(dp_r[i], count_less(i)+1)

def count_more(i):
  for j in range(i, n):
    if arr[j] <= arr[i]:
      dp_l[i] = max(dp_l[i], count_more(i)+1)

n = int(input())
arr = list(map(int, input().split()))
dp_r = [1] * n
dp_l = [1] * n
result = []
for i in range(n):
  # 현재 원소를 기준으로 오름차순
  count_less(i)
  count_more(i)

for i,j in zip(dp_r,dp_l):
  result.append(i+j-1)

print(result)
