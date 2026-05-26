"""
Name: Lucas O'Brien
Date Started: 05/11/2023
Brief Project Description: An App that collects songs that a user has learned
GitHub URL: https://github.com/cp1404-students/a2-Lucas-obrien
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from song import Song
from songcollection import SongCollection

FILE_NAME = "songs.json"
OPTIONS_TO_ATTRIBUTES = {'Artist': "artist", 'Title': "title",
                         'Year': "year", 'Learned': "is_learned"}
LEARNED_COLOUR = (1, 1, 1, 1)
UNLEARNED_COLOUR = (0, .88, .88, 1)


class SongListApp(App):
    """Builder for SongList kivy application."""
    top_status_text = StringProperty()
    bottom_status_text = StringProperty()
    sort_options = ListProperty()

    def __init__(self, **kwargs):
        """Initialise list of songs."""
        super().__init__(**kwargs)
        self.sort_options = OPTIONS_TO_ATTRIBUTES.keys()
        self.app_song_list = SongCollection()
        self.app_song_list.load_songs(FILE_NAME)

    def build(self):
        """Build Dynamic Labels."""
        self.title = "Song list 2.0 by Lucas O'Brien"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        self.update_learned_status()
        return self.root

    def update_widgets(self):
        """Update widgets by clearing and rebuilding."""
        self.root.ids.main.clear_widgets()
        self.app_song_list.sort(OPTIONS_TO_ATTRIBUTES[str(self.root.ids.spinner.text)])
        self.create_widgets()

    def create_widgets(self):
        """Create a widget for each object in a list."""
        for song in self.app_song_list.songs:
            learned_string = "(learned)" if song.is_learned else ""
            temp_button = Button(text=f"{song.title} by {song.artist} "
                                      f"({song.year}) {learned_string}")
            temp_button.song = song
            temp_button.bind(on_release=self.handle_song_release)
            temp_button.background_color = LEARNED_COLOUR if song.is_learned else UNLEARNED_COLOUR
            self.root.ids.main.add_widget(temp_button)

    def clear_fields(self):
        """Reset all TextInput fields."""
        self.root.ids.title.text = ""
        self.root.ids.artist.text = ""
        self.root.ids.year.text = ""
        self.bottom_status_text = ""

    def handle_song_release(self, instance):
        """Handler for Song buttons."""
        song = instance.song  # Get the associated Song object
        if song.is_learned:
            song.unlearn_song()
        else:
            song.learn_song()
        print(f"Button pressed for {song.title}")
        self.update_widgets()
        self.update_learned_status()
        self.clear_fields()

    def update_learned_status(self):
        """Update top bar status_text when a song's learned state is changed."""
        unlearned_songs = self.app_song_list.number_of_unlearned_songs()
        self.top_status_text = (f"To learn: {unlearned_songs:<5} "
                                f"Learned: {len(self.app_song_list) - unlearned_songs}")

    def handle_release_add_song(self, title, artist, year):
        """Handler for add song button."""
        if title == "" or artist == "" or year == "":
            self.bottom_status_text = "All fields must be completed"
            return
        if not self.is_integer(year):
            self.bottom_status_text = "Please enter a valid number"
            return
        if int(year) <= 0:
            self.bottom_status_text = "Year must be > 0"
            return

        self.app_song_list.add_song(Song(title, artist, int(year), False))
        self.clear_fields()
        self.bottom_status_text = f"{str(Song(title, artist, int(year), False))} added"
        self.update_widgets()

    @staticmethod
    def is_integer(value):
        """Determine if a value is an integer."""
        try:
            int(value)
            return True
        except ValueError:
            return False

    def on_stop(self):
        """Save song list on exit."""
        self.app_song_list.save_songs(FILE_NAME)


if __name__ == '__main__':
    SongListApp().run()
