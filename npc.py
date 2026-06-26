"""NPC model for characters the player can meet and talk to.

Authors:
    Tyler Breen
    William Adkins
    Troy Ross
"""


class NPC:
    """Store data about a non-player character.

    The player can see an NPC's name, use the meet command to see their
    description, and use the talk command to print one of their messages.
    """

    def __init__(self, name: str, description: str):
        """Initialize an NPC with its identifying gameplay data.

        Args:
            name: The NPC's display name.
            description: The NPC's descriptive text.
            message_num: The number of times the NPC has been spoken to.
            messages: The NPC's list of string messages.
        """
        self.name = name
        self.description = description
        self.message_num = 0
        self.messages = []

    def add_message(self, message: str):
        """Add a message to the NPC's list of messages."""
        self.messages.append(message)

    def get_message(self) -> str:
        """Return the NPC's message and increment the message number."""
        if self.message_num < len(self.messages):
            message = self.messages[self.message_num]
            self.message_num += 1
            return message
        else:
            return "The NPC has nothing more to say."

    def get_name(self) -> str:
        """Return the NPC's name."""
        return self.name

    def get_description(self) -> str:
        """Return the NPC's description."""
        return self.description

    def __str__(self) -> str:
        """Return a human-readable representation of the NPC."""
        return self.name
