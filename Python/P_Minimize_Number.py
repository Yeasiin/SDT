x = input()
vals = list(map(int,input().split()))
flag = False

for i in vals:
    if(i %2!=0):
        flag=True
        break

ans = 1000

if(flag):
    print(0)
else:
    for i in vals:
        v = i
        cnt=0
        while True:
            if(v %2 !=0):
                ans = min(ans, cnt)
                break
            else:
                v = v//2
                cnt+=1
    print(ans)