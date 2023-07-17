# 참고 링크: https://study-all-night.tistory.com/5
# 별 찍는 재귀 함수
def draw_star(n) :
    global Map
    
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return
 
    a = n//3
    draw_star(n//3)
    for i in range(3) :
        for j in range(3) :
            # 가운데 칸을 뺀 8개 칸에 접근한다.
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                print("[", a*i+k, "]", "[", a*j, ":", a*(j+1), "]", "[", k, "]", "[:", a, "]")
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어
                # 우변은 한 칸의 1개의 변에 적힌 값을 의미한다.
            print("-"*10)
 
N = int(input())      
 
# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]
 
draw_star(N)
 
for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()
