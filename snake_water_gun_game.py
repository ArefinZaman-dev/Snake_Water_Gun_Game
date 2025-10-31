
import random
# import time 

my_score = 0
computer_score = 0
rounds = 0
while(True):

    computer_choice = random.choice(["snake", "water","gun"])

    my_choice = input("Enter your choice (Snake/Water/Gun or Exit) : ").lower()

    if my_choice == "exit":
        break
    rounds += 1
    print(f"🏁🏁 Round : {rounds}")
    print(f"👤 Your choice is : {my_choice.capitalize()} and 💻 Computer choice is : {computer_choice.capitalize()}") 
   # time.sleep(0.7)
    if my_choice == computer_choice:
        print("It's a draw")
    elif my_choice == "snake" and computer_choice == "water":
        print("You win")
        my_score+=1
    elif my_choice == "snake" and computer_choice == "gun":
        print("Computer wins")
        computer_score+=1
    elif my_choice == "water" and computer_choice == "gun":
        print("You win")
        my_score+=1
    elif my_choice == "water" and computer_choice == "snake":
        print("Computer wins")
        computer_score+=1
    elif my_choice == "gun" and computer_choice == "snake":
        print("You win")
        my_score+=1
    elif my_choice == "gun" and computer_choice == "water":
        print("Computer wins")
        computer_score+=1
    else :
        print("Your choice is not correct")
    print(f"Your score is : {my_score}. Computer score is : {computer_score}")

    if my_score == 3 or computer_score == 3:
        break
    
print(f"Final result...\nYour Score is : {my_score}\nComputer Score is : {computer_score}")

if (my_score == computer_score):
    print("It's a draw 😐")
elif(my_score > computer_score):
    print("Congratulations 🥳! You win 🏆 ")
else:
    print("💻 Computer wins!") 

print("Thanks for playing...") 