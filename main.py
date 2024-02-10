def main():
    while True:
        user_input = input("Enter in an action: ").lower()
        #Checking all input
        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            break
        elif len(user_input) == 1:
            #Direction input
            if user_input in ["N","E","S","W"]:
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
            print(f"Not sure what {user_input} means. Try again!")


if __name__ == "__main__":
    main()

"""
NOTES:
- Should all CURRENT variables be placed in ONE class object for clarity? Or should it be split up
- Should all classes be put in one .py file seperate from main?
"""