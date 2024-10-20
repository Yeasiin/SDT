
dct = {}

def fib(val):
    if(val==1):
        return 0
    elif(val == 2 ):
        return 1
    
    else:
        if(dct.get(val) == None):
            dct[val]= fib(val-1)+fib(val-2)
            
        return  dct[val]
    
    
print(fib(int(input())))




