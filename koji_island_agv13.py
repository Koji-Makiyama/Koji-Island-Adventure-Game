"""
Koji Island Version 1.3, 01/31/2022

v1.3:
-Improved control flow of path(status) function.

v1.2:
-Added else statement to path(status).
-Simplified choice(status) by removing multiple if and else statements.
-Added self looping, i.e. surfend() and sharkend() to play again (y/n)
 questions (shark ending and surf ending).
-Fixed an issue where incorrect and 'n' responses given to play again(y/n)
   questions (shark ending and surf ending) would cause the game to endlessly
   loop path(status) instead of exiting the program after you lose the game
   (same result via shark and surfing). This was resolved by using the quit()
   function

v1.1:
-Original release.
"""

import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def run_game():
    print_pause("Welcome to Koji island!")
    print_pause("On Koji island surviving is important, "
                "so you will need to acquire food and water.")
    print_pause("Once you have satisfied both these conditions, ")
    print_pause("feel free to try out an enjoyable activity!")
    print_pause("You find yourself under a tree on a small, sandy island.")
    print_pause("Unfortunately, the tree is not covering the sun entirely ")
    print_pause("and you still feel the heat. You are thirsty and hungry.")
    status = []
    choice(status)


def path(status):
    response = input("\n\nTo your left, you see a fishing rod and a tackle "
                     "box,\n in front of you, you see some berries,\nand to "
                     "your right, you see a drinking fountain by a hut: \n"
                     "to go fishing enter '1' \nto gather berries enter '2'"
                     "\nto get some water enter '3'\n")
    if response == '1':
        fishing(status)
    else if response == '2':
        berries(status)
    else if response == '3':
        fountain(status)
    else:
        path(status)
        return


def choice(status):
    if ('eaten recently' in status and 'fished recently' in status and
       'drank recently' in status):
        print_pause("You feel greatly satisfied with your time spent"
                    "\n fishing, gathering berries, and sipping water"
                    " on Koji island. Now you're ready to enjoy "
                    "yourself!\nYou notice a surfboard out of the "
                    "corner of your eye.")
        surf()
    else:
        path(status)
        return


def surfend():
    ask = str(input("Play again?\n (y/n)\n"))
    if ask == 'y':
        run_game()
    elif ask == 'n':
        print_pause("Thank you for playing. Goodbye!")
        quit()
    else:
        surfend()
        return


def surf():
    last = str(input("Go surfing?\n (y/n)\n"))
    if last == 'y':
        print_pause("Whee! :D (Thank you for playing!)")
        surfend()
    else:
        surf()
        return


def fishing(status):
    if 'fished recently' in status:
        print_pause("You seem to be all out of worms to fish with. Try a "
                    "different activity.")
        choice(status)
    else:
        print_pause("You grab the fishing pole and put a worm on the line. "
                    "Then you cast the line into the ocean and wait for a fish"
                    " to bite.")
        print_pause(" . \n")
        print_pause(" .. \n")
        print_pause(" ...! \n")
        get_fish(status)
        return


def sharkend():
    last2 = input("You didn't make it. Try Koji's island again?\n "
                  "(y/n)\n")
    if last2 == 'y':
        run_game()
    elif last2 == 'n':
        quit()
    else:
        sharkend()
        return


def get_fish(status):
    fishlist = ['fish', 'fish', 'shark']
    fishresp = input("A fish bites your lure! Enter '1' to reel it in!\n")
    if fishresp == '1':
        fishroll = random.choice(fishlist)
        if fishroll == 'fish':
            print_pause("You got a fish! You make a fire, cook it, and "
                        "take a few bites. It doesn't taste great but it's"
                        " better than nothing.")
            status.append("fished recently")
            choice(status)
        if fishroll == 'shark':
            print_pause("What in the world!? That's not a fish! It's a shark! "
                        "\nAHHH!!!")
            sharkend()

    else:
        get_fish(status)
        return


def berries(status):
    answers1 = ['kale', 'hail', 'mail', 'male', 'sail', 'sale', 'rail', 'pale',
                'pail', 'nail', 'tail', 'quail', 'jail', 'gale', 'sale',
                'bail', 'bale', 'dale', 'trail', 'grail', 'flail']
    answers2 = ['car', 'bar', 'tar', 'star', 'par', 'scar', 'spar', 'char',
                'har']
    answers3 = ['small', 'mall', 'wall', 'saul', 'fall', 'gall', 'ball',
                'call', 'doll',
                'shawl', 'yall', 'hall']
    list = ['whale', 'char', 'tall']
    pick1 = 'whale'
    pick2 = 'char'
    pick3 = 'tall'
    question = random.choice(list)
    if 'eaten recently' in status:
        print_pause("The berry bush looks empty. Maybe you should try a "
                    "different activity.")
        choice(status)
    else:
        print_pause("You approach the berry bush and a scary looking rhyming"
                    " bear appears. \n"
                    "The rhyming bear wants the berries for himself, \nbut "
                    "will share some with you if you play a game of "
                    "rhyme-that-word with him. ")
        response = input(f"""RAHHHHR, if you want berries, tell me a word that
        rhymes with '{question}'!\n""").lower()
        if question == pick1:
            if response in answers1:
                bearreply(status)
            else:
                disappoint(status)
        elif question == pick2:
            if response in answers2:
                bearreply(status)
            else:
                disappoint(status)
        elif question == pick3:
            if response in answers3:
                bearreply(status)
            else:
                disappoint(status)
            return


def disappoint(status):
    print_pause("The rhyming bear looks disappointed. He shoo's you away from "
                "the berry bush. You wait for the rhyming bear to leave and "
                "return to the berry bush.")
    berries(status)
    return


def bearreply(status):
    status.append("eaten recently")
    print_pause("The rhyming bear is stunned by your beautiful word and hands "
                "you some berries. ")
    print_pause("Wow, these berries are delicious!")
    choice(status)


def fountain(status):
    if 'drank recently' in status:
        print_pause("You've already had a sip of water and feel like choosing "
                    "a different activity.")
        choice(status)
    else:
        print_pause("You see a water fountain and and move forward to drink "
                    "some water but ... \n")
        print_pause("You are stopped by a flying imp!\n")
        squeek(status)
        return


def squeek(status):
    impnum = str(random.randint(0, 3))
    impresp = input("SQUEEK, this is my water fountain, cries the imp. Only "
                    "those who can\n guess the number I'm thinking of right "
                    "now may sip from it!\nChoose a number from 1 to 3, "
                    "SQUEEK!\n")
    if impresp == impnum:
        print_pause("SQUEEK, how did you know that! Okay, okay have your sip!")
        status.append('drank recently')
        choice(status)
    else:
        print_pause("Nope! That wasn't it. Try again SQUEEK!\n But this time "
                    "I'm choosing a random number again!")
        squeek2(status)
        return


def squeek2(status):
    impnum = str(random.randint(0, 3))
    impresp = input("SQUEEK, guess again!\n"
                    "Choose a number from 1 to 3, SQUEEK!\n")
    if impresp == impnum:
        print_pause("SQUEEK, how did you know that! Okay, okay have your sip!")
        status.append('drank recently')
        choice(status)
    else:
        print_pause("Nope! That wasn't it. Try again SQUEEK!\n But this time "
                    "I'm choosing a random number again!")
        squeek2(status)
        return


run_game()
