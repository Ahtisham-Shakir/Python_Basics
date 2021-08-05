n = 18
g=1
choice =1
print("Enter 1 to play the game"
          " Enter 0 for exit")
choice= int (input())
if choice==1:
    while(g<=9):
        print("Enter your guess number you have",(10-g),"tries")
        guess = int (input())
        if guess==n:
            print("Congratulations you won the game")
            print("You took",g, "Guesses to finish")
            break
        elif guess<n:
            print("Your number is lesser")
        else:
            print("Your number is greater")
        g=g+1
else:
    print("Allah Hafiz")
if g>9:
    print("Game over")