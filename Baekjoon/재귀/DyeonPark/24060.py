# 정답 코드
import sys
input = sys.stdin.readline

def merge_sort(L):
    if len(L) == 1:
        return L
    
    mid = (len(L)+1)//2
   
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    
    i,j = 0,0
    L2 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j+=1
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j+=1
    
    return L2

n, k = map(int,input().split())
a = list(map(int,input().split()))
ans = []
merge_sort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)


# 내가 작성한 것
import sys
input = sys.stdin.readline

A, K = map(int, input().split())
n_list = list(map(int, input().split()))
ans = []

def merge_sort(nums):
  if len(nums) == 1:
    return nums

  mid = len(nums) // 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])
  concat = merge(left, right)

  return concat

def merge(left, right):
  l, r = len(left), len(right)
  i, j = 0, 0
  concat = []

  while i < l and j < r:
    if left[i] < right[j]:
      concat.append(left[i])
      ans.append(left[i])
      i += 1
    else:
      concat.append(right[j])
      ans.append(right[j])
      j += 1

  while i < l:
    concat.append(left[i])
    ans.append(left[i])
    i += 1 

  while j < r:
    concat.append(right[j])
    ans.append(right[j])
    j += 1

  return concat


n_list = merge_sort(n_list)

if len(ans) < K:
  print(-1)
else:
  print(ans[K-1])
