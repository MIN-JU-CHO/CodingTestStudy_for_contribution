def all_is_same(x: int, y: int, l: int) -> bool:
    print(f'all_is_same({x}, {y}, {l})')
    # 잘린 색종이 내 숫자 합 더한 값으로 완전한지 더 잘라야되는지 리턴
    global white, blue
    summed = sum([paper[i][j] for i in range(x, x+l) for j in range(y, y+l)])
    if summed == 0:
        white += 1
        return True
    if summed in [1, l ** 2]:
        blue += 1
        return True
    return False


def cut(x: int, y: int, l: int):
    global white, blue
    if all_is_same(x, y, l):
        return
    else:
        cut(x, y, l//2)
        cut(x, y+l//2, l//2)
        cut(x+l//2, y, l//2)
        cut(x+l//2, y+l//2, l//2)


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0

cut(0, 0, N)
print(f'{white}\n{blue}')
