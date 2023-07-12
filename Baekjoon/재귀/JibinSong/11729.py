n = int(input())

def count_top(i):
  if i == 1:
    num = 1
    return num
  num = count_top(i-1)
  num = num + 1 + num
  return num

print(count_top(n))
