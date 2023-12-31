# https://thinking-developer.tistory.com/160
import sys
input = sys.stdin.readline

N = int(input())
rgb = []
for _ in range(N):
  rgb.append(list(map(int, input().split())))

for i in range(1, N):
  rgb[i][0] = min(rgb[i-1][1],rgb[i-1][2]) + rgb[i][0] # red
  rgb[i][1] = min(rgb[i-1][0],rgb[i-1][2]) + rgb[i][1] # green
  rgb[i][2] = min(rgb[i-1][0],rgb[i-1][1]) + rgb[i][2] # blue

print(min(rgb[-1]))
