# 소요 시간: 약 30m
# 풀이 링크: https://file.notion.so/f/f/e3a1bb69-1ac8-40f7-baa4-cd9b87eabde9/ee76ec69-e11a-4e0e-9c93-a68976901ea5/%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B3%E1%86%B8%E1%84%8C%E1%85%A1%E1%86%BC_-16.jpg?id=147d7c12-c6a3-4413-b846-2e38c2178801&table=block&spaceId=e3a1bb69-1ac8-40f7-baa4-cd9b87eabde9&expirationTimestamp=1696550400000&signature=IQNfjrf5CgxMqpMG0WOZSztvpM6TFj_OXKAFKi1WcBM&downloadName=%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B3%E1%86%B8%E1%84%8C%E1%85%A1%E1%86%BC+%F0%9F%98%8E-16.jpg
# 참고 여부: 참고하지 않음
import sys
sys.setrecursionlimit(1000000)

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
image = [list(map(int, input())) for _ in range(N)]


def divide_n_conquer(x, y, n):
  # print('(', end='')
  total = 0
  for i in range(n):
    total += sum(image[x + i][y:y + n])

  if total == 0:
    print('0', end='')
  elif total == n * n:
    print('1', end='')
  else:
    print("(", end='')
    half = n // 2
    divide_n_conquer(x, y, half) # 왼쪽 위
    divide_n_conquer(x, y + half, half) # 오른쪽 위
    divide_n_conquer(x + half, y, half) # 왼쪽 아래
    divide_n_conquer(x + half, y + half, half) # 오른쪽 아래
    print(")", end='')

divide_n_conquer(0, 0, N)
