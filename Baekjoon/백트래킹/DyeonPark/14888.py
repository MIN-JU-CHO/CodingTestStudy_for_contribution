import sys

INF = sys.maxsize
max_val = -INF
min_val = INF

N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

def backtracking(depth, res, plus, minus, multiple, div):
  global max_val, min_val
  # depth == N-1: # 잘못된 예시
  if depth == N:
    max_val = max(max_val, res)
    min_val = min(min_val, res)
    return
  
  if plus:
    backtracking(depth + 1, res + nums[depth], plus - 1, minus, multiple, div)
  if minus:
    backtracking(depth + 1, res - nums[depth], plus, minus - 1, multiple, div)
  if multiple:
    backtracking(depth + 1, res * nums[depth], plus, minus, multiple - 1, div)
  if div:
    backtracking(depth + 1, int(res / nums[depth]), plus, minus, multiple, div - 1)

# backtracking(0, nums[0], oper[0], oper[1], oper[2], oper[3]) # 잘못된 예시
backtracking(1, nums[0], oper[0], oper[1], oper[2], oper[3])
print(max_val)
print(min_val)
