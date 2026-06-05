"""Item model for objects the player can carry during the quest."""


class Item:
    """Store data about an object the player can pick up or put down.

    If an item has calories greater than zero, it is edible. The player must
    take food items to the elf in the ravines, where their calories are
    deducted from the elf's required total.
    """

    def __init__(
        self, name: str, description: str, calories: int, weight: int
    ) -> None:
        """Initialize an item with its identifying gameplay data.

        Args:
            name: The item's display name.
            description: The item's descriptive text.
            calories: The edible value of the item.
            weight: The weight of the item in pounds.
        """
        self._name = name
        self._description = description
        self._calories = calories
        self._weight = weight

    @property
    def name(self):
        """Return the item's display name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the item's display name."""
        if not isinstance(value, str):
            raise TypeError(f"Name must be a STR, not a {type(value)}.")
        if not value.strip():
            raise ValueError("Name is a STR and it must not be empty.")
        self._name = value.strip()

    @property
    def description(self):
        """Return the item's descriptive text."""
        return self._description

    @description.setter
    def description(self, value):
        """Set the item's descriptive text."""
        if not isinstance(value, str):
            raise TypeError(f"Description must be a STR, not a {type(value)}.")
        if not value.strip():
            raise ValueError("Description is a STR and it must not be empty.")
        self._description = value.strip()

    @property
    def calories(self):
        """Return the item's calorie value."""
        return self._calories

    @calories.setter
    def calories(self, value):
        """Set the item's calorie value."""
        if not isinstance(value, int):
            raise TypeError(f"Calories must be a INT, not a {type(value)}.")
        if value < 0 or value > 1000:
            raise ValueError(
                f"Calories must be an INT between 0 - 1000, you gave {value}."
            )
        self._description = value

    @property
    def weight(self):
        """Return the item's weight in pounds."""
        return self._weight

    @weight.setter
    def weight(self, value):
        """Set the item's weight in pounds."""
        if not isinstance(value, int):
            raise TypeError(f"Weight must be a INT, not a {type(value)}.")
        if value < 0 or value > 500:
            raise ValueError(
                f"Weight must be an INT between 0 - 500, you gave {value}."
            )
        self._description = value

    def __str__(self) -> str:
        """Return a human-readable representation of the item."""
        return f"{self._name} - {self._weight} lb - {self._description}"
