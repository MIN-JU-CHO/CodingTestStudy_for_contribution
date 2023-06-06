def is_decimal(x: int):
  if x == 1:
    return False
  elif x in [2, 3]:
    return True

  for i in range(2, x):
    if x % i == 0:
      return False
  return True


M = int(input())
N = int(input())

nums = []
for i in range(M, N+1):
  if is_decimal(i):
    nums.append(i)

if len(nums) > 0:
  print(sum(nums))
  print(nums[0])
else:
  print(-1)
