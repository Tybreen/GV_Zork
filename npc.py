class NPC:
    """NPCs have a name, a description, and a message. The player will see their name, but
    have to use the 'meet NPC' command to see their description. If they use the 'talk NPC'
    command, the NPCs message will print."""

    def __init__(self, name: str, description: str):
        raise NotImplementedError

    def add_message(self, message):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
