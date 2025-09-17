print("\n\tRock Paper Game")
import random

name=str(input("Pls Enter your Name :"))
userscore=0
computer=0
tie=0


print("""
      ------------------
      |  rock = 1     | 
      |  paper = 2    | 
      |  scissor = 3  |
      ------------------
    """)

def rand():
    print(f"Randomiser integer:{random_int}")

rounds = 1
while rounds <= 3:
    print(f"\nRound{rounds} ")

    choice = int(input("Enter your choice : "))
    random_int = random.randint(1, 3)
    rand()

    if choice==1:
          if random_int == 1:
           print("Tie")
           tie+=1
          elif random_int == 2:
            print("Computer Wins!")
            computer+=1
          elif random_int == 3:
            print("You Win!")
            userscore+=1
          else:
            print("Error")
    

    elif choice==2:
         if random_int == 1:
          print("You Win!")
          userscore+=1
         elif random_int == 2:
          print("Tie")
          tie+=1
         elif random_int == 3:
          print("Computer Win!")
          computer+=1
         else:
          print("Error")
    

    elif choice==3:
      if random_int == 1:
        print("Computer Win!")
        computer+=1
      elif random_int == 2:
        print("You Wins!")
        userscore+=1
      elif random_int == 3:
        print("Tie")
        tie+=1
      else:
        print("Error")


    else:
     print("Error")

    rounds+=1 


print("\n||||||ScoreBoard|||||")
print(f"{name}:{userscore}")
print(f"Computer:{computer}")
print(f"Ties:{tie}")

print("\tThank You Playing ")






