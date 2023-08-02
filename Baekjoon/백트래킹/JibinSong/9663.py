#  queen의 공격 위치 표시
def set_queen(arr_copy, x, y):
  # 십자
  arr_copy[x][y] = 2
  # 공격 위치 표시
  for i in range(1, n):
    # 십자
    print(*arr_copy, sep='\n')
    print()
    if arr_copy[x][i] == 2:  # 퀸의 자리를 공격하면 => return false
      return [False, False]
    else:
      arr_copy[x][i] = 1
    print(*arr_copy, sep='\n')
    print()
    if arr_copy[i][y] == 2:
      return [False, False]
    else:
      arr_copy[i][y] = 1
    # 대각선
    print(*arr_copy, sep='\n')
    print()
    if arr_copy[i][i] == 2:
      return [False, False]
    else:
      arr_copy[i][i] = 1
  print('result')
  print(*arr_copy, sep='\n')
  print()
  return [True, arr_copy]


def suceess(x, y):
  arr = [[0 for _ in range(n)] for _ in range(n)]
  num = n
  arr = set_queen(arr, x, y)[1]
  print("확인용", *arr, sep='\n')
  print()
  # 퀸을 다 배치시킬 때까지
  for i in range(n):
    print("i", i)
    for j in range(n):
      print("cnt", cnt)
      if num <= 0:
        return True
      if arr[i][j] == 0:
        get = set_queen(arr, i, j)
        print(get)
        if get[0]:
          num -= 1
          arr = get[1]

  return False


n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0

for i in range(n):
  for j in range(n):
    if suceess(i, j):
      cnt += 1
print(cnt)
