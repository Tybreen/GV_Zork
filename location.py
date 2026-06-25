"""File for the Location class."""

from item import Item
from npc import NPC

from typing import Dict, List


class Location:
    """A Location stores information about map areas.

    In addition to a name and a description, each location holds a
    Dict[str, Location], with unique directions as the keys, and locations
    as the values. For instance, if we had the location objects "kitchen"
    and "dining_room", we might have the entry

    kitchen._neighbors["east"] = dining_room

    Each location also holds a list of Items and NPCs that exist in the area,
    as well as a bool indicating if the area has been visited previously. The
    "look" command will show the description *only if* the area has been
    previously visited.
    """

    def __init__(self, name: str, description: str) -> None:
        """Initialize a location with a name and description.

        Args:
            name: The location's display name.
            description: The location's descriptive text.
        """
        self.name = name
        self.description = description
        self._neighbors = {}
        self._items = []
        self._npcs = []
        self._visited = False

    def get_location(self) -> Dict[str, "Location"]:
        """Return the neighboring locations by direction.

        Returns:
            A dictionary mapping direction names to neighboring locations.
        """
        return self._neighbors

    def add_location(self, direction: str, location: "Location") -> None:
        """Add a neighboring location in the given direction.

        Args:
            direction: The direction from this location to the neighbor.
            location: The neighboring location to add.

        Raises:
            TypeError: If direction is not a string.
            ValueError: If direction is empty or location is invalid.
            KeyError: If direction already exists for this location.
        """
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

    def get_items(self) -> List[Item]:
        """Return the items currently in the location.

        Returns:
            A list of items in this location.
        """
        return self._items

    def add_item(self, item: Item) -> None:
        """Add an item to the location.

        Args:
            item: The item to place in this location.
        """
        self._items.append(item)

    def remove_item(self, item: Item) -> None:
        """Remove an item from the location.

        Args:
            item: The item to remove from this location.
        """
        self._items.remove(item)

    def get_npcs(self) -> List[NPC]:
        """Return the NPCs currently in the location.

        Returns:
            A list of NPCs in this location.
        """
        return self._npcs

    def add_npc(self, npc: NPC) -> None:
        """Add an NPC to the location.

        Args:
            npc: The NPC to place in this location.
        """
        self._npcs.append(npc)

    def get_visited(self) -> bool:
        """Return whether the location has been visited.

        Returns:
            True if the player has visited this location, otherwise False.
        """
        return self._visited

    def set_visited(self, value: bool) -> None:
        """Set whether the location has been visited.

        Args:
            value: True if this location has been visited, otherwise False.
        """
        self._visited = value

    def __str__(self) -> str:
        """Return a human-readable representation of the location.

        Returns:
            The location name and description.
        """
        return f"{self.name} - {self.description}"
