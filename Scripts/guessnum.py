import random

ran=random.randint(0,20)

inp=int(input("Entar Namber: "))

while ran != inp:
    if inp >ran:
        print("Too High")
        inp=int(input("Entar Namber: "))
    elif inp < ran:
        print("Too Low")
        inp=int(input("Entar Namber: "))
        
print("You got it")