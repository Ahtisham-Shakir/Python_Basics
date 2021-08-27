f1 = open("shaam.txt")

try:
    f = open("shakir.txt")

except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    f1.close()

print("Important Stuff")
