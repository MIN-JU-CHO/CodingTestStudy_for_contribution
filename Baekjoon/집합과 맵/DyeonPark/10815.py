N = int(input())
cards = set(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

for i in checks:
  if i in cards:
    print(1, end = " ")
  else:
    print(0, end = " ")
