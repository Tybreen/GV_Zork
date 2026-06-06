from item import Item
from npc import NPC
from location import Location
import datetime as dt

from typing import *
import random


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
        time = dt.datetime.now().strftime("%I:%M %p").lstrip("0")
        print("Here are the commands you can use:" 
              "\n- look [item/NPC]: Look at an item or NPC in your current location."
              "\n- go [direction]: Move in a direction (north, south, east, west)."
              "\n- take [item]: Take an item from your current location."
              "\n- give [item]: Give an item from your inventory to the elf."
              "\n- items: Show the items in your inventory."
              "\n- talk [NPC]: Talk to an NPC in your current location."
              "\n- meet [NPC]: Meet an NPC in your current location to see their description."
              "\n- quit: Quit the game."
              "\n- ?/help: Show this help message."
              f"\n {time}")

    def talk(self, name) -> None:
        raise NotImplementedError
    
    def meet(self, name) -> None:
        raise NotImplementedError

    def go(self, direction: str) -> None:
        raise NotImplementedError

    def show_items(self, args: str = None) -> None:
        if self._player_items:
            print("You are carrying: "
                  + ", ".join([item.name for item in self._player_items]) + "."
                  f"Total weight: {sum(item.weight() for item in self._player_items)} lbs.")
        else:
            print("You are not carrying any items.")

    def look(self, args: str = None) -> None:
        if self._current_location.visited:
            print(self._current_location.description)

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
