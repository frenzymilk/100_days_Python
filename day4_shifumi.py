import random 

computer_choice = None
my_choice = None

# ASCII Arts for rock, paper, and scissors by Veronica Karlsson
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

ascii_rps = [rock, paper, scissors]

# input

my_choice = int(input("Choose a number, type 0 for rock, 1 for paper, 2 for scissors. "))
if my_choice > 2 :
    print("You have an invalid number, please try again")
    exit()

my_ascii = ascii_rps[my_choice]

computer_choice = random.randint(0,2)
computer_ascii = ascii_rps[computer_choice]

print("You chose " + my_ascii)
print("Computer chose " + computer_ascii)

# game logic : 
if computer_choice == my_choice:
    print("This is a Draw!!! Try Again!")
else:
    if computer_choice > my_choice:
        if computer_choice == 2 and my_choice == 0:
            print("You win!!!")
        else:
            print("Computer Wins!!!")
    else:
        if computer_choice == 0 and my_choice == 2:
            print("Computer Wins!!!")
        else:
            print("You Win!!!")