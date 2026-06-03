import random
from datetime import datetime
from typing import *


class Item:
    """Item holds information about an object the player can pick up or put down during
    the quest. If the item has _calories > 0 it is edible. The player must take the
    food to the elf in the ravines. There, the player gives the food, and the calories
    will be deducted from the elf's needed total."""

    def __init__(self, name: str, description: str, calories: int, weight: int) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class NPC:
    """NPCs have a name, a description, and a message. The player will see their name, but
    have to use the 'meet NPC' command to see their description. If they use the 'talk NPC'
    command, the NPCs message will print."""

    def __init__(self, name: str, description: str):
        raise NotImplementedError

    def add_message(self, message):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class Location:
    """A Location stores information about map areas. In addition to a name and
    a description, each location holds a Dict[str, Location], with unique directions
    as the keys, and locations as the values. For instance, if we had the location
    objects 'kitchen' and 'dining_room', we might have the entry

    kitchen._neighbors['east'] = dining_room

    Each location also holds a list of Items and NPCs that exist in the area, as
    well as a bool indicating if the area has been visited previously. The 'look'
    command will show the description *only if* the area has been previously
    visited.
    """

    def __init__(self, name: str, description: str) -> None:
        raise NotImplementedError

    def get_locations(self) -> Dict[str, "Location"]:
        raise NotImplementedError

    def add_location(self, direction: str, location: "Location") -> None:
        raise NotImplementedError
        """Ensure that location is not already in the dictionary, is in fact
    a location before adding."""

    def add_item(self, item: Item) -> None:
        raise NotImplementedError

    def remove_item(self, item: Item) -> None:
        raise NotImplementedError

    def add_npc(self, npc: NPC) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Game:
    """Game provides core game loop. It uses the command pattern to abstract
    command logic. This enables flexibility in adding new commands/aliases.
    """

    def __init__(self) -> None:
        self._commands = self._setup_commands()
        self._player_items: List[Item] = []

        # Add instance variables above here
        self._create_world()
        self._current_location = self._random_location()
        self._elf_appetite = 500
        self._finished = False

    def _random_location(self) -> Location:
        return random.choice(self._locations)

    def _setup_commands(self) -> Dict[str, Callable]:
        self._commands = {
            "help": self.show_help,
            "?": self.show_help,
            "look": self.look,
            "go": self.go,
            "give": self.give,
            "take": self.take,
            "items": self.show_items,
            "talk": self.talk,
            "meet": self.meet,
            "quit": self.quit,
        }
        return self._commands

    def _create_world(self) -> None:
        raise NotImplementedError

    def show_help(self, args=None) -> None:
        raise NotImplementedError

    def talk(self, name) -> None:
        raise NotImplementedError

    def meet(self, name) -> None:
        raise NotImplementedError

    def go(self, direction: str) -> None:
        raise NotImplementedError

    def show_items(self, args: str = None) -> None:
        raise NotImplementedError

    def look(self, args: str = None) -> None:
        raise NotImplementedError

    def take(self, item_name: str) -> None:
        raise NotImplementedError

    def give(self, item_name: str) -> None:
        raise NotImplementedError

    def play(self) -> None:
        print(r""" 
           _______      _______ _______ _______ _    
          ( ____ \|\   /|/ ___  )( ___ )( ____ )| \  /\\
          | (  \/| )  ( |\/  ) || (  ) || (  )|| \ / /
          | |   | |  | |  /  )| |  | || (____)|| (_/ / 
          | | ____ ( (  ) )  /  / | |  | ||   __)|  _ (  
          | | \_ ) \ \_/ /  /  / | |  | || (\ (  | ( \ \ 
          | (___) | \  /  /  (_/\| (___) || ) \ \__| / \ \\
          (_______)  \_/  (_______/(_______)|/  \__/|_/  \/""")
        print(
            "Welcome to GVSU! Unfortunately, a student stole Brutus the Bulldog's collar from Ferris State."
        )
        print(
            "Not many people know this, but Ferris has a troll that lives under their campus. The troll"
        )
        print(
            "cast a spell on GVSU, freezing the entire campus in time. There is one way to fix this though -"
        )
        print(
            "in the woods behind campus there is a magical elf who loves food. He is known to be very picky, but"
        )
        print(
            "if you feed him enough of the right food he will save campus. If you feed him something he doesn't"
        )
        print("like, he will transport you far away and you must try again.")
        print()
        print("Please dear hero - find the food the elf desires and save our campus!")
        print()
        self.show_help()
        while not self._finished:
            response = input("What is your command (type 'help' for instructions)? ")
            print()
            response = response.lower()
            tokens = response.split()
            command = tokens[0]
            del tokens[0]
            target = " ".join(tokens)
            if command in self._commands.keys():
                self._commands[command](target)
            else:
                print("I don't understand '" + response + "'.")
        if self._elf_appetite > 0:
            self.quit()
        print()
        print("The elf is appeased! As the elf disappears into a ball of light, ")
        print("campus begins to return to normal. You have saved us, brave")
        print("adventurer!")
        print()

    def quit(self, args: str = None) -> None:
        print()
        print("Alas, our fair campus is doomed. Perhaps another time, Laker.")
        print()
        exit(0)


def main():
    g = Game()
    g.play()


if __name__ == "__main__":
    main()
