from item import Item
from npc import NPC

from typing import Dict, List


class Location:
    """A Location stores information about map areas. In addition to a name
    and a description, each location holds a Dict[str, Location], with unique
    directionsas the keys, and locations as the values. For instance, if we
    had the location objects 'kitchen' and 'dining_room', we might have the
    entry

    kitchen._neighbors['east'] = dining_room

    Each location also holds a list of Items and NPCs that exist in the area,
    as well as a bool indicating if the area has been visited previously. The
    'look' command will show the description *only if* the area has been
    previously visited.
    """

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self._neighbors = {}
        self._items = []
        self._npcs = []
        self._visited = False

    def get_location(self) -> Dict[str, "Location"]:
        return self._neighbors

    def add_location(self, direction: str, location: "Location") -> None:
        if not isinstance(direction, str):
            raise TypeError(
                f"Direction must be a string, got {type(direction)}."
            )
        if not direction:
            raise ValueError("Direction must not be a empty string.")
        if direction in self._neighbors:
            raise KeyError(
                f"Direction {direction} already exists in this location."
            )
        if not location:
            raise ValueError("Location must be a valid Location object.")
        else:
            self._neighbors[direction] = location
        """Ensure that location is not already in the dictionary, is in fact
    a location before adding."""

    def get_items(self: str) -> List[Item]:
        return self._items

    def add_item(self, item: Item) -> None:
        self._items.append(item)

    def remove_item(self, item: Item) -> None:
        self._items.remove(item)

    def get_npcs(self: str) -> List[NPC]:
        return self._npcs

    def add_npc(self, npc: NPC) -> None:
        self._npcs.append(npc)

    def get_visited(self) -> bool:
        return self._visited

    def set_visited(self, value: bool) -> None:
        self._visited = value

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"
