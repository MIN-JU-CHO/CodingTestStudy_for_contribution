while True:
  n = int(input())
  if n == -1:
    break

  nums = []
  for i in range(1, n):
    if n % i == 0:
      nums.append(i)

  if sum(nums) == n:
    print(f"{n} = {' + '.join([str(i) for i in nums])}")
  else:
    print(f"{n} is NOT perfect.")
