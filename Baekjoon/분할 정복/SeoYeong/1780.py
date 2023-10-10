from itertools import chain

def to_be_cut(x: int, y: int, l: int) -> bool:
    global a, b, c
    # flattened_list = list(chain(*original_list))
    flattened_set = list(set(chain(*[paper[i][y:y+l] for i in range(x, x+l)])))
    if len(flattened_set) == 1:
        if flattened_set[0] == -1: 
            a+=1
        elif flattened_set[0] == 0: 
            b+=1
        else: 
            c+=1
        return True
    return False


def divide(x: int, y:int, l:int):
    if to_be_cut(x, y, l):
        return 
    else:
        divide(x, y, l//3)
        divide(x, y+l//3, l//3)
        divide(x, y+2*l//3, l//3)
        divide(x+l//3, y, l//3)
        divide(x+l//3, y+l//3, l//3)
        divide(x+l//3, y+2*l//3, l//3)
        divide(x+2*l//3, y, l//3)
        divide(x+2*l//3, y+l//3, l//3)
        divide(x+2*l//3, y+2*l//3, l//3)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
a, b, c = 0, 0, 0

divide(0, 0, N)

print(f"{a}\n{b}\n{c}")
