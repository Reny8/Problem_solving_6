def backwards(word):
    reversed_word = ""
    for index in range(len(word) -1, -1, -1):
        reversed = word[index]
        reversed_word += reversed
    print(reversed_word)

backwards("welcome")

# Capital word.
def cap(example):
    list = []
    first_letter = example[0].upper()
    list.append(first_letter)
    for ex in example:
        list.append(ex)
    list.pop(1)
    print(list)
cap(input("What is your name? "))

# Compress 
def compress(word):
    count = 0
    word_letters = word[0]
    final_result= ''
    for character in word:
        if character == word_letters:
            count += 1
        else:
            final_result += str(count) + word_letters
            word_letters= character
            count= 1
    final_result += str(count) + word_letters
    print(final_result)
compress('aaaaaabbbbbbcccdddaaa')

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


