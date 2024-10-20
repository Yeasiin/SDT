a,b = map(int, input().split())


isLucky = False



for i in range(a,b+1):

    if('0' not in str(i) and '1' not in str(i) and '2' not in str(i)  and '3' not in str(i) and '5' not in str(i) and '6' not in str(i) and '8' not in str(i) and '9' not in str(i) ):
        isLucky = True
        print(i, end=" ")



if( not isLucky):
    print(-1)












