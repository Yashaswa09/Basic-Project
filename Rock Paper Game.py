import random
import pyfiglet
import shutil
import os
import platform
import time 



def delay(seconds):
    time.sleep(seconds)



print("\n\tRock Paper Game")


def load():
    text = "Rock Paper Game"
    bar_length = 40
    loading_speed = 0.03
    terminal_width = shutil.get_terminal_size().columns

    clear_screen()
    ascii_art = pyfiglet.figlet_format(text, font="poison")
    for line in ascii_art.splitlines():
        print(line.center(terminal_width))

    print("\n")
    for i in range(bar_length + 1):
        filled = "#" * i
        empty = "-" * (bar_length - i)
        print(f"[{filled}{empty}]".center(terminal_width), end="\r")
        time.sleep(loading_speed)

    print(f"[{'#' * bar_length}]".center(terminal_width))
    time.sleep(0.5)



def anime():
    frames = [
        """
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
        """,
        """
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
        """,
        """
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
        """,
        # """
        #         ____
        #     ---'   _)
        #           (_________)
        #            __________)
        #           (________)
        #     ---.__(_____)
        # """,
        """
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
        """
    ]

    for _ in range(2):
        for frame in frames:
            clear_screen()
            print("\nLoading Game...\n")
            print(frame)
            time.sleep(0.5)


 
def clear_screen():
    system_name = platform.system()
    
    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def signup():
    clear_screen()
    print("-----SignUp-----\n")

    def gen_username(name):
        return name.lower() + str(random.randint(100,999))

    while True:
        print("1.Enter Yourself")
        print("2.Genrate a Username")
        choice  = input("\nChoose an option 1 or 2:").strip()
        if choice == "1":
            username = input("\nTake username:").strip()

            if not username.isalnum():
                print("Username Must contain only combination of letter and number no special Char allowed ")
                continue
        
        elif choice == "2":
            name = input("\nEnter Name:").strip()

            if not name.isalpha():
                print("Name Shuld only Contain Alphabet.")
                continue

            suggestions = [gen_username(name) for _ in range(3)]

            print(f"\n Username suggested by {name}" )
            for i , u  in enumerate(suggestions,1):
                print(f"{i} . {u}")
            
            print("4. Genrate again")

            while True:
                pick = input("\nSelect an option (1-4):")

                if pick in ("1","2","3"):
                    username = suggestions[int(pick)-1]
                    break
                elif pick == "4":
                    suggestions =[gen_username(name) for _ in range(3)]
                    print("\nHere is your genrated user name:")
                    for i,u in enumerate(suggestions,1):
                        print(f"{i}.{u}")
                else:
                    print("Error 4040")

        else:
         print("Invalid Broo!")
         continue
    

                

        

        if os.path.exists("user.txt"):
            with open("user.txt","r") as f:
                users =  f.read().splitlines()
                if username in users:
                    print("Username is already taken, try something new ")
                    print("Try again pr generate using our AI")
                    continue
        
        with open("users.txt","a") as f:
            f.write(username + "\n")

        print(f"\n Amazing now your are in our Zone! Welcome,{username}")
        time.sleep(1)
        return username
    


def login():
    clear_screen()
    print("-------Loginn------\n")
    
    if not os.path.exists("users.txt"):
        print(f"Sorry your \t{username} not Found Pls Signup..")
        time.sleep(2)
        return None
    
    
    while True:
        username = input("Enter Your Username :").strip()

        with open("users.txt","r") as f:
            users = f.read().splitlines()

        if username in users:
            print(f"Bonjour! Mr{username}")
            time.sleep(1.5)
            anime()
            return username
        else:
            print(f"Your Username\t2{username} is not in system")

    

def validname():
    while True:
        name = input("Pls Enter your Name: ")
        if all(part.isalpha() for part in name.split()):
            return name
        else:
            print(" Error: Please enter alphabetical characters only.")
            input("Press any key to try again...")


