N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt_0 = 0
cnt_1 = 0
cnt__1 = 0

# 같은 종이로 이뤄졌는지 확인
def is_same(arr):
  global cnt_0, cnt_1, cnt__1
  n = len(arr)
  for i in range(n):
    for j in range(n):
      if arr[0][0] != arr[i][j]:
        return div(arr)
  if arr[0][0] == 0:
    cnt_0 += 1
    return
  elif arr[0][0] == 1:
    cnt_1 += 1
    return
  else:
    cnt__1 += 1
    return


# 종이를 9등분한다.
def div(arr):
  n = len(arr)
  n1 = n // 3
  n2 = n // 3 * 2

  a1 = [i[:n1] for i in arr[:n1]]
  a2 = [i[n1:n2] for i in arr[:n1]]
  a3 = [i[n2:] for i in arr[:n1]]

  a4 = [i[:n1] for i in arr[n1:n2]]
  a5 = [i[n1:n2] for i in arr[n1:n2]]
  a6 = [i[n2:] for i in arr[n1:n2]]

  a7 = [i[:n1] for i in arr[n2:]]
  a8 = [i[n1:n2] for i in arr[n2:]]
  a9 = [i[n2:] for i in arr[n2:]]

  is_same(a1)
  is_same(a2)
  is_same(a3)
  is_same(a4)
  is_same(a5)
  is_same(a6)
  is_same(a7)
  is_same(a8)
  is_same(a9)

is_same(arr)
print(cnt__1)
print(cnt_0)
print(cnt_1)
