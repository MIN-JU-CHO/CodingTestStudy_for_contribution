# https://thinking-developer.tistory.com/158
N = int(input())
print(2 ** N - 1)

A, B, C = [], [], []

def move(N, _from, _to):
  print(f{_from} {_to}")

def hanoi(N, _from, _to, _via):
  if N == 1:
    move(N, _from, _to)
  else:
    hanoi(N-1, _from, _via, _to)
    move(N, _from, _to)
    hanoi(N-1, _via, _to, _from)

hanoi(N, "A", "C", "B")
