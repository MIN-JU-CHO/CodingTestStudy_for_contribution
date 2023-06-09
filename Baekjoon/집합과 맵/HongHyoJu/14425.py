
# 자료형에 따라 시간복잡도가 다름.
# list 의 삽입, 제거, 탐색, 포함여부는 보통 O(N)
# dict, set 의 삽입, 제거, 탐색, 포함여부는 보통 O(1)
# dict, set 이 시간복잡도가 낮은 이유는 hash 값을 사용하기 때문에 빠른 접근이 가능.

# ==> 값의 순서, index 에 접근할 때는 보통 list 를 사용,
#     값의 탐색이나 확인은 보통 dict, set 을 많이 사용한다.

# set : 순서 없고, 중복 허용하지 않음.
# dict : 순서 없고, key/value 쌍으로 이루어짐 {'a':1, 'b':2}

S = set()
cnt = 0
N, M = map(int, input().split())

for _ in range(N):
    S.add(input().strip())

for _ in range(M):
    if input().strip() in S:
        cnt += 1

print(cnt)
