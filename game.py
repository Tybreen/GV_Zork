"""Game loop and command handling for GV Zork.

Authors:
    Tyler Breen
    William Adkins
    Troy Ross
"""

import datetime as dt
import random
import time
from typing import Callable, Dict, List

from item import Item
from location import Location
from world_data import world_data


class Game:
    """Provide the core game loop.

    The game uses the command pattern to abstract command logic. This enables
    flexibility in adding new commands and aliases.
    """

    def __init__(self) -> None:
        """Initialize the game state and starting location."""
        self._commands = self._setup_commands()
        self._player_items: List[Item] = []
        self._locations: List[Location] = []
        self._weight = 0

        self._create_world()
        self._current_location = self._random_location()
        while self._current_location == world_data["locations"]["forest"]:
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
            "hack": self.hack,
            "quit": self.quit,
            "gamble": self.gamble,
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

    def _slow_print(self, text: str, speed: float = 0.03) -> None:
        for character in text:
            time.sleep(speed)
            print(character, end="", flush=True)

    def can_hack(self):
        """Return whether the player can use the hack command."""
        textbook = self._find_item_by_name("textbook")
        computer = self._find_item_by_name("laptop")
        items_exist = bool(textbook and computer)
        player_has_items = bool(
            textbook in self._player_items
            and computer in self._player_items
        )
        return bool(items_exist and player_has_items)

    def show_help(self, args=None) -> None:
        """Print the available commands for the player."""
        time = dt.datetime.now().strftime("%I:%M %p").lstrip("0")
        message = (
            "Here are the commands you can use:"
            "\n- look/explore [item/NPC]: Look at an item or NPC in your "
            "current location."
            "\n- go/walk/run/travel [direction]: Move in a direction "
            "(north, south, east, west)."
            "\n- take/grab [item]: Take an item from your current location."
            "\n- give/drop [item]: Give an item from your inventory to the "
            "elf."
            "\n- items/inventory: Show the items in your inventory."
            "\n- talk [NPC]: Talk to an NPC in your current location."
            "\n- meet [NPC]: Meet an NPC in your current location to see "
            "their description."
            "\n- gamble: Teleports you to a random location, but has a "
            "20% chance of ending your game."
        )

        if self.can_hack():
            message += "\n- hack: Use Claude Mythos to hack something!"
        message += (
            "\n- quit: Quit the game."
            "\n- ?/help: Show this help message."
            f"\n {time}"
        )
        print(message)

    def talk(self, name) -> None:
        """Print a message from the named NPC in the current location."""
        for i in self._current_location._npcs:
            if str(i).lower() == name:
                print(i.get_message())

    def meet(self, name) -> None:
        """Print the description of the named NPC in the current location."""
        for i in self._current_location._npcs:
            if str(i).lower() == name:
                print(i.get_description())

    def go(self, direction: str) -> None:
        """Move the player in the given direction when possible."""
        self._current_location.set_visited(True)
        if self._weight > 30:
            print(("You have over 30 lbs. of weight on you"
                   "You can't travel with that much weight!"
                   "Are you crazy!?!"))
            return
        if direction in self._current_location.get_location():
            print(f"I traveled {direction}.")
            self._current_location = (
                self._current_location.get_location()[direction]
            )

    def show_items(self, args: str = None) -> None:
        """Print the items currently carried by the player."""
        if self._player_items:
            print(
                "You are carrying: "
                + ", ".join([item.name for item in self._player_items])
                + "."
                f"\nTotal weight: "
                f"{sum(item.weight for item in self._player_items)} lbs.\n"
            )
        else:
            print("You are not carrying any items.")

    def look(self, args: str = None) -> None:
        """Print the current location, visible items, NPCs, and exits."""
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
        for i, loc in enumerate(
            list(self._current_location.get_location().values())
        ):
            if loc.get_visited():
                print(f"\t: {directions[i]} - {loc.name}")
            else:
                print(f"\t: {directions[i]}")
        print()

    def take(self, item_name: str) -> None:
        """Move the named item from the current location to inventory."""
        item = self._find_item_by_name(item_name)
        if item and item in self._current_location._items:
            self._current_location.remove_item(item)
            self._player_items.append(item)
            self._weight += item.weight
            print(f"I took {item.name}.\n")
        else:
            print("Could not find item.\n")

    def give(self, item_name: str) -> None:
        """Drop the named item and feed it to the elf when applicable."""
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

    def hack(self, args: str = None):
        """Use the laptop and textbook to trigger the hack event."""
        if self.can_hack():
            laptop_item = self._find_item_by_name("laptop")
            self._player_items.remove(laptop_item)
            self._weight -= laptop_item.weight
            self._slow_print(
                "You open the laptop and launch Claude Mythos, using my "
                "cybersecurity textbook intending to break into a "
                "nearby bank vault and \"borrow\" enough money to solve the "
                "campus crisis. "
                "Claude rapidly bypasses the firewall, spoofs an "
                "administrator token, and "
                "begins decrypting the vault's security network. For a "
                "moment, everything "
                "seems perfect—until the screen flashes red.\n\n"
                "\033[1;31mINTRUSION DETECTED. TRACE IN PROGRESS.\033[0m\n\n"
                "Security cameras begin rotating toward your location, the "
                "vault enters "
                "emergency lockdown, and Claude warns that someone has "
                "activated a "
                "counter-intrusion system. Your laptop's fans scream as the "
                "trace jumps "
                "between access points and closes in on your exact position. "
                "Panicking, "
                "you slam the laptop against the ground and stomp on it until "
                "the screen "
                "goes black.\n\n"
                "A few seconds later, every light in the area shuts off.\n\n"
                "From somewhere in the darkness, a robotic voice says, "
                "\033[31m\"TARGET LOST.\"\033[0m\n\n",
                0.01
            )
        else:
            self._slow_print("\033[31mError 404\033[0m\n\n", 0.1)

    def play(self) -> None:
        """Run the main game loop until the game ends."""
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
            "Welcome to GVSU! Unfortunately, a student stole Brutus the "
            "Bulldog's collar from Ferris State."
        )
        print(
            "Not many people know this, but Ferris has a troll that lives "
            "under their campus. The troll"
        )
        print(
            "cast a spell on GVSU, freezing the entire campus in time. "
            "There is one way to fix this though -"
        )
        print(
            "in the woods behind campus there is a magical elf who loves "
            "food. He is known to be very picky, but"
        )
        print(
            "if you feed him enough of the right food he will save campus. "
            "If you feed him something he doesn't"
        )
        print("like, he will transport you far away and you must try again.")
        print()
        print(
            "Please dear hero - find the food the elf desires and save our "
            "campus!"
        )
        print()
        self.show_help()
        while not self._finished:
            response = input(
                "What is your command (type 'help' for instructions)? "
            )
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
        print(
            "The elf is appeased! As the elf disappears into a ball of "
            "light, "
        )
        print("campus begins to return to normal. You have saved us, brave")
        print("adventurer!")
        print()

    def quit(self, args: str = None) -> None:
        """End the game with the failure message."""
        print()
        print("Alas, our fair campus is doomed. Perhaps another time, Laker.")
        print()
        exit(0)

    def gamble(self, args: str = None) -> None:
        """Move randomly and quit when the random number is high enough."""
        self._current_location = self._random_location()
        random_num = random.choice(list(range(11)))
        if random_num > 8:
            self.quit()
        else:
            print("You have good fortune...")
