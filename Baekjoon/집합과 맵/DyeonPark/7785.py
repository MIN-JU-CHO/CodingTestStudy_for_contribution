names = set()

for _ in range(int(input())):
  name, cmd = input().split()
  if cmd == "enter":
    names.add(name)
  else:
    names.discard(name)

for name in sorted(list(names), reverse=True):
  print(name)
