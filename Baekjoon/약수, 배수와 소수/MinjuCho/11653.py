N = int(input())
result = []
i=2
while i<=N:
    if N%i==0:
        N = N/i
        result.append(i)
        continue
    else:
        i = i+1
for num in result:
    print(num)
