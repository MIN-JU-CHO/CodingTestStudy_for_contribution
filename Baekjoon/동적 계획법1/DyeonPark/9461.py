import sys 
input = sys.stdin.readline

p = [1] * (101)
for i in range(4, 101):
  p[i] = p[i-2] + p[i-3]

for i in range(int(input())):
  print(p[int(input())])
