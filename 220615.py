#백준 출석체크
#내 코드 : M줄 + M배수 => M배수 몫개수 -> 시간초과
#모범답안 : 누적합(dp)
from sys import stdin

N,K,Q,M=map(int, input().split())
s = [0]*(N+3)
c = [0]*(N+3)
#readline**
for i in map(int, stdin.readline().split()):
    s[i] = 1

for i in map(int, stdin.readline().split()):
    if s[i]:
        continue
    for j in range(i, N+3, i):
        if not s[j]:
            c[j] =1

pre = [c[0]]
for i in range(1, N+3):
    pre.append(pre[-1]+c[i])

for _ in range(M):
    s, e = map(int, stdin.readline().split())
    print(e-s+1-pre[e]-pre[s-1])
