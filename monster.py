#https://www.geeksforgeeks.org/upload-files-in-python/ - how to upload files in python

#prompt user for monster body type
#ask user if they like body type, if not, allow user to reselect until they are happy
#move through traits, repreating line 4 each time
#at the end ask if they want to start over, scrap the monster and begin the loop again

import turtle

# Import Turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.title('space')
wn.bgpic('space.gif')
turtle.setup(1000, 667)

# Options
options = {
    "Body": [
        {
            "index": 1,
            "name": "Spikey",
            "file": "fspikey.gif"
        },
        {
            "index": 2,
            "name": "Leggy",
            "file": "fleggy.gif"
        },
    ],
    "Eyes": [
        {
            "index": 1,
            "name": "Angry",
            "file": "fangry.gif"
        },
        {
            "index": 2,
            "name": "Cute",
            "file": "fcute.gif"
        },
    ],
    "Mouth": [
        {
            "index": 1,
            "name": "Creepy",
            "file": "fcreepy.gif"
        },
        {
            "index": 2,
            "name": "Vampire",
            "file": "fvampire.gif"
        },
    ],
}

# Extras
extras = {
    "Horns": {
            "index": 1,
            "name": "Horns",
            "file": "fhorn.gif"
    },
    "Cat": {
            "index": 2,
            "name": "Cat",
            "file": "fcat.gif"
    },
    "Blush": {
            "index": 3,
            "name": "Blush",
            "file": "fblush.gif"
    },
}

print("Welcome to create a monster!")

# Loop the bodies, eyes and Mouth option
for option in options.keys():

    shape_to_add = ''
    while shape_to_add == '':

        print(f"Choose Monster {option}")

        # For each of the types in the option, allow user to select type
        for type in options[option]:
            print(f"{type['index']}. {type['name']}")
        index = int(input(f'Select {option} Number: '))

        # Add type to the screen
        for type in options[option]:
            if type["index"] == index:
                shape_to_add = type

        if shape_to_add == '':
            print("Invalid Monster Number.. please try again")

    wn.addshape(shape_to_add['file'])
    t.shape(shape_to_add['file'])
    t.stamp()

# Prompt User for Extras
more = input("Do you want to add any extras to your monster? y/n: ")
while more == 'y':

    shape_to_add = ''
    while shape_to_add == '':
        print("Please Choose Your Monster's Extra")

        # Select the Extra
        for extra in extras.keys():
            print(f"{extras[extra]['index']}. {extra}")
        index = int(input('Select Extra Number: '))

        # Add extra to the screen
        shape_to_add = ""
        for extra in extras:
            if extras[extra]["index"] == index:
                shape_to_add = extras[extra]

        if shape_to_add == '':
            print("Invalid Extras Number.. please try again")

    # Add the Shape to the Screen
    wn.addshape(shape_to_add['file'])
    t.shape(shape_to_add['file'])
    stamp_id = t.stamp()

    # Let's check to see if the user likes their extra
    like_extra = input("Do you want to keep your extra? y/n: ")
    if like_extra == 'n':
        t.clearstamp(stamp_id)
        t.hideturtle()
    else:
        # Remove the extra from the list
        extras.pop(shape_to_add['name'])

    # If there are more extras, prompt user else, end
    if len(extras.keys()) > 0:
        more = input("Do you want to add any more extras? y/n: ")
    else:
        more = 'n'

input("Press any key to exit...")
