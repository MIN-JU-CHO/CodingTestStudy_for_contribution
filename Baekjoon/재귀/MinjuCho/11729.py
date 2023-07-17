def hanoi (n, start, end):
    # 옮기는 원판이 1개일 때
    if n == 1:
        print(start, end)
        return

    # n-1개를 중간 지점으로 옮기기
    hanoi(n-1, start, 6-start-end)

    # 남은 원판을 목적지에 옮기기
    print(start, end)

    # n-1개를 목적지에 옮기기
    hanoi(n-1, 6-start-end, end)

n = int(input())

# 경우의 수 출력
print(2**n-1)

hanoi(n, 1, 3)
