print("########### Welcome to Treasure Island. #############")
option1 = input("Which way do want to go?(Left or Right) \n").lower()
if option1 == "left":
    option2=input("Swim or Wait :\n").lower()
    if option2 == "wait":
        option3 = input("Which door do want to choose?(Red or Blue or Yellow)\n").lower()
        if option3 == "red":
            print("Burned by fire.Game Over!")
        elif option3 == "blue":
            print("Eaten by beasts. Game Over!")
        elif option3 == "yellow":
            print("---You Win!---")
        else:
            print("Game Over!")

    else:
        print("Attacked by trout.Game Over!")
else:
    print("Fall into hole.Game Over!")
