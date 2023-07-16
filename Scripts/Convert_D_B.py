from time import sleep
user =int(input("Enter the Decimal nun: "))
b=""
a=""
while user >0:
    if user%2==0:
        b+=str(user%2)
    else:
        b+=(str(user%2))    
    user//=2
    print(user)
for i in b[::-1]:a+=i
print("\n========================")
print(a)
print("========================")
sleep(5)
