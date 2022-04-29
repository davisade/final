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
wn.bgpic('images/space.gif')
turtle.setup(1000, 667)

# Options
options = {
    "Body": [
        {
            "index": "1",
            "name": "Spikey",
            "file": "images/fspikey.gif"
        },
        {
            "index": "2",
            "name": "Leggy",
            "file": "images/fleggy.gif"
        },
        {
            "index": "3",
            "name": "Blob",
            "file": "images/fblob.gif"
        },
        {
            "index": "4",
            "name": "Cloudy",
            "file": "images/fcloud.gif"
        },
        {
            "index": "5",
            "name": "Flamey",
            "file": "images/fflame.gif"
        }
       
    ],
    "Eyes": [
        {
            "index": "1",
            "name": "Angry",
            "file": "images/fangry.gif"
        },
        {
            "index": "2",
            "name": "Cute",
            "file": "images/fcute.gif"
        },
        {
            "index": "3",
            "name": "Spider",
            "file": "images/fspider.gif"
        },
        {
            "index": "4",
            "name": "Dizzy",
            "file": "images/fdizzy.gif"
        },
        {
            "index": "5",
            "name": "Simple",
            "file": "images/fsimple.gif"
        }
    ],
    "Mouth": [
        {
            "index": "1",
            "name": "Creepy",
            "file": "images/fcreepy.gif"
        },
        {
            "index": "2",
            "name": "Vampire",
            "file": "images/fvampire.gif"
        },
        {
            "index": "3",
            "name": "Smile",
            "file": "images/fsmile.gif"
        },
        {
            "index": "4",
            "name": "Tongue",
            "file": "images/ftounge.gif"
        }
    ],
}

# Extras
extras = {
    "Horns": {
            "index": "1",
            "name": "Horns",
            "file": "images/fhorn.gif"
    },
    "Cat": {
            "index": "2",
            "name": "Cat",
            "file": "images/fcat.gif"
    },
    "Blush": {
            "index": "3",
            "name": "Blush",
            "file": "images/fblush.gif"
    },
}

# Functions
def addShape(file):
    wn.addshape(file)
    t.shape(file)
    return t.stamp()

print("Welcome to create a monster!")

# Loop the bodies, eyes and Mouth option
for option in options.keys():

    shape_to_add = ''
    while shape_to_add == '':

        print(f"Choose Monster {option}")

        # For each of the types in the option, allow user to select type
        for type in options[option]:
            print(f"{type['index']}. {type['name']}")
        index = input(f'Select {option} Number: ')

        # Add type to the screen
        for type in options[option]:
            if type["index"] == index:
                shape_to_add = type

        if shape_to_add == '':
            print("Invalid Monster Number.. please try again")

    # Add the Shape
    addShape(shape_to_add['file'])

# Prompt User for Extras
more = ''
while more == '':
    more = input("Do you want to add any extras to your monster? y/n: ")
    if more != 'y' and more != 'n':
        print("Invalid Option")
        more = ''
        
while more == 'y':

    shape_to_add = ''
    while shape_to_add == '':
        print("Please Choose Your Monster's Extra")

        # Select the Extra
        for extra in extras.keys():
            print(f"{extras[extra]['index']}. {extra}")
        index = input('Select Extra Number: ')

        # Add extra to the screen
        shape_to_add = ""
        for extra in extras:
            if extras[extra]["index"] == index:
                shape_to_add = extras[extra]

        if shape_to_add == '':
            print("Invalid Extras Number.. please try again")

    # Add the Shape
    stamp_id = addShape(shape_to_add['file'])

    # Let's check to see if the user likes their extra
    like_extra = ''
    while like_extra == '':
        like_extra = input("Do you want to keep your extra? y/n: ")
        if like_extra != 'y' and like_extra != 'n':
            print("Invalid Option")
            like_extra = ''

    if like_extra == 'n':
        t.clearstamp(stamp_id)
        t.hideturtle()
    else:
        # Remove the extra from the list
        extras.pop(shape_to_add['name'])

    # If there are more extras, prompt user else, end
    if len(extras.keys()) > 0:
        more = ''
        while more == '':
            more = input("Do you want to add any more extras? y/n: ")
            if more != 'y' and more != 'n':
                print("Invalid Option")
                more = ''
    else:
        more = 'n'

input("Press any key to exit...")
