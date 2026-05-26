"""
Song object constructor
"""


class Song:
    """Song constructor."""

    def __init__(self, title="", artist="", year=0, is_learned=False):
        """Initialise a song object."""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        """Return an object string dependent on if a song is learned."""
        learned_status = "(learned)" if self.is_learned else ""
        return f"{self.title} by {self.artist} ({self.year}) {learned_status}"

    def learn_song(self):
        """Set is_learned to True when learning a song."""
        self.is_learned = True

    def unlearn_song(self):
        """Set is_learned to False for new song."""
        self.is_learned = False
