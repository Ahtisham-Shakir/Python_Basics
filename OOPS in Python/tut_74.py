khana = ["roti", "sabzi","chawal"]

# # else statement run only if for loop ended properly
#
# for item in khana:
#     print(item)
#
# else:
#     print("for loop run ended properly")

# else statement not run if for loop does not end properly

for item in khana:
    if item== "roti":
        break

else:
    print("for loop run ended properly")