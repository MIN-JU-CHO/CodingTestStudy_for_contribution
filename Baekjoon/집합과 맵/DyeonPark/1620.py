import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}

for i in range(N):
  pokemon[input().strip()] = i + 1

names = list(pokemon.keys())
for i in range(M):
  cmd = input().strip()
  if cmd.isdigit():
    print(names[int(cmd)-1])
  else:
    print(pokemon[cmd])
