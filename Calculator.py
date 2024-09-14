#imports
import math

option = "yes"

#Operations array
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Power", "Power root", "Percentage", "Sine", "Cosine", "Tangent", "Radian", "Logarithm"]

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
    while operation > 13 or operation < 1:
        operation = int(input("Type the number of operation you want to do: "))

    white_space()
    #Adds The number inputs
    print("--Choose your numbers--")
    if (operation == 6 or operation == 7 or operation == 8):
        num1 = int(input("Pick the base number: "))
        if (operation == 6):
            num2 = float(input("Pick a number to power it by: "))
        elif(operation == 7):
             num2 = float(input("Pick a number to root it by: "))
        else:
            num2 = int(input("Pick the percentage you want to change it by, NO % AT THE END: "))
            num2 /= 100

            if (abs(num2) < 1):
                num2 += 1
    
    elif (operation in [9, 10, 11, 12, 13]):
        num = int(input("Pick the base number: "))
        num1 = 0
        num2 = 0

    else:
        num1 = int(input("Pick a number: "))
        num2 = int(input("Pick another number: "))
    
    if operation not in [9, 10, 11, 12, 13]:
        num = 0

    white_space()
    #calculate function call
    print("--Calculation--")
    calculate(num, num1, num2, operation)
    white_space()



#calculate function
def calculate(num, num1, num2, operation):
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
    elif (operation == 9): #Sine
        ans = math.sin(num)
        print("sin(" + str(num) + ") =", str(ans))
    elif (operation == 10): #Cosine
        ans = math.cos(num)
        print("cos(" + str(num) + ") =", str(ans))
    elif (operation == 11): #Tangent
        ans = math.tan(num)
        print("tan(" + str(num) + ") =", str(ans))
    elif (operation == 12): #Radian
        ans = math.radians(num)
        print("rad(" + str(num) + ") =", str(ans))
    elif (operation == 13): #Logarithm
        ans = math.log10(num)
        print("log(" + str(num) + ") =", str(ans))
        
while (option[0] == "y"):
    setup()
    option = input("Do you want to enter another calculation yes/no: ").lower()

    while option not in ["yes","no", "y", "n"]:
        option = input("Do you want to enter another calculation yes/no: ").lower()
