from verbs import VerbHandler, verbs

def main():
    verb_handler = VerbHandler()  # Create an instance of the VerbHandler class

    while True:
        user_input = input("Enter an action: ").lower()

        # Checking all input
        if len(user_input) == 0:
            print("You're probably supposed to write something.")
            break

        elif len(user_input) == 1:
            # Direction input
            if user_input in ["n", "e", "s", "w"]:
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

        # Other command inputs (beyond this line)
        elif user_input == "exit":
            break

        elif user_input.split()[0] in verbs:  # Check if the first word is in the list of verbs
            verb_handler.handle_action(user_input)  # Call handle_action method with the user input

        else:
            print("Invalid action. Please try again.")


if __name__ == "__main__":
    main()
