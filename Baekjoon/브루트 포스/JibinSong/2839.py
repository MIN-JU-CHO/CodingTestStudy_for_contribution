n = int(input())

m = n // 5
result = 0
for i in range(m, -1, -1):
  if (n - 5 * i) % 3 == 0:
    result = i + (n - 5 * i) // 3
    print(result)
    break

if not result:
  print(-1)
