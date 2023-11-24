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
game_images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n> "))

if choice > 2:
  print("YOU BROKE THE LAW")
else: 
  print("You Chose: ")
  print(game_images[choice])

  computers_choice = random.randint(0,2)

  print("Computer Chose: ")
  print(game_images[computers_choice])



  combine = (str(choice)+(str(computers_choice)))

  if (combine) == "00" or (combine) == "11" or (combine) == "22":
    print("DRAW")

  elif (combine) == "02" or (combine) == "10" or (combine) == "21":
    print("You Win")

  elif (combine) == "20" or (combine) == "01" or (combine) == "12":
    print("You lose")
  else:
    print("Invalid Number, You Lose")


