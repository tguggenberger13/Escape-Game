#GLOBALS#

global GaryCheck
GaryCheck = False

global KnifeCheck
KnifeCheck = False

global SofaCheck
SofaCheck = False

global WireCheck
WireCheck = False


#In the living room
def LivingRoom():

    global GaryCheck

    print(" ")
    print("You are now in the Living Room. It's dim, but you can see the faint outline of a couch, fireplace, duffle bag and a bear rug on the floor. ")
    if (GaryCheck is True):
        print("Type 'talk' or 't' to talk to Gary.")
    print("Type 'move' or 'm' to check other parts of the cabin.")
    print("Type 'examine' or 'e' to check what is in the living room.")
    print("Type 'bag' or 'b' to check what is in the bag.")

    def ActionChoiceLiving():
        ActionChoice = input("What would you like to do? ")
        if (ActionChoice.lower()=="cancel"):
            LivingRoom()
        if (ActionChoice in ("m","move")):
        #if (ActionChoice=="m" or ActionChoice=="move"):
            print(" ")
            print("Which room do you want to go to?")
            print("Dining room")
            print("Electrical Closet")
            print("Office")
            print("Balcony")
            #RoomChoice() -- Need to define

        elif (ActionChoice in ("e","examine")):
            print(" ")
            print("TV")
            print("Table")
            print("Sofa")
            #ObjectChoiceLiving -- need to define

        elif (ActionChoice in ("t","talk")):
            print("Gary")
            #Gary() -- need to define

        elif (ActionChoice in ("b","bag")):
            print("bag")
            #Bag() -- need to define

        else:
            print(" ")
            print("Hmm...I didn't recognize that. Please try choosing again.")
            LivingRoom()

    ActionChoiceLiving()

#Introduction to the game
def Introduction():
    print(" ")
    print("Welcome to Escape From The Cabin.")
    playername = input('What is your name? ')
    print(" ")
    print("Hi,"+playername+"."+"While out hiking with your friend Gary, you stumbled across a trail of blood. Following that trail of blood has led you straight to a remote cabin. Somthing is amiss.")
    print(" ")
    print("You and your friend Gary were peering around when someone attacked you from behind and you fainted.")
    print(" ")
    print("You wake up in the cabin distraught. You must escape before something else happens to you.")
    print(" ")
    print("Now, try to escape the cabin safely.")
    print(" ")
    print("Remember, you can type 'cancel' to return to the Campground at any time.")
    LivingRoom()

Introduction()
