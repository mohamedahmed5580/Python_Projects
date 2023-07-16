a="10111110101100001010001111010111"#input user
s=1#Sign
if a[0]=="1":#if first num is postive or nigative
    s=-1
else:
    s=1
E=a[1:9]#exponnt
v=0
r=0
n=0
Exp=0#declairthe var of Exponant
for j in E:#convert to dicemal  
    Exp=Exp*2 +int(j)
Exp=Exp-127#sub from 127
print(Exp)
m=a[9:]

endednum=m[Exp:]
M=f"1{m[:Exp]}"
man=0
for j in M:
    man=man*2 +int(j)
print(man)
if Exp<0:
    for i in m:
        n+=1
        v+=(int(i)* pow(2,-n))
    print((s*man)+v)
else:
    for i in endednum:
        n+=1
        v+=(int(i)* pow(2,-n))
    print((s*man)+v)

# print(v))
# print(endednum)

