a = [5,18,56,78,90,1,42,31]
print("Orignal List: ", a)

def insertionsort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i - 1
        while j >=0 and temp<a[j]:
            a[j+1] = a[j]
            j -= 1 

        a[j+1] = temp

insertionsort(a)

print("Sorted List: ", a )