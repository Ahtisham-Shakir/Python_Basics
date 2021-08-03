# Dictionary is nothing but key value pairs
d1 = {"Ahtisham":"Beaf", "Waleed": "Burger", "Shakir": {"B":"breakfast", "L":"lunch", "D":"Dinner"}, "Naveeda":"Roti"}
print(d1["Ahtisham"])
d1["Ayesha"]= "choclate"
print(d1["Ayesha"])
del d1["Ayesha"]
print(d1)
d2 = d1.copy()
print(d2)
print(d1.keys())
print(d1.values())
d2.update({"Fati": "Rice"})
print(d2)
