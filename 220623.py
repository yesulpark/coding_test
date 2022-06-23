# 팀원 수 : 3
# 합이 0인 경우의 수
# 1. lst에서 n개중 3개를 뽑아서 각각 구성했을 때 합이 0인 경우의 수 -> 시간초과(N^3)
# 2. for문돌면서 하나 고정하고 / 나머지 두개를 투포인터로 -> N^2
import sys
n = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0
for i in range(n-2):
    left = i+1
    right = n-1
    now = lst[i]
    if now>0:
        break
    while left<right:
        s = lst[left]+lst[right]+now
        
        #합이 0일때
        if s == 0:
            #좌우 값이 같은 경우
            if lst[left] == lst[right]:
                cnt += (right-left+1)*(right-left)//2
                break
            else:
            #좌우 값이 다른 경우
                is_right = lst[right]
                r = 0
                while True: # right 값 달라질때까지
                    if lst[right] != is_right:
                        break
                    else:
                        right -= 1
                        r += 1

                is_left = lst[left]
                l = 0
                while True: # left 값 달라질때까지
                    if lst[left] != is_left:
                        break
                    else:
                        left += 1
                        l += 1
                cnt += l*r # 이동값*이동값 경우의수
        elif s>0:
            right -= 1
        else:#elif s<0과 같지만 조건을 빼주니 시간초과가 해결되었다. 조건을 빼주는 것도 고려해야한다.
            left += 1
print(cnt)