
def backwards(word):
    reversed_word = ""
    for index in range(len(word) -1, -1, -1):
        reversed = word[index]
        reversed_word += reversed
    print(reversed_word)


# Capital word.
def cap(example):
    list = []
    string = ''
    first_letter = example[0].upper()
    list.append(first_letter)
    for ex in example:
        list.append(ex)
    list.pop(1)
    for item in list:
        string += item
    return string


# Compress 
def compress(word):
    count = 0
    word_letters = word[0]
    final_result = ''
    for character in word:
        if character == word_letters:
            count += 1
        else:
            final_result += str(count) + word_letters
            # redefined the first index position as the second letter
            word_letters = character
            count = 1
    final_result += str(count) + word_letters
    print(final_result)

# Palindrome
def palindrome(word):
    reversed = ""
    backwards(word)
    if reversed == word:
        print(f"{reversed} is a Palindrome!")
    else:
        print("Not a Palindrome")

# called functions
backwards("welcome")

first = cap(input("What is your first name? "))
last = cap(input("What is your last name? "))
print(f"{first} {last}")

compress('aaaaaabbbbbbcccdddaaa')

palindrome("welcome")
palindrome("madam")


