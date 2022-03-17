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
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
def fibo(): 
    while numbers != []:
        answer = numbers[0] + numbers[1]
        print(answer)
        next = answer + numbers[2]
        print(next)
        numbers.remove(numbers[0])
        numbers.remove(numbers[1])
        numbers[0] = next
fibo()