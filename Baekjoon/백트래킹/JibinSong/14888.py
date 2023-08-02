import math
from itertools import permutations, combinations, product, combinations_with_replacement


def get_operator(a, i, b):
  if i == 0:
    return a + b
  if i == 1:
    return a - b
  if i == 2:
    return a * b
  if i == 3:
    if a < 0:
      return -(-a // b)
    return a // b


n = int(input())

# 1~100
arr = list(map(int, input().split()))

# 덧셈:0, 뺄셈:1, 곱셈:2, 나눗셈:3
operator = list(map(int, input().split()))
arr2 = []

for i in range(4):
  arr2.extend([i] * operator[i])
# print(arr2)  # [0, 0, 1, 2, 3]

min = math.inf
max = -math.inf

for i in permutations(arr2, n - 1):
  result = arr[0]
  for j in range(n - 1):
    result = get_operator(result, i[j], arr[j + 1])
  if result <= min:
    min = result
  if result >= max:
    max = result
print(max)
print(min)
