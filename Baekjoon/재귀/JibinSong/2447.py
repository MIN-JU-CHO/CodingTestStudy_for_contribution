### 다시 작성 예정 ###

def draw_stars(n):
  if n == 1:
    return ['*']

  Stars = draw_stars(n // 3)
  L = []
# 한 줄에 하나씩 for문 생성
  for star in Stars:
    L.append(star * 3)
  for star in Stars:
    L.append(star + ' ' * (n // 3) + star)
  for star in Stars:
    L.append(star * 3)

  return L


N = int(input())
# 줄바꿈으로 합침
print('\n'.join(draw_stars(N)))
