def draw(n):
    if n == 3:
        star[0][:3] = star[2][:3] = [1]*3
        star[1][:3] = [1, 0, 1]
        return

    a = n//3
    draw(a)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                star[a*i+k][a*j:a*(j+1)] = star[k][:a]


N = int(input())
star = [[0] * N for i in range(N)]

draw(N)

for i in star:
    for j in i:
        if j:
            print("*", end='')
        else:
            print(" ", end='')
    print()
