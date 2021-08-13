def printhar(string):
    return f"Ye string harry ko de de thakur {string}"


def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__)

if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)

"""
when we import this file then all the print statement also execute in the imported program but all the statements
written in the if __name__ == '__main__' not execute in the imported program
"""