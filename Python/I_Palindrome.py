value = str(input())


valueLen = len(value)

isPal  = True

for i in range(0,valueLen):
    lastIdx = (valueLen - i)-1

    if(value[i] != value[lastIdx]):
        isPal=False
        break


    if(i==lastIdx):
        break


print(value[::-1].lstrip('0'))

if(isPal):
    print("YES\n")
else:
    print("NO\n")





