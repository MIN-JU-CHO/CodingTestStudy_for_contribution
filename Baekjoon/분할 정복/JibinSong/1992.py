def is_same(arr):
  global result

  n = len(arr)
  start_value = arr[0][0]
  for i in range(n):
    for j in range(n):
      if arr[i][j] != start_value:
        return div(arr)
  if start_value:
    result += '1'
  else:
    result += '0'
  return


def div(arr):
  global result
  n = len(arr)
  mid = n // 2
  result += '('
  arr1 = [arr[i][:mid] for i in range(mid)]
  arr2 = [arr[i][mid:] for i in range(mid)]
  arr3 = [arr[i][:mid] for i in range(mid, n)]
  arr4 = [arr[i][mid:] for i in range(mid, n)]
  is_same(arr1)
  is_same(arr2)
  is_same(arr3)
  is_same(arr4)
  result += ')'


N = int(input())

arr = [list(map(int, list(input()))) for _ in range(N)]

# print(arr)
result = ''
is_same(arr)

print(result)
