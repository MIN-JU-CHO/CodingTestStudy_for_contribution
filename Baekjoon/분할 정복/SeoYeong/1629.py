def dq(A: int, B: int, C: int) ->int:
    print(A, B, C)
    if B == 1:
        return A%C
    elif B % 2 == 0:
        return (dq(A, B//2, C) **2) %C
    else:
        return ((dq(A, B//2, C) **2) *A) %C


A, B, C = map(int, input().split())
answer = dq(A, B, C)
print(answer)


