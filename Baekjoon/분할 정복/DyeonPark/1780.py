# 문제: 1780 (종이의 개수)
# 첫 번째 풀이 : 시간초과 (~50m)
# 풀이 논리: https://media.discordapp.net/attachments/1018477653860294689/1161409518882799716/image.png?ex=653831e7&is=6525bce7&hm=82ab1934990552763b16149b14b83431f575fafa51ca1c3198548b9358dbd9b8&=&width=1593&height=906
import sys
sys.setrecursionlimit(1000000)

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

def divide_n_conquer(x, y, n):
  global minus_cnt, zero_cnt, plus_cnt
  total = 0
  paper_type = set()
  for i in range(x, x + n):
    paper_type.update(arr[i][y:y + n]) # 이 과정에서 2배로 탐색하게 됨
    total += sum(arr[i][y:y + n])

  if total == -(n**2) and len(paper_type) == 1:
    minus_cnt += 1
    return
  elif total == 0 and len(paper_type) == 1:
    zero_cnt += 1
    return
  elif total == n**2 and len(paper_type) == 1:
    plus_cnt += 1
    return
  else:
    div = N // 3
    for i in range(3):
      for j in range(3):
        divide_n_conquer(x + i * div, y + j * div, div)

divide_n_conquer(0, 0, N)

print(f"{minus_cnt}\n{zero_cnt}\n{plus_cnt}")

# 두 번째 풀이
# 참고: https://zidarn87.tistory.com/385
import sys
sys.setrecursionlimit(1000000)

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

def divide_n_conquer(x, y, n):
  global minus_cnt, zero_cnt, plus_cnt
  
  data = arr[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if data != arr[i][j]: # 종이 종류가 달라지면, 분할이 필요한 것으로 판단 
        for row in range(3):
          for col in range(3):
            div = n // 3
            divide_n_conquer(x + row * div, y + col * div, div)
        return
  if data == -1:
    minus_cnt += 1
  elif data == 0:
    zero_cnt += 1
  else:
    plus_cnt += 1

divide_n_conquer(0, 0, N)
print(f"{minus_cnt}\n{zero_cnt}\n{plus_cnt}")
