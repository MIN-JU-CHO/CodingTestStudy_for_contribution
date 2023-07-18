
def cut(a, n):
    if n == 1:
        return
    for i in range(a + n//3, a+(n//3)*2):
        ans[i] = ' '
    cut(a, n//3)
    cut(a + (n//3)*2, n//3)


while True:
    try:
        n = int(input())
        ans = ['-']*(3**n)
        cut(0, 3**n)
        print(''.join(ans))
    except:
        break
