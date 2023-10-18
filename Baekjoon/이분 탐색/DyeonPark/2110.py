import sys

def input():
    return sys.stdin.readline().rstrip()

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = sorted(arr)

# 이분 탐색의 기준 설정 
# arr 내의 값이 아닌, 공유기 간 거리 값이 탐색의 기준이 된다!

start = 1 # 공유기 간 최소 거리
end = arr[-1] - arr[0] # 공유기 간 최대 거리
result = 0

while start <= end:
    term = (start + end) // 2 # 공유기 간 가능한 거리 범주의 중간 값
    install_pos = arr[0]
    
    cnt = 1 # 공유기 개수를 세기 위함 (맨 처음에는 꼭 설치하는 것으로 해서 1부터 시작)
    for i in range(1, N):
        if arr[i] >= install_pos + term:
            install_pos = arr[i] # 공유기 설치
            cnt += 1 # 공유기 수 세기
    
    # 공유기 설치를 모두 마쳤다면, 설치된 공유기 수에 따라서 공유기 간 거리 값(term)을 이분탐색으로 재설정한다
    if cnt >= C: # 설치된 공유기의 수가 많다면, 아직 공유기 간 거리를 더 넓게 설정할 수 있는 상황
        start = term + 1
        result = term # 최대값을 찾는 것이기 때문에, 거리를 늘릴 때만 result를 업데이트 해준다!
    else: # 공유기가 더 적게 설치된다면, 공유기 간 거리를 줄여야 하는 상황
        end = term - 1

print(result)