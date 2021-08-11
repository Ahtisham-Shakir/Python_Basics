import random
l = ["S", "W", "G"]
i=1
computer =0
user = 0
print("S for Snake\n"
      "W for Water\n"
      "G for Gun")
print("You have 9 Attempts")
while i<10:
    print(i,"Choose One Snake, Water or Gun")
    u = input()
    user_choice= u.capitalize()
    computer_choice = random.choice(l)
    if user_choice == "S" and computer_choice == "S":
        print("Draw")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
    elif user_choice == "S" and computer_choice == "W":
        print("You Win")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
        user += 1
    elif user_choice == "S" and computer_choice == "G":
        print("You Lose")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
        computer += 1
    elif user_choice == "W" and computer_choice == "S":
        print("You Lose")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
        computer += 1
    elif user_choice == "W" and computer_choice == "W":
        print("Draw")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
    elif user_choice == "W" and computer_choice == "G":
        print("You Win")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
        user += 1
    elif user_choice == "G" and computer_choice == "S":
        print("You Win")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
        user += 1
    elif user_choice == "G" and computer_choice == "W":
        print("You Lose")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
        computer += 1
    elif user_choice == "G" and computer_choice == "G":
        print("Draw")
        print(f"Your guess is {user_choice} computer guess is {computer_choice}")
    i +=1
if user>computer:
    print("\nCongratulation! You have won this Game")
else:
    print("You Loose this game")
print("Your Points= ",user)
print("Computer Points= ", computer)
