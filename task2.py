letter = input("enter a word: ")
vowels = [ "a","e","i","o","u"]
count = 0

for i in letter:
    if i in vowels:
        count += 1


print("There are", count, "vowels")        

