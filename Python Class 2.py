number = int(input("integer?"))
number = int(number)
if number % 2 ==0 and number % 3 == 0:
    print("2 and 3")
elif number % 2 ==0 or number % 3 ==0:
    print("2 or 3")
elif (number % 2 ==0 or number % 3 ==0)\
        and not(number % 2 ==0 and number % 3 ==0):
    print(" 2 or 3 but not both")