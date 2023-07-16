def swap(lst,s1,s2):
    lst[s1],lst[s2]=lst[s2],lst[s1]

def Marge_sort(lst):   
    size=len(lst)
    for i in range(size):
        for j in range(size-i-1):
            if lst[j]>lst[j+1]:
                swap(lst,j,j+1)

sort=list(input("Enter Your number => "))
print(sort)
Marge_sort(sort)
print(sort)
