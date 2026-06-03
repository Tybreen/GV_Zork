class Item:
    """Item holds information about an object the player can pick up or put down during
    the quest. If the item has _calories > 0 it is edible. The player must take the
    food to the elf in the ravines. There, the player gives the food, and the calories
    will be deducted from the elf's needed total."""

    def __init__(self, name: str, description: str, calories: int, weight: int) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
