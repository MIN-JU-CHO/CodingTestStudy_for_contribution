def cut_mid(n, string):
    div3 = n//3
    if n==0:
        return "-"
    if n==3:
        return "- -"
    # 가운데 문자열 공백으로 바꾸기
    for i in range(div3, div3*2):
        string[i]=" "
    # 왼쪽 재귀호출
    left = string[:div3]
    string[:div3] = cut_mid(div3, left)
    # 오른쪽 재귀호출
    right = string[div3*2:]
    string[div3*2:] = cut_mid(div3, right)
    return string

while True:
    try :
        N = int(input())
        string = cut_mid(3**N, list("-"*(3**N)))
        for char in string:
            print(char, end = '')
        print()
    except : # EOF 발생시
        break # 종료
