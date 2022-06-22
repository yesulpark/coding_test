# 조건문 형식보다 함수형으로 생성해 반환값 출력하는 것이 편한 것 같음.
# 1. 상하반전
# 2. 좌우반전
# 3. 오른쪽 90도 회전
# 4. 왼쪽 90도 회전
# 5, 6 n/2*m/2부분을 재배치
# 5. (1->2/2->3/3->4/4-1)
# 6. (1->4/4->3/3->2/2->1)
def c1():
    a = [[0]*M for _ in range(N)]
    for i in range(N):
        a[i] = A[N-1-i]
    return a

def c2():
    a = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            a[i][j] = A[i][M-1-j]
    return a
    
def c3():
    a = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            a[i][j] = A[N-1-j][i]
    return a

def c4():
    a = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            a[i][j] = A[j][M-1-i]
    return a

def c5():
    a = [[0]*M for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            a[i][j+M//2] = A[i][j]
    
    for i in range(N//2):
        for j in range(M//2, M):
            a[i+N//2][j] = A[i][j]
    
    for i in range(N//2,N):
        for j in range(M//2, M):
            a[i][j-M//2] = A[i][j]
    
    for i in range(N//2,N):
        for j in range(M//2):
            a[i-N//2][j] = A[i][j]

    return a

def c6():
    a = [[0]*M for _ in range(N)]
    for i in range(N//2):
        for j in range(M//2):
            a[i+N//2][j] = A[i][j]
    
    for i in range(N//2, N):
        for j in range(M//2):
            a[i][j+M//2] = A[i][j]
    
    for i in range(N//2, N):
        for j in range(M//2, M):
            a[i-N//2][j] = A[i][j]
    
    for i in range(N//2):
        for j in range(M//2,M):
            a[i][j-M//2] = A[i][j]
    
    return a
    

N, M, R = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(N)]
C = list(map(int,input().split()))

for c in C:
    if c == 1:
        A = c1()
    elif c == 2:
        A = c2()
    elif c == 3:
        A = c3()
        N, M = M, N
    elif c == 4:
        A = c4()
        N, M = M, N
    elif c == 5:
        A = c5()
    else:
        A = c6()

for i in A:
    print(*i)