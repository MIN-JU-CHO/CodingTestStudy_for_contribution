import sys

def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        mid = (len(A)+1) // 2
        left = merge_sort(A[:mid])            # 전반부 정렬
        right = merge_sort(A[mid:])         # 후반부 정렬

        # MERGE
        i, j = 0, 0
        temp = []
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:                  # 왼쪽 배열 원소 삽입
                temp.append(left[i])
                result.append(left[i])
                print(result)
                i+=1
            else:                                       # 오른쪽 배열 원소 삽입
                temp.append(right[j])
                result.append(right[j])
                print(result)
                j+=1
        while i < len(left):                    # 왼쪽 배열 부분이 남은 경우
            temp.append(left[i])
            result.append(left[i])
            print(result)
            i+=1
        while j < len(right):               # 오른쪽 배열 부분이 남은 경우
            temp.append(right[j])
            result.append(right[j])
            print(result)
            j+=1
        return temp

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 실행 과정을 그대로 담을 배열
result = []
merge_sort(A)

if len(result) >= K:
    print(result[K-1])
else:
    print(-1)
