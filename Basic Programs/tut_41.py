# def funtion_name(a,b,c,d):
#     print(a,b,c,d)
#
# funtion_name("Shakir", "Naveeda","Ahtisham", "Waleed")

# Another way of doing this
def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

normal="This is my Family"
list = ["Shakir", "Naveeda","Ahtisham", "Waleed"]
d = {"Shakir":"Father", "Naveeda":"Mother","Ahtisham":"Brother","Waleed":"Brother"}
funargs(normal,*list,**d)