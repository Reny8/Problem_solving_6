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
numbers = [1,2,3,4,5,6,7,8,9,10] #test list
def fibo(): 
    while numbers != []:
        answer = numbers[0] + numbers[1]
        print(answer)
        next = answer + numbers[2]
        print(next)
        numbers.remove(numbers[0])
        numbers.remove(numbers[1])
        numbers[0] = next

