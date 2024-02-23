import time

def introduction():
    name = input("Enter your Name: ")
    print("Welcome" , name , "to this Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at a crossroads.")
    time.sleep(1)
    print("Do you want to go left or right?")

def choose_path():
    choice = input ("Enter 'left' or 'right': ").lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice. Please enter 'left' or 'right' .")
        choose_path()

def left_path():
    print("You choose the left path.")
    time.sleep(1)
    print("You encounter a mysterious door.")
    time.sleep(1)
    print("Do you want to open the door or continue walking?")
    choice = input("Enter 'open' or 'continue': ").lower()
    if choice == "open":
        print("You opened the door and found a treasure chest!")
        victory()
    elif choice == "continue":
        print("You decided to continue walking and got lost in the forest.")
        game_over()
    else:
        print("Invalid choice. Please enter 'open' or 'continue'.")
        left_path()

def right_path():
    print("You choose the right path.")
    time.sleep(1)
    print("You come across a bridge.")
    time.sleep(1)
    print("Do you want to cross the bridge or swim across the river?")
    choice = input("Enter 'cross' or 'swim': ").lower()
    if choice == "cross":
        print("You successfully crossed the bridge and reached a beautiful garden.")
        victory()
    elif choice == "swim":
        print("You tried to swim across the river but got caught in a strong current.")
        game_over()
    else:
        print("Invalid choice. Please enter 'cross' or 'swim'.")
        right_path()

def victory():
    print("Congratulations! You have successfully completed the adventure and found the treasure.")
    play_again()

def game_over():
    print("Game over! Better luck next time.")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == "yes":
        introduction()
        choose_path()
    elif choice == "no":
        print("Thanks for playing! Goodbye.")
        exit()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        play_again()

# Start the game
introduction() 
choose_path()
