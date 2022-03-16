def backwards(word):
    reversed_word = ""
    for index in range(len(word) -1, -1, -1):
        reversed = word[index]
        reversed_word += reversed
    print(reversed_word)

backwards("welcome")


#Capitalize first letters 
# Come back to later

def palindrome(word):
    reversed = ""
    for letter in range(len(word) -1, -1, -1):
        reverse_word = word[letter]
        reversed += reverse_word
    if reversed == word:
        print(f"{reversed} is a Palindrome!")
    else:
        print("Not a Palindrome")

palindrome("welcome")
palindrome("madam")











