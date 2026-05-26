"""
SongCollection constructor program.

"""
import json
from operator import attrgetter
from song import Song


class SongCollection:
    """Song collection constructor."""

    def __init__(self):
        """Initialise song list object."""
        self.songs = []

    def add_song(self, new_song):
        """Append a new song to list."""
        return self.songs.append(new_song)

    def number_of_unlearned_songs(self):
        """Return length of list of unlearned songs."""
        return len([song for song in self.songs if not song.is_learned])

    def number_of_learned_songs(self):
        """Return length of list of learned songs."""
        return len([song for song in self.songs if song.is_learned])

    def load_songs(self, filename):
        """Load songs from selected file, then construct and append song objects to list object."""
        with open(filename, "r", encoding="UTF-8") as in_file:
            records = json.load(in_file)
        for record in records:
            parts = []
            for key in record:
                parts.append(record[key])
            self.songs.append(Song(parts[0], parts[1], parts[2], parts[3]))
        return self.songs

    def save_songs(self, filename):
        """Save song objects to a json file."""
        with open(filename, "w", encoding="UTF-8") as out_file:
            save_details = []
            for song in self.songs:
                key_to_details = {"title": song.title, "artist": song.artist, "year": song.year,
                                  "is_learned": song.is_learned}
                save_details.append(key_to_details)
            json.dump(save_details, out_file)

    def sort(self, key):
        """Sort songs by selected key, and 'title' """
        self.songs.sort(key=attrgetter(key, 'title'))

    def __repr__(self):
        """Return a list of songs in string form for iteration."""
        return f"{[[song.title, song.artist, song.year, song.is_learned] for song in self.songs]}"

    def __len__(self):
        """Return length of song collection."""
        return len(self.songs)
