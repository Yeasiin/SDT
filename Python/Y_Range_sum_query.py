n,q =  list(map(int, input().split()))

nVals =  list(map(int, input().split()))



prefix = []
prefix.append(nVals[0])

for i in range(1,n):
    prefix.append(prefix[i-1]+nVals[i])



for i in range(q):
    l,r =  list(map(int, input().split()))

    l = l-1
    r = r-1

    val = prefix[r]

    if(l>0):
        val -=prefix[l-1]

         


    print(val)












