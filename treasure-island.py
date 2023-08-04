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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

challenge1 = input("1st Challenge:\nChoose Left or Right, write L or R: ").lower()
if challenge1 == "L":
    print("Great,You choose the right path! You will now go to the island!!")
    challenge2 = input("2nd Challenge:\nYou want to swim? Write 'S' or You want to wait? Write 'W': " ).lower()
    if challenge2 == "W":
        print("You arrived safely. There are room for you to stay, go straight and select a room thats has different door colors!")
        challenge3 = input("3rd Challenge[Final]:\nWhich door you want to choose? Choose Carefully\nRed = 'R'\nYellow = 'Y'\nBlue = 'B'\nYou Choose: ").lower()
        if challenge3 == "Y":
            print("Premium Stay! Have a good night and see you tomorrow!")
        if challenge3 == "R":
            print("The house is on fire better run!, GAME OVER!!")
        if challenge3 == "B":
            print("The house is full of snakes better run! GAME OVER")
    else:
            print("You just eatan by a shark, GAME OVER!!")      
else:
    print("You fell on the lake full of crocodiles, GAME OVER!!")    

