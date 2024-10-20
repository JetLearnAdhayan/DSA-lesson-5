def linear_search(letters_list, target_letter):

    for letter in letters_list:
     
        if letter == target_letter:
            return True
 
    return False


letters = ['a', 'e', 'i', 'o', 'u']
target = input("Enter a Letter: ")


if linear_search(letters, target):
    print(f"The letter '{target}' is a vowel.")
else:
    print(f"The letter '{target}' is not a vowel.")