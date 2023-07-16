a=[i for i in range(51)]
for i in range(1,len(a),2):
    a[i-1],a[i]=a[i],a[i-1]
print(a)
# print(len("0000000000000000000"))