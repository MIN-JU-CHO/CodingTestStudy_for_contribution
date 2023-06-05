p, q = map(int, input().split())

nums = []
for i in range(1, p+1):
  if p % i == 0:
    nums.append(i)

if q > len(nums):
  print(0)
else:
  print(nums[q-1])
