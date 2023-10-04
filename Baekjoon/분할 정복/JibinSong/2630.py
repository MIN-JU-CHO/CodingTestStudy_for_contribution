# arr가 주어졌을 때, 전체가 같은 색인지 확인하는 함수
def is_same(arr):
  global one_cnt, zero_cnt
  start_value = arr[0][0]
  div_n = len(arr)
  for i in range(div_n):
    for j in range(div_n):
      if arr[i][j] != start_value:
        div(arr)
        return
  if start_value:
    one_cnt += 1
  else:
    zero_cnt += 1
  return


# arr가 주어졌을 때, arr를 분할하는 함수
def div(arr):
  # n이 8일 때,
  n = len(arr)
  mid = n // 2
  # print(n, mid)
  arr1 = [arr[i][:mid] for i in range(mid)]
  arr2 = [arr[i][mid:] for i in range(mid)]
  arr3 = [arr[i][:mid] for i in range(mid, n)]
  arr4 = [arr[i][mid:] for i in range(mid, n)]

  is_same(arr1)
  is_same(arr2)
  is_same(arr3)
  is_same(arr4)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

zero_cnt = 0
one_cnt = 0

is_same(arr)
print(zero_cnt)
print(one_cnt)
