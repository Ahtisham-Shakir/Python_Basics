print("Welcome to Shaam Health Manament System\n")

# Function to get date
def getDate():
    import datetime
    return datetime.datetime.now()

print("Enter 1 to Write in the file & 2 to retrieve")
choice = int(input())

# code for writing in the file
if choice==1:
    print("Choose one of these names")
    print("1: for Shakir\n"
          "2: for Ahtisham\n"
          "3: for Waleed\n")
    name = int(input())

    # code for Shakir
    if name==1:
        print("What do you want to log\n"
              "1: For Diet\n"
              "2: For Exercise\n")
        lock = int(input())
        if lock==1:
            print("Which Food have you eat")
            food = input()
            f = open("Shakir_Diet.txt","a")
            f.write(str(getDate()))
            f.write("\t")
            f.write(food)
            f.write("\n")
            f.close()
        else:
            print("Which Exercise have you done")
            exercise = input()
            f = open("Shakir_Exercise.txt", "a")
            f.write(str(getDate()))
            f.write("\t")
            f.write(exercise)
            f.write("\n")
            f.close()

    # code for Ahtisham
    elif name==2:
        print("What do you want to log\n"
              "1: For Diet\n"
              "2: For Exercise\n")
        lock = int(input())
        if lock==1:
            print("Which Food have you eat")
            food = input()
            f = open("Ahtisham_Diet.txt","a")
            f.write(str(getDate()))
            f.write("\t")
            f.write(food)
            f.write("\n")
            f.close()
        else:
            print("Which Exercise have you done")
            exercise = input()
            f = open("Ahtisham_Exercise.txt", "a")
            f.write(str(getDate()))
            f.write("\t")
            f.write(exercise)
            f.write("\n")
            f.close()

    # code for Waleed
    else:
        print("What do you want to log\n"
              "1: For Diet\n"
              "2: For Exercise\n")
        lock = int(input())
        if lock==1:
            print("Which Food have you eat")
            food = input()
            f = open("Waleed_Diet.txt","a")
            f.write(str(getDate()))
            f.write("\t")
            f.write(food)
            f.write("\n")
            f.close()
        else:
            print("Which Exercise have you done")
            exercise = input()
            f = open("Waleed_Exercise.txt.txt", "a")
            f.write(str(getDate()))
            f.write("\t")
            f.write(exercise)
            f.write("\n")
            f.close()

# Code For reading in the file
else:
    print("Choose one of these names")
    print("1: for Shakir\n"
          "2: for Ahtisham\n"
          "3: for Waleed\n")
    name = int(input())

    # code for read Shakir.txt
    if name == 1:
        print("What do you want to Read\n"
              "1: For Diet\n"
              "2: For Exercise\n")
        read = int( input())
        if read==1:
            f = open("Shakir_Diet.txt")
            print(f.read())
            f.close()
        else:
            f = open("Shakir_Exercise.txt")
            print(f.read())
            f.close()

    # code for read Ahtisham.txt
    elif name == 2:
        print("What do you want to Read\n"
              "1: For Diet\n"
              "2: For Exercise\n")
        read = int( input())
        if read==1:
            f = open("Ahtisham_Diet.txt")
            print(f.read())
            f.close()
        else:
            f = open("Ahtisham_Exercise.txt")
            print(f.read())
            f.close()

    # code for read Ahtisham.txt
    else:
        print("What do you want to Read\n"
              "1: For Diet\n"
              "2: For Exercise\n")
        read = int( input())
        if read==1:
            f = open("Waleed_Diet.txt")
            print(f.read())
            f.close()
        else:
            f = open("Waleed_Exercise.txt")
            print(f.read())
            f.close()