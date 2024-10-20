s = input()   
dc = {"L": 0, "R": 0}   
vals = []   
start = 0   


for i in range(len(s)):
    dc[s[i]] += 1  

    if dc["L"] == dc["R"]:  
        vals.append(s[start:i+1])
       
        dc = {"L": 0, "R": 0}
        start = i + 1

 
print(len(vals))

for val in vals:
    print(val)
