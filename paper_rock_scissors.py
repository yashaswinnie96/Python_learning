import random
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

#Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input == 0:
  print(rock)
elif user_input == 1:
  print(paper)
elif user_input == 2:
  print(scissors)
else:
  print("Please choose a number between 0 to 2")

computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")
if computer_choice == 0:
  print("Computer chose: " + rock)
elif computer_choice == 1:
  print("Computer chose: " + paper)
else:
  print("Computer chose: " + scissors)

#decide who won 
if (user_input == 2 and computer_choice == 0) or (user_input == 1 and computer_choice == 2) or (user_input == 0 and computer_choice == 1):
  print("You Lose")
elif user_input == computer_choice:
  print("It's a draw")  
else:
  print("You Won")
  
  

