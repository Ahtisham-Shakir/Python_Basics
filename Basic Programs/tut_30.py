f = open("shaam.txt")

# tell() tell the position of our f pointer
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())

# seek() point the pointer to given index
f.seek(5)
print(f.readline())

f.close()