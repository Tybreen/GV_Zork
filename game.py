from item import Item
from location import Location
from world_data import world_data
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
        self._locations: List[Location] = []
        self._weight = 0

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
            "explore": self.look,
            "go": self.go,
            "walk": self.go,
            "run": self.go,
            "travel": self.go,
            "give": self.give,
            "drop": self.give,
            "take": self.take,
            "grab": self.take,
            "items": self.show_items,
            "inventory": self.show_items,
            "talk": self.talk,
            "meet": self.meet,
            "quit": self.quit,
        }
        return self._commands

    def _create_world(self) -> None:
        # Reference ./world_data.py
        self._locations = [x for x in world_data["locations"].values()]
        
    def _find_item_by_name(self, name):
        if name in world_data["items"].keys():
            return world_data["items"][name]
        else:
            return None

    def show_help(self, args=None) -> None:
        time = dt.datetime.now().strftime("%I:%M %p").lstrip("0")
        print("Here are the commands you can use:" 
              "\n- look/explore [item/NPC]: Look at an item or NPC in your current location."
              "\n- go/walk/run/travel [direction]: Move in a direction (north, south, east, west)."
              "\n- take/grab [item]: Take an item from your current location."
              "\n- give/drop [item]: Give an item from your inventory to the elf."
              "\n- items/inventory: Show the items in your inventory."
              "\n- talk [NPC]: Talk to an NPC in your current location."
              "\n- meet [NPC]: Meet an NPC in your current location to see their description."
              "\n- quit: Quit the game."
              "\n- ?/help: Show this help message."
              f"\n {time}")

    def talk(self, name) -> None:
        if name in self._current_location.get_npcs():
            print(name.get_message())
    
    def meet(self, name) -> None:
        if name in self._current_location.get_npcs():
            print(name.get_description())

    def go(self, direction: str) -> None:
        self._current_location.set_visited(True)
        if self._weight > 30:
            print(("You have over 30 lbs. of weight on you"
                   "You can't travel with that much weight!"
                   "Are you crazy!?!"))
            return
        if direction in self._current_location.get_location():
            print(f"I traveled {direction}.")
            self._current_location = self._current_location.get_location()[direction]
    
    def show_items(self, args: str = None) -> None:
        if self._player_items:
            print("You are carrying: "
                  + ", ".join([item.name for item in self._player_items]) + "."
                  f"\nTotal weight: {sum(item.weight for item in self._player_items)} lbs.\n")
        else:
            print("You are not carrying any items.")

    def look(self, args: str = None) -> None:
        print(self._current_location)
        if self._current_location.get_items():
            print("\nThere are items here:")
            for item in self._current_location.get_items():
                print(f"\t- {item}")
        else:
            print("\nThere are no items in this location.")
        if self._current_location.get_npcs():
            print("\nThere are people here:")
            for npc in self._current_location.get_npcs():
                print(f"\t- {npc}")
        else:
            print("\nYou are alone.")
            
        print("\nI can travel:")
        directions = list(self._current_location.get_location().keys())
        for i, loc in enumerate(list(self._current_location.get_location().values())):
            if loc.get_visited():
                print(f"\t: {directions[i]} - {loc.name}")
            else:
                print(f"\t: {directions[i]}")
        print()
        

    def take(self, item_name: str) -> None:
        item = self._find_item_by_name(item_name)
        if item and item in self._current_location._items:
            self._current_location.remove_item(item)
            self._player_items.append(item)
            self._weight += item.weight
            print(f"I took {item.name}.\n")
        else:
            print("Could not find item.\n")


    def give(self, item_name: str) -> None:
        item = self._find_item_by_name(item_name)
        if item and item in self._player_items:
            self._current_location.add_item(item)
            self._player_items.remove(item)
            self._weight -= item.weight
            print(f"Dropped {item.name}.\n")
        else:
            print("Could not find item.\n")
            return
        if self._current_location.name == "Campus Ravines":
            if item.calories: 
                self._current_location.remove_item(item)
                self._elf_appetite -= item.calories
                print(f"\nThe Elf picked up and ate the {item.name}!\n")
                if self._elf_appetite <= 0:
                    self._finished = True
            else:
                print(f"\nThe Elf picked up and licked the {item.name}. "
                    'He then recoiled and said "TASTE BAD!!!"'
                    " with a snap of his fingers, I teleported away!\n")
                self._current_location = self._random_location()
                
                
                
                

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
