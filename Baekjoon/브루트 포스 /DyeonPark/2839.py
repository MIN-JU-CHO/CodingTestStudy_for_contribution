import sys

N = int(input())

max_5 = N // 5
count = sys.maxsize

is_pos = False
for i in range(max_5, -1, -1):
  remain = N - (5 * i)
  if remain % 3 == 0:
    count = min(count, remain // 3 + i)
    is_pos = True

if is_pos:
  print(count)
else:
  print(-1)
