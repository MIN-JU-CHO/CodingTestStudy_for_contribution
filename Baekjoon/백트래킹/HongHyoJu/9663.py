def put_queen(num):
    global ans
    if num == n:
        ans += 1
        return

    for i in range(n):
        rows[num] = i
        if is_ok(num):
            put_queen(num+1)


def is_ok(num):
    for i in range(num):
        # 세로
        # if rows[i] == rows[num]:
        #     return False
        # 대각선
        # if abs(num-i) == abs(rows[num] - rows[i]):
        #     return False
        if rows[i] == rows[num] or abs(num-i) == abs(rows[num]-rows[i]):
            return False
    return True


n = int(input())
ans = 0
rows = [0]*n

put_queen(0)
print(ans)
