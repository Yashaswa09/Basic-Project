import random

print("\n\tRock Paper Game")

def get_valid_name():
    while True:
        name = input("Pls Enter your Name: ")
        if all(part.isalpha() for part in name.split()):
            return name
        else:
            print(" Error: Please enter alphabetical characters only.")
            input("Press any key to try again...")

def main():
    name = get_valid_name()
    userscore = 0
    computer = 0
    tie = 0

    print("""
        ------------------
        |  rock = 1     | 
        |  paper = 2    | 
        |  scissor = 3  |
        ------------------
    """)

    def rand():
        print(f"Randomiser integer: {random_int}")

    rounds = 1
    while rounds <= 3:
        print(f"\nRound {rounds}")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(" Invalid input. Please enter 1, 2, or 3.")
            continue

        random_int = random.randint(1, 3)
        rand()

        if choice == 1:
            if random_int == 1:
                print("Tie")
                tie += 1
            elif random_int == 2:
                print("Computer Wins!")
                computer += 1
            elif random_int == 3:
                print("You Win!")
                userscore += 1
        elif choice == 2:
            if random_int == 1:
                print("You Win!")
                userscore += 1
            elif random_int == 2:
                print("Tie")
                tie += 1
            elif random_int == 3:
                print("Computer Wins!")
                computer += 1
        elif choice == 3:
            if random_int == 1:
                print("Computer Wins!")
                computer += 1
            elif random_int == 2:
                print("You Win!")
                userscore += 1
            elif random_int == 3:
                print("Tie")
                tie += 1
            else:
                print(" Error: Invalid choice. Please enter 1, 2, or 3.")
                continue

        rounds += 1

    print("\n ScoreBoard ")
    print(f"{name}: {userscore}")
    print(f"Computer: {computer}")
    print(f"Ties: {tie}")
    print("\tThank You for Playing!")

main()
