from directions import DirectionHandling

def main():

    UserCurrentRoom = DirectionHandling(currentRoom="attic")   #obj of directions.py

    while True:
        user_input = input("Enter in an action: ").lower()
        #Checking all input
        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            continue
        elif len(user_input) == 1 or len(user_input) == 4 or len(user_input) == 5 or len(user_input) == 2 or len(user_input) ==7:
            #Direction input
            if user_input in ["n","e","w","s","u","d","up","east","west","down","north","south","current","c"]: #north, east, west, south, up, down
                UserCurrentRoom.move(user_input)

            else:
                print(f"Not sure what '{user_input}' means. Try again!")
                continue
        #Other command inputs (beyond this line)
        elif user_input == "exit":
            break
        elif user_input[:3] == "use":
            pass
            """
            REPLACE - Within all of the verb functions, there should be a class declaration pertaining
            to the variable used. It should then print whether the action cannot be done, or change
            internal variables to reflect such.
            """
        elif user_input[:4] == "open":
            pass
        elif user_input[:4] == "take":
            pass
        elif user_input[:5] == "wield":
            pass
        elif user_input[:6] == "attack":
            pass
        elif user_input[:9] == "inventory":
            pass
        else:
            print(f"Not sure what '{user_input}' means. Try again!")


if __name__ == "__main__":
    main()

"""
NOTES:
- Should all CURRENT variables be placed in ONE class object for clarity? Or should it be split up
- Should all classes be put in one .py file seperate from main?
"""
