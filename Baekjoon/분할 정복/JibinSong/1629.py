### 풀이1 ### 
a, b, c = map(int, input().split())

mod_list = []

while b > 1:
  b, m = divmod(b, 2)
  mod_list.append(m)

mod_list.reverse()
d = [0 for _ in range(len(mod_list) + 1)]
d[0] = a
for i in range(1, len(d)):
  # 1이면 (=홀수이면)
  if mod_list[i - 1]:
    d[i] = d[i - 1]**2 * d[0]
  else:
    d[i] = d[i - 1]**2

print(d[-1] % c)

### 풀이2 ###
a, b, c = map(int, input().split())

mod_list = []

while b > 1:
  b, m = divmod(b, 2)
  mod_list.append(m)

mod_list.reverse()
d = [0 for _ in range(len(mod_list) + 1)]
d[0] = a
for i in range(1, len(d)):
  # 1이면 (=홀수이면)
  if mod_list[i - 1]:
    d[i] = d[i - 1]**2 * d[0] % c
  else:
    d[i] = d[i - 1]**2 % c

print(d[-1] % c)

### 풀이3 ### 
a, b, c = map(int, input().split())

def mul(b):
  if b == 1:
    return a
  b, m = divmod(b, 2)
  # 1이면 (=홀수이면)
  if m:
    return mul(b)**2*a%c
  else:
    return mul(b)**2%c
print(mul(b)%c)
