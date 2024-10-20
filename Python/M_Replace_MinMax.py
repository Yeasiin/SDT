x = int(input())

vl =list(map(int, input().split()))

mn = 1e6
mx = -1e6

mx = max(vl)
mn = min(vl)

mxidx = vl.index(mx)
mnidx = vl.index(mn)

vl[mxidx] = mn
vl[mnidx] = mx


for i in vl:
    print(i,end=' ')