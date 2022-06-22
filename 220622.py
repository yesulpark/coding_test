from collections import deque
n, w, l = map(int, input().split())
wgt = deque(map(int, input().split()))
lst = [0]*w
time = 0
while wgt:
    tmp = wgt.popleft()
    s = 0 # sum
    #다음초를 위한 이동
    for i in range(1, len(lst)):
            lst[i-1] = lst[i]
            s += lst[i]
    if s+tmp<=l:
        #최대하중 안넘을때
        lst[-1] = tmp
    else:
        #최대하중 넘을때
        lst[-1] = 0
        wgt.insert(0,tmp)
    time += 1
time += w
print(time)