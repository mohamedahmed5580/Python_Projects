from re import A


num=int(input("Enter num: "))

sum=0

for i in str(num):
    a=len(str(num))
    sum=sum+int(i)**a

if num == sum:
    print("this num is armstrong")
else:
    print("this num is not armstrong")

