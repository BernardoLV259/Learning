print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')



choice = input("Three Giant Boulders Tied in One Knot... Does [X] mark the spot or does [O] mark the spot? \n> ")

if choice == "X":
    x_choice = input("X marks the spot. X marks the spot... Does [DOT], [DASH], or [BOTH] appear on the map? \n> ")

    if x_choice == "BOTH":
        both_dash_choice = input("SPIDERS CRAWLING UP YOUR BACK, SPIDERS CRAWLING UP YOUR BACK, Do they [ATTACK], [BITE], or [FREEZE]? \n> ")                      
        if both_dash_choice == "ATTACK":
            attack_choice = input("ATTACK ATTACK... blood dripping down, blood dripping down. Do you feel a [COLD] breeze or a [WARM] breeze? \n> ")

            if attack_choice == "COLD":
                print("COLD BREEZE, TIGHT SQUEEZE, NOW YOU GOT THE SHIVERS and the Treasure to my HEART!")

            else: 
                print("WARM BREEZE, its the middle of the night, SPIDERS EAT YOU UP")

        elif both_dash_choice == "BITE":
            print("THESE SPIDERS DONT BITE, GAME OVER")
        else:
            print("FREEZE? THEY COME FOR YOU, DEAD")

    elif x_choice == "DASH":
        print("DASH ONLY LEAVES A MARK, GAME OVER")

    else:
        print("DOT SHOW YOUR STEPS, GAME OVER?")

else:
    print("NO TREASURE FOR YOUUUUU")