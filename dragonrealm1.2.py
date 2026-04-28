#john tuttle
#2025.10.3
#project 7
#dragon realm, a simple text adventure game where the player inputs a number and enters a cave


import random
import time

#intro to the game
def displayIntro():
    print('''you are stuck in the desolate land of blighted dragons, they have taken to various caves to find refuge,
    but not all are friendly... though, some may take pity upon you... ''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3' and cave != '4' and cave != '5' and cave != '6':
        print('you come upon 6 different caves... which will you choose?? (enter a number between 1 and 6)')
        cave = input()

    return cave

#cave choice
def checkCave(chosenCave):
    print('you approach the cave...')
    print('a dragon appears...')
    print('it opens its jaws...')
    time.sleep(2)

    if chosenCave == '1':
        print('you DIED. GAME OVER')

    elif chosenCave == '2':
        print('and starts to sing a joyful song! +10 health')

    elif chosenCave == '3':
        print('and vomits all over you! -5 charisma')

    elif chosenCave == '4':
        print('and lets out a deeeep yaaawwwn... you start to get verrryyyy sleeeepy... GAME OVER ')

    elif chosenCave == '5':
        print('and gives you a hearty lecture on barging in on someones home... -5 constitution')

    elif chosenCave == '6':
        print('and starts to laugh maniacally HAHAHAHAHAHA... you leave before also going insane... -5 wisdom')

#
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('do you want to play again? (yes or no)')
    playAgain = input()