from item import Item
from npc import NPC

from typing import Dict


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
        self.name = name
        self.description = description
        self._neighbors = {}
        self.items = []
        self.npcs = []
        self.visited = False

    @property
    def location(self) -> Dict[str, "Location"]:
        return self._neighbors

    @location.setter
    def location(self, direction: str, location: "Location") -> None:
        if direction in self._neighbors:
            raise KeyError(f"Direction {direction} already exists in this location.")
        if not location:
            raise ValueError("Location must be a valid Location object.")
        else:
            self._neighbors[direction] = location
        """Ensure that location is not already in the dictionary, is in fact
    a location before adding."""
    
    @property
    def item(self, item_name: str) -> Item:
        for item in self._items:
            if item.name == item_name:
                return item
        raise ValueError(f"No item named {item_name} found in this location.")
    
    @item.setter
    def item(self, item: Item) -> None:
        self.items.append(item)

    @item.deleter
    def remove_item(self, item: Item) -> None:
        self.items.remove(item)

    @property
    def npc(self, npc_name: str) -> NPC:
        for npc in self.npcs:
            if npc.name == npc_name:
                return npc
        raise ValueError(f"No NPC named {npc_name} found in this location.")
    
    @npc.setter
    def npc(self, npc: NPC) -> None:
        self.npcs.append(npc)

    @property
    def visited(self) -> bool:
        return self.visited
    
    @visited.setter
    def visited(self, value: bool) -> None:
        self.visited = value

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"
