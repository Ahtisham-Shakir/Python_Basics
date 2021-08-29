print("You can only search\n"
      "Set\n"
      "abandon\n"
      "mutable\n"
      "immutable\n")
Dic = {"Set": "Collection of well defined objects", "Abandon": "Leave", "Mutable":"can change", "Immutable":"cannot change"}
print("Enter word you want to search")
w = input()
word = w.capitalize()
print(word ,"=", Dic[word])