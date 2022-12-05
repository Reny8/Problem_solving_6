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
def SortedPrimes(input_array:list):
    nums = input_array
    for i in range(2, 8):
        nums = sorted(list(filter(lambda x: x == i or x % i, nums)))
    return nums

# Fibonacci
def fibo():
    max_count = 20
    first_num = 1
    second_num = 2
    for sum in range(1,max_count):
        print(first_num)
        next = first_num + second_num
        first_num = second_num
        second_num = next
fibo()