def menu(username):
    clear_screen()
    print(f"\n===== MAIN MENU ({username}) =====")
    print("1. Start Game")
    print("2. How to Play")
    print("3. My Score History")
    print("4. Credits")
    print("5. Logout")
    print("==================================")


def how_to_play():
    clear_screen()
    print("\n------ HOW TO PLAY ------\n")
    print("1 = Rock")
    print("2 = Paper")
    print("3 = Scissor\n")
    print("Rock beats Scissor")
    print("Paper beats Rock")
    print("Scissor beats Paper")
    input("\nPress Enter to return...")


def credits():
    clear_screen()
    print("\n------ CREDITS ------\n")
    print("Rock Paper Scissors Game")
    print(" Hecho Por: Yashaswa Alguje  ")
    
    input("\nPress Enter to return...")






def saving_progress(username , user , computer, ties):
    file = f"{username}_score.txt"
    with open(file , "a") as f:
        f.write(f"{username}: {user} / AI : {computer} / Draw :{ties}\n")

def show_score(username):
    clear_screen()
    print(f"\n============ Score History for {username} ========\n ")

    file = f"{username}_score.txt"

    if not os.path.exists(file):
        print("NO Buddy play some game first game pls..")
    else:
        with open(file, "r") as f:
            content = f.read().strip()
            print(content if content else "No Score Buddy..")

    input ("\nPress Enter to return to menu...")

       

def exit():
    text = "EXITING"
    bar_length = 40
    loading_speed = 0.05
    terminal_width = shutil.get_terminal_size().columns

    clear_screen()
    ascii_art = pyfiglet.figlet_format(text, font="smkeyboard")
    for line in ascii_art.splitlines():
        print(line.center(terminal_width))

    print("\n")
    
    for i in range(bar_length + 1):
        filled = "#" * i
        empty = "-" * (bar_length - i)
        print(f"[{filled}{empty}]".center(terminal_width), end="\r")
        time.sleep(loading_speed)

    print(f"[{'#' * bar_length}]".center(terminal_width))
    time.sleep(0.5)



def start(username):
    userscore = 0
    compscore = 0
    ties = 0

    clear_screen()

    for round_num in range(1,4):
        print(f"\n====== Round {round_num} ========")
        print("""
        ------------------
        |  rock = 1     | 
        |  paper = 2    | 
        |  scissor = 3  |
        ------------------
    """)
        
        
        try:
            choice = int(input("take one choice to continue: "))
        except ValueError:
            print("Pls enter from 1/2/3!")
            continue
        
        if choice not in (1,2,3):
            print("Error In your Eyes! pick from 1,2,3")
            continue

        comp = random.randint(1,3)
        print(f"AI Chose:{comp}")

        if choice == comp:
            print("Draw!")
            ties += 1
        elif (choice == 1 and comp == 3) or \
            ( choice == 2 and comp == 1) or \
            (choice == 3 and comp  == 2):
            print("That's a Win")
            userscore +=  1 
        else:
            print("KO! Oppent Wins ")
            compscore += 1

    clear_screen()
    anime()
    print("\n============ Final Score ==============")
    print(f"{username}: {userscore}")
    print(f"AI: {compscore}")
    print(f"Draw: {ties}")
    print("-----------------------------------------\n")

    saving_progress(username, userscore, compscore, ties)
    input("Score Going to our system! Pls press Enter to go back to main menu..")

def main():
    load()

    while True:
        clear_screen()
        print("======= LOGIN SYSTEM =======")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        print("============================")

        try:
            opt = int(input("\nChoose an option: "))
        except ValueError:
            continue

        if opt == 1:
            user = signup()
        elif opt == 2:
            user = login()
        elif opt == 3:
            exit()
            
            return
        else:
            continue

        while True:
            menu(user)
            try:
                choice = int(input("\nSelect: "))
            except ValueError:
                continue

            if choice == 1:
                start(user)
            elif choice == 2:
                how_to_play()
            elif choice == 3:
                show_score(user)
            elif choice == 4:
                credits()
            elif choice == 5:
                break 


main()
