def recur(n):
  if n in [0, 1]:
    return n
  else:
    return recur(n-1) + recur(n-2)

N = int(input())
print(recur(N))
