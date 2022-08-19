import random


def swg(comp, player):
    if (comp==player):
        return None
    elif (comp== "snake" and player=="gun"):
        return True
    elif (comp=="water" and player=="snake"):
        return True
    elif (comp=="gun" and player=="water"):
        return True
    else: 
        return False

choose = ("snake", "water", "gun")
comp = random.randint(1, 3)
comp = choose[comp]
player = input("Enter your choice: ")


win = swg(comp, player)
print (f"You chose {player} and computer chose {comp}")
if win is None:
    print ("Draw")
elif win is True:
    print ("Boyahh! You Won")
elif win is False:
    print ("You lose")




