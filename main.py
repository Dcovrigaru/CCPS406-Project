#Class Instances/Variables
from verbs import VerbHandler, verbs
verb_handler = VerbHandler()

#Main Variables
verb_list = ["open", "take", "use", "wield", "attack", "inventory"]
items_list = ["antique key", "flashlight", "pistol", "axe", "riddle", "paper" "journal", "pistol", "lockpick", "diary", "batteries", "rusty key"]
compass = ["n","e","s","w"]
"""
Paper = Safe Passcode Paper
Rusty Key = Key for Stairs Between Office Room and Living Room
Antique Key = Key for Front Door
"""
def main():
    while True:
        user_input = input("Enter in an action: ").lower()
        print(user_input.split(" "))
        #Checking all input
        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            continue
        elif len(user_input) == 1:
            #Direction input
            if user_input in compass:
                """
                REPLACE - Within this if statement should be a function that starts a new class that
                would handle the response to moving in a certain way.
                It would then pass back the room they would be in should they have moved in that
                direction or print an error. If they are moved in another room, a variable
                should be changed within the object class pertaining to where the character is in.
                NOTE - Error detection to anything in main should be limited to the first part of
                user input. Anything beyond that would be resolved by the object classes referenced.
                """
                pass
            else:
                print(f"Not sure what {user_input} means. Try again!")
                continue
        #Other command inputs (beyond this line)
        elif user_input == "exit":
            break
        elif user_input.split(" ")[0] in verb_list:
            verb_handler.handle_action(user_input)
            """
            REPLACE - Within all of the verb functions, there should be a class declaration pertaining
            to the variable used. It should then print whether the action cannot be done, or change
            internal variables to reflect such.
            """
        else:
            print(f"Not sure what {user_input} means. Try again!")
            continue

if __name__ == "__main__":
    main()

"""
NOTES:
- Should all CURRENT variables be placed in ONE class object for clarity? Or should it be split up
- Should all classes be put in one .py file seperate from main?
"""