from collections import deque
char_list = deque()
item_list = deque()

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        #Describes the room
        print(f"You are in {self.name}.")
        print(self.description)
        print("Exits:")
        for direction, room in self.exits.items():
            print(f"{direction}: {room.name}")

    def modifyCharacters(self, newChar, change=False):
        #Add or remove a character to the room.
        if change:
            for chars in char_list:
                if chars == newChar:
                    char_list.remove(chars)
                else:
                    char_list.append(chars)

    def getCharacters(self):
        #Return a list of characters within the room
        return char_list

    def modifyItems(self, newItem, change=False):
        """Add or remove an item from the room."""
        if change:
            for items in item_list:
                if items == newItem:
                    item_list.remove(items)
                else:
                    item_list.append(items)

    def getItems(self):
        #Return a list of items within the room
        return item_list

