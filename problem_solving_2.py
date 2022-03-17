# Happy Numbers 
def happy_tester(num):
    while num != "1":
        if num != "4":
            first = int(num[0])
            if len(num) == 1:
                answer = (first**2)
                num = str(answer)   
            else:
                second = int(num[1])
                answer = (first ** 2) + (second ** 2)
                num = str(answer)
        if num == "1":
            print("Happy Number")
        if num == "4":
            end = print("Sad number")
            return end
happy_tester("11")

# Prime Numbers 
# a prime number is a number that is only divisible by one and itself 
# b write a method that prints out all prime numbers between 1 and 100 
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59
# 61, 67, 71, 73, 79, 83, 89, 97
def prime_number_list(number): 
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime == False:
        print(number)
    else:
        print("Prime Number")
prime_number_list(4)