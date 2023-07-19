def merge_sort(array):
  if len(array)>=2:
    q = (0 + len(array)-1) // 2
    # 전반부 정렬
    front = array[:q + 1]
    print('front',front)
    front = merge_sort(front)
    # 후반부 정렬
    back = array[q + 1:]
    print('back',back)
    back = merge_sort(back)
    # 병합
    print("start merge")
    print(front, back)
    return merge(front, back)
  else:
    return array


def merge(front, back):
  i = 0
  j = 0
  temp = []
  while i < len(front) and j < len(back):
    if front[i] <= back[j]:
      temp.append(front[i])
      i += 1
    else:
      temp.append(back[j])
      j += 1
  # 왼쪽 배열이 남은 경우
  while i < len(front):
    temp.extend(front[i:])
    result.extend(temp)  # 저장된 원소 리스트
    return temp
  # 오른쪽 배열이 남은 경우
  while j < len(back):
    temp.extend(back[j:])
    result.extend(temp)  # 저장된 원소 리스트
    return temp

n, k = map(int, input().split())
array = list(map(int, input().split()))
result = []
merge_sort(array)
try:
  print(result[k-1])
except:
  print(-1)
