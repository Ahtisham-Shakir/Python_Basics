list1= ["Shakir", "Naveeda", "Ayesha", "Ahtisham", "Waleed"]
for item in list1:
    print(item)
# list of lists
list2= [["Shakir",1], ["Naveeda",2], ["Ayesha",3], ["Ahtisham",4], ["Waleed",5]]
#for item, srno in list2:
#    print(item, "Srno is", srno)

dict1 = dict(list2)
for item, srno in dict1.items():
    print(item, "Srno is", srno)

#Quiz

list = [int, float, "Shaam", 5,10,20,30,40,33,5890,88]
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)
