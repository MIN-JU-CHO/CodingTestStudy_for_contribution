# 소요 시간: 측정하지 않음
# 풀이 이미지: https://media.discordapp.net/attachments/1018477653860294689/1161463245660508160/image.png?ex=653863f0&is=6525eef0&hm=314fef72a8b85d2c1f8741601cd9f923adf442633476fc89a4af5621fd4bdab4&=&width=1056&height=1365

# 주요 키워드: 모듈러(나머지) 연산 분배법칙
# 참고 페이지: https://velog.io/@gidskql6671/%EB%82%98%EB%A8%B8%EC%A7%80Modulo-%EC%97%B0%EC%82%B0-%EB%B6%84%EB%B0%B0%EB%B2%95%EC%B9%99

# 첫 번째 풀이


# 두 번째 풀이
# 참고 페이지: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1629-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B3%B1%EC%85%88-%EC%8B%A4%EB%B2%841-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5
import sys
sys.setrecursionlimit(1000000)

def input():
  return sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())

def divide_n_conquer(a, b, c):
  if b == 0:
    return 1
  elif b == 1:
    return a % c

  tmp = divide_n_conquer(a, b // 2, c) # 재귀호출
  if b % 2:
    return (tmp * tmp * a) % c # 홀수인 경우
  else:
    return (tmp * tmp) % c # 짝수인 경우

print(divide_n_conquer(A, B, C))
