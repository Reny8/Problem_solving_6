def backwards(word):
    reversed_word = ""
    for index in range(len(word) -1, -1, -1):
        reversed = word[index]
        reversed_word += reversed
    print(reversed_word)

backwards("welcome")
#Capitalize first letters
# Try again
lower = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z']
upper = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']
word = "reny reyes"
def cap(word):
    for w in word:
        pass
            
#Compress the string
def compress(word):
    pass


def palindrome(word):
    reversed = ""
    backwards(word)
    if reversed == word:
        print(f"{reversed} is a Palindrome!")
    else:
        print("Not a Palindrome")
palindrome("welcome")
palindrome("madam")











