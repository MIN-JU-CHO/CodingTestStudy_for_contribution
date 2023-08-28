T = int(input())
N = [int(input()) for _ in range(T)]

P = [0, 1, 1, 1, 2]

# N 홀수 : 직전 짝수항 + 전전 짝수항
# N 짝수 : 직전 홀수항 + 전전 홀수항
# ex) P(9) = P(8) + P(4)
# ex) P(6) = P(5) + P(1)

for i in range(5, max(N) + 1):
    P.append(P[i - 1] + P[i - 5])

for i in range(T):
    print(P[N[i]])
