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
