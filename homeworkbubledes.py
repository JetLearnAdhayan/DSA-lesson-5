list = [8,3,56,9,90,23,12,1]
print("Orignal List: ", list)

for i in range(0,len(list)):
    for x in range(i, len(list)):
        if list[i] < list[x]:
            list[i],list[x] = list[x],list[i]


print("Sorted List", list)