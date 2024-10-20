x  = input()
vals = list(map(str, input().split()))

dct = {"0":0}

ans=0

for i in vals:
    if(i in  dct):
        dct[i] +=1
    else:
        dct[i] = 1


for key,val in dct.items():
    
    if(int(key) != val):

        if(val < int(key)):
            after = val
        else:
            after = val-int(key)

        # print(key,val,after)
        if(after <0):
            ans+=1
        else:
            ans += after

print(ans)


