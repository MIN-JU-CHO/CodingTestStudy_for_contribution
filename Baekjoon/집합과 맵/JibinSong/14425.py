### version 1 ### => pypy로 실행하니 시간 초과 발생, python3로 실행하면 정답 처리
n, m = list(map(int, input().split()))

s = []
for _ in range(n):
  s.append(input())

check_list = []
for _ in range(m):
  check_list.append(input())

result = 0
for i in check_list:
  if i in s:
    result += 1

print(result)

### version 2 ###

n, m = list(map(int, input().split()))

s = set()
for _ in range(n):
  s.add(input())

result = 0
for _ in range(m):
  string = input()
  if string in s:
    result += 1

print(result)
