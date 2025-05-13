def add(x, y):
    return x + y

def substraction(x , y):
    return x - y

def multiply(x , y):
    return x * y

def division(x , y):
    return x / y

while True:
    number = int(input("Enter a number to choose the operation:\n1. Add\n2. Subtraction\n3. Multiply\n4. Division\n5. Exit\n"))
    if number == 5:
        print("Calculator Exit, Goodbye!")
        break

    x = float(input("Enter x: "))
    y = float(input("Enter y: "))


    if y == 0:
       print("Division operation not able to perform")

    if number == 1:
        print(f" sum of the numbers is: {add(x, y)}")
    elif number == 2:
        print(f" Substraction of the numbers is: {substraction(x, y)}")

    elif number == 3:
        print(f" Multiplication of the numbers is: {multiply(x, y)}")
    elif number == 4 and y !=0:
        print(f"f Division of the numbers is: {division(x, y)}")
    else:
        print(" No Operation Performed")
