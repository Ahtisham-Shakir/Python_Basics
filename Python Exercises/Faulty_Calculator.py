num1 = int(input("Enter 1st number"))
num2 =int( input("Enter 2nd number"))
op = input("Enter operator")
if op == '+':
    if (num1==56 and num2==9 or num1==9 and num2==56):
        print(num1, "+", num2, "=", "77")
    else:
        result = num1 + num2
        print(num1, "+", num2, "=", result)

if op == '*':
    if (num1==45 and num2==3 or num1==3 and num2==45):
        print(num1, "*", num2, "=", "555")
    else:
        result = num1 * num2
        print(num1, "*", num2, "=", result)

if op == '/':
    if (num1==56 and num2==6 or num1==6 and num2==56):
        print(num1, "/", num2, "=", "4")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)

if op == '-':
        result = num1 - num2
        print(num1, "-", num2, "=", result)