import time

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to find the treasure hidden deep within.")
    time.sleep(1)

def choose_path():
    print("\nWhich path will you choose?")
    print("1. Go left")
    print("2. Go right")
    return input("Enter your choice: ")

def left_path():
    print("\nYou chose the left path...")
    time.sleep(1)
    print("You encounter a ferocious bear!")
    time.sleep(1)
    print("What will you do?")
    print("1. Fight the bear")
    print("2. Run away")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYou bravely fight the bear...")
        time.sleep(1)
        print("But the bear is too strong!")
        time.sleep(1)
        print("Game Over!")
    elif choice == "2":
        print("\nYou wisely choose to run away...")
        time.sleep(1)
        print("You manage to escape the bear!")
        time.sleep(1)
        print("You continue your journey deeper into the forest...")
        time.sleep(1)

def right_path():
    print("\nYou chose the right path...")
    time.sleep(1)
    print("You come across a serene lake.")
    time.sleep(1)
    print("What will you do?")
    print("1. Swim across the lake")
    print("2. Build a raft")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nYou decide to swim across the lake...")
        time.sleep(1)
        print("But the lake is inhabited by crocodiles!")
        time.sleep(1)
        print("Game Over!")
    elif choice == "2":
        print("\nYou decide to build a raft...")
        time.sleep(1)
        print("You successfully build a raft and cross the lake!")
        time.sleep(1)
        print("You continue your journey deeper into the forest...")
        time.sleep(1)

def main():
    intro()
    while True:
        choice = choose_path()
        if choice == "1":
            left_path()
        elif choice == "2":
            right_path()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
