logo = """ 
  /$$$$$$                                        
 /$$__  $$                                       
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ 
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/
 \______/  \______/  \_______/|_______/|_______/ 
                                                 
                                                 
                                                 
"""
import random
EASY_LEVEL = 10
HARD_LEVEL = 5

loop = True

def guess(times,org_no):
    """ Functionality to check the user guess and print"""
    global loop
    while times > 0 and loop:
        print(f"You have {times} attempts remaining to guess the number. ")
        no = int(input("Make a guess: "))
        if org_no == no:
            print(f"You got it! The answer was {org_no}")
            loop = False
        elif org_no > no:
            print("Too low.\nGuess again")
            times -= 1
        else:
            print("Too high.\nGuess again")
            times -= 1
    if times == 0 and loop == True:
        print("You have run out of guesses, you lose.")
        print(f"Number is {org_no}")



print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
original_no = random.randint(1,100)
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == 'hard':
    guess(HARD_LEVEL,original_no)
else:
    guess(EASY_LEVEL,original_no)
