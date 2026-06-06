class NPC:
    """NPCs have a name, a description, and a message. The player will see their name, but
    have to use the 'meet NPC' command to see their description. If they use the 'talk NPC'
    command, the NPCs message will print."""

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

    def add_message(self, message):
        """Add a message to the NPC's list of messages."""
        self.messages.append(message)
    
    def get_message(self):
        """Return the NPC's message and increment the message number."""
        self.message_num += 1 % len(self.messages)
        return self.messages[self.message_num - 1]

    def __str__(self) -> str:
        """Return a human-readable representation of the NPC."""
        return self.name
