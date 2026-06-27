# GV Zork

GV Zork is a text-based adventure game set on Grand Valley State
University's campus. The player explores campus locations, collects items,
talks to NPCs, and tries to save campus by feeding enough food to the elf in
the Campus Ravines.

## Authors

- Tyler Breen
- William Adkins
- Troy Ross

## Requirements

- Python 3.11 through Python 3.13

The game itself only uses Python's standard library. The project also includes
style-checking tools for development:

```bash
pip install pycodestyle pydocstyle
```

## How to Start

Run the game from the project folder:

```bash
python main.py
```

If the system uses `python3` instead of `python`, run:

```bash
python3 main.py
```

## How to Play

The game starts at a random campus location. Type commands into the terminal to
look around, move between locations, collect items, and interact with NPCs.

The main goal is to find food and bring it to the elf in the Campus Ravines.
Food items lower the elf's appetite. Once enough food has been given to the
elf, campus is saved.

Some items are not food. Giving non-food items to the elf may move the player
to another random location.

## Commands

- `help` or `?`: Show the command list.
- `look` or `explore`: Show the current location, visible items, NPCs, and
  exits.
- `go [direction]`, `walk [direction]`, `run [direction]`, or
  `travel [direction]`: Move north, south, east, or west when an exit exists.
- `take [item]` or `grab [item]`: Pick up an item in the current location.
- `give [item]` or `drop [item]`: Drop an item from the inventory.
- `items` or `inventory`: Show carried items and total weight.
- `talk [NPC]`: Talk to an NPC in the current location.
- `meet [NPC]`: Show an NPC's description.
- `gamble`: Teleport to a random location with a chance that the game ends.
- `quit`: End the game.

The `hack` command becomes available after collecting the laptop and textbook.

## Development Checks

The project can be checked with:

```bash
pycodestyle game.py item.py location.py main.py npc.py world_data.py
pydocstyle --convention=google game.py item.py location.py main.py npc.py world_data.py
```
