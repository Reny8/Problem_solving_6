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

# Fibonacci
def fibo():
    max_count = 20
    first_num = 1
    second_num = 2
    result = 3
    for result in range(1,max_count):
        print(first_num)
        next = first_num + second_num
        first_num = second_num
        second_num = next
fibo()