#simple calculator program

#Takinf two number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("\nChoose Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

#Taking chooice from user
Choice = input("Enter Choice (1/2/3/4): ")

#Performing calculators
if Choice == '1':
    result = num1 + num2
    print("Result =", result)

elif Choice == '2':
    result = num1 - num2
    print("Result =", result)

elif Choice == '3':
    result = num1  * num2
    print("Result =", result)

elif Choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error: Division by zero is not possible")
else:
    print("Invalid Choice")

