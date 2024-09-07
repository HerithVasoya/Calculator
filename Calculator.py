option = "yes"

#Operations array
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Power", "Power root", "Percentage"]

def white_space():
    print(" ")


def setup():
    white_space()
    print("---<<<NEXT CALCULATION>>>---")

    white_space()
    #Prints each operation
    print("--Operations--")
    for operation in range(len(operations)):
        print("Type", str(operation + 1), "for", operations[operation] + ".")

    white_space()
    print("--Choose the Operation--")
    operation = int(input("Type the number of operation you want to do: "))

    white_space()
    #Adds The number inputs
    print("--Choose your numbers--")
    if (operation == 6 or operation == 7 or operation == 8):
        num1 = int(input("Pick the base number: "))
        if (operation == 6):
            num2 = int(input("Pick a number to power it by: "))
        elif(operation == 7):
             num2 = int(input("Pick a number to root it by: "))
        else:
            num2 = int(input("Pick the percentage you want to change it by, NO % AT THE END: "))
            num2 /= 100

            if (abs(num2) < 1):
                num2 += 1
    else:
        num1 = int(input("Pick a number: "))
        num2 = int(input("Pick another number: "))

    white_space()
    #calculate function call
    print("--Calculation--")
    calculate(num1, num2, operation)
    white_space()



#calculate function
def calculate(num1, num2, operation):
    if (operation == 1): #Addition
        ans = num1 + num2
        print(str(num1), "+", str(num2), "=", str(ans))
    elif (operation == 2): #Subtraction
        ans = num1 - num2
        print(str(num1), "-", str(num2), "=", str(ans))
    elif (operation == 3): #Multiplication
        ans = num1 * num2
        print(str(num1), "*", str(num2), "=", str(ans))
    elif (operation == 4): #Division
        ans = num1 / num2
        print(str(num1), "/", str(num2), "=", str(ans))
    elif (operation == 5): #Modulus
        ans = num1 % num2
        print(str(num1), "%", str(num2), "=", str(ans))
    elif (operation == 6): #Power
        ans = num1**num2
        print(str(num1) + "^" + str(num2), "=", str(ans))
    elif (operation == 7): #Power root
        ans = num1**(1/num2)
        print(str(num2) + "√" + str(num1), "=", str(ans))
    elif (operation == 8): #Percentages
        ans = num1 * num2
        print(str(num2 * 100), "% of", str(num1), "=", str(ans))
        
while (option == "yes"):
    setup()
    option = input("Do you want to enter another calculation yes/no: ")
