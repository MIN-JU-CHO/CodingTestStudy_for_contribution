str1 = input()  # ACAYKP => 기준
str2 = input()  # CAPCAK => 선택
N = len(str2)
d = [[1, str2[i + 1:]] for i in range(N)]
# d[0][1] = "32"
print(d)

# if str2[0] in str1:
#   d[0][0] = 1
#   d[0][1] = str2[1:] # APCAK

# now = 1
# if str2[1] in str1:
#   for i in range(1):
#     if str2[1] in d[i][1]:
#       d[1][0] = max(d[i][0]+d[1][0], d[1][0])

for i in range(N):
  # CAPCAK에서 C부터 시작
  # C가 기준에 있는지 확인
  if str2[i] in str1:
    print("str2[i]", str2[i])
    for j in range(i):
      print("j", j, "d[j][1]", d[j][1])
      if str2[i] in d[j][1]:
        d[i][0] = max(d[j][0] + d[i][0], d[i][0])
        d[i][1] = d[j][1][d[j][1].index(str2[i]) + 1:]

# # d[i]+d[2] 가능한지 확인 CP
# def is_okay(key_str):
#   f = key_str[0]
#   for i in key_str:
#     if str1.index(i) > str1.index(i):

# # CAPCAK에서 C부터 시작
# d[0] = 1 # C
# d[1] = max(d[1], d[0]+d[1]) # A 또는 CA
# for k in range(2):
#   # d[i]+d[2] 가능한지 확인
#   d[2] = max(d[2], d[k]+d[2])

# for k in range(3):
#   d[3] = max(d[3], d[i]+d[3])
print("d", d)
