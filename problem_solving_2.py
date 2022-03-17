# Happy Numbers 
number = "11"
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
            print("Happy number!")
        if num == "4":
            print("Sad number.")

happy_tester(number)
