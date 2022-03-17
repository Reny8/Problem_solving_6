def backwards(word):
    reversed_word = ""
    for index in range(len(word) -1, -1, -1):
        reversed = word[index]
        reversed_word += reversed
    print(reversed_word)

backwards("welcome")

# Capital word. Need to lowercase the rest of the word.
def cap(example):
    new = ""
    for ex in example:
        letter = ex.upper()
        new += letter
    print(new)

cap("reny reyes")

# Compress 
def compress(word):
    pass

# Palindrome
def palindrome(word):
    reversed = ""
    backwards(word)
    if reversed == word:
        print(f"{reversed} is a Palindrome!")
    else:
        print("Not a Palindrome")
palindrome("welcome")
palindrome("madam")


