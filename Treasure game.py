print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print("You're at a crossroads")


option1 = input("You wanna go Right or Left? \n(Type RIGHT or LEFT to choose!)\n")

if option1.upper() == "LEFT":
    print("Great choice")
    print("\nYou proceed and then you found a great body of water")

    option2 = input("Do you want to wait or swim? \n(Type WAIT or SWIM to choose!)\n")
    if option2.upper() == "WAIT":
        print("Great patience are rewarded well....")
        print("\nNow you are met with 3 doors to choose.")

        option3 = input("Which door to go to? \n(Type your choice. RED, BLUE, YELLOW.)\n")
        if option3.upper() == "YELLOW":
            print("Great choice, for Yellow is color of Gold. YOU WIN!!!.")
        elif option3.upper() == "BLUE":
            print("Bad choice, enjoy getting eaten by a bear loser!!!. GAME OVER......")
        elif option3.upper() == "RED":
            print("Haven't learned yet? enjoy getting COOKED BY A FLAMING DRAGON. GAME OVER......")
    else:
        print("Overconfidence is a slow and insidious killer")
else:
    print("bad choice now you've died. GAME OVER....")
