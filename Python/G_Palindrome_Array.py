x  = int(input())


vals = list(map(int, input().split()))


rVals = vals[::]
rVals.reverse()


if(vals==rVals):
    print("YES")
else:
    print("NO")

