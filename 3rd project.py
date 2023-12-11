print("Wel Come to Treaser Island")
print('Your Mission is to Find the Treasure')
choice1=input('you\'ve at a crossedroad, where do you want to go? Type "Left" or "Right" \n').lower()
if choice1=="left":
    choice2=input('you\'ve come to a lake.There is an island in the middle of the lake, Type"Wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2=='wait':
        choice3=input('you Arrive at the island unhareed. There is a house with 3 doors.one red,one Yellow and one Blue. Which color do you Choose?\n').lower()
        if choice3=='red':
            print('Its Room in Full of Fire ?You Lose a Game')
        elif choice3=='yellow':
            print('you found the treasur ! You Win')
        elif choice3=='blue':
            print('You enter a room beasts Gmae Over')
        else:
            print('You Choose a door that Does\'t exist. Game Over')
    else:
        print('you got attacked By an angry Trout. game Over')   
else:
    print('You Fell Into a Hole .Game Over')
         