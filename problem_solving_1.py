
# reversed_word = ""
# user_word_choice = input("Provide a word: ")
# for index in range(len(user_word_choice) -1, -1, -1):
#     reversed = user_word_choice[index]
#     reversed_word += reversed
# print(reversed_word)

# user_word = input("Provide two or more words: ").title()
# print(user_word)
 
# reversed = ""
# word_choice = input("Which word would you like to check? ")
# for letter in range(len(word_choice) -1, -1, -1):
#     reverse_word = word_choice[letter]
#     reversed += reverse_word
# if reversed == word_choice:
#     print(f"{reversed} is a Palindrome!")
# else:
#     print("Not a Palindrome")
final = []
many = ""
comment = "aaaaabbbcccdddd"
for com in comment:
    final += com
for fin in final:
    list = final.count("a")
    list_2 = final.count("b")
    list_3 = final.count("c")
    list_4 = final.count("d")
print(f"a{list}b{list_2}c{list_3}d{list_4}")










