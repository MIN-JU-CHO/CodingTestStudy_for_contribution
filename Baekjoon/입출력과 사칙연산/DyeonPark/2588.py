a = input()
b = input()

tmp1 = int(a) * int(b[-1])
tmp2 = int(a) * int(b[-2])
tmp3 = int(a) * int(b[-3])

print(tmp1)
print(tmp2)
print(tmp3)
print(tmp1 + tmp2 * 10 + tmp3 * 100)
