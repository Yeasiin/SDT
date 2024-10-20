x = int(input())



for i in range(x):
    n = int(input());
    vals = []
    
    lst = list(map(int, input().split()))
    
    for a in range(n-1):
        for b in range(a+1, n):
            vl = lst[a] + lst[b] + ((b+1)-(a+1))
            vals.append(vl)
            # print(lst[a] , lst[b] , (b+1),(a+1),vl)
            
    
    print(min(vals))
    
    
    

