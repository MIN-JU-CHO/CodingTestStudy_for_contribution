# 듣보잡
N, M = map(int, input().split())

N_set = set([input() for _ in range(N)])
M_set = set([input() for _ in range(M)])

inter = sorted(list(N_set.intersection(M_set)))
print(len(inter))
for i in inter:
  print(i)
