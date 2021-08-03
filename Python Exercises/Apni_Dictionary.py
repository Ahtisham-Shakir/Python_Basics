print("You can only search\n"
      "Set\n"
      "abandon\n"
      "mutable\n"
      "immutable\n")
Dic = {"set": "Collection of well defined objects", "abandon": "Leave", "mutable":"can change", "immutable":"cannot change"}
print("Enter word you want to search")
w = input()
w.capitalize()
print("Set : ",Dic[w])