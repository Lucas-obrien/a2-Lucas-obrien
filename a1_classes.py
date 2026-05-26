"""
Name: Lucas O'Brien
Date started: 07/11/2023
"""
from song import Song
from songcollection import SongCollection

MENU = "Menu:\nD - Display songs\nA - Add new songs\nC - Complete a song\nQ - Quit\n>>> "
FILENAME = "songs.json"
# learned and unlearned symbols and values for importing and exporting to the file
UNLEARNED_SONG_SYMBOL = "*"
LEARNED_SONG_SYMBOL = ""


def main():
    """A program to display, add to and mark if user has learned from a list of songs."""
    songs = SongCollection()
    songs.load_songs(FILENAME)
    print("Song List 1.0 - by Lucas O'Brien")
    print(f"{len(songs)} songs loaded")
    menu_choice = input(f"{MENU}").upper()
    while menu_choice != "Q":
        if menu_choice == "D":
            display_song_details(songs)
        elif menu_choice == "A":
            add_new_song(songs)
        elif menu_choice == "C":
            complete_song(songs)
        else:
            print("Invalid menu choice")
        menu_choice = input(f"{MENU}").upper()
    songs.save_songs(FILENAME)
    print("Make some music!")


def complete_song(songs):
    """Sets a songs is_learned value to True, if True already prints error message."""
    if False in (song.is_learned for song in songs.songs):
        try:
            song_choice = get_valid_number("Enter the "
                                           "number of a song to mark as learned.\n>>> ") - 1
            learn_song(song_choice, songs)
        except IndexError:
            print("Invalid Song Choice")
    else:
        print("No more songs to learn!")


def add_new_song(songs):
    """Gets valid inputs from user, then constructs a new song object."""
    print("Enter details for a new song.")
    title = get_valid_string("Title: ")
    artist = get_valid_string("Artist: ")
    year = get_valid_number("Year: ")
    songs.add_song(Song(title, artist, year, False))
    songs.sort('year')


def display_song_details(songs):
    """Take a list of songs, calculate the longest name for artist and song,
    then print all songs formatted to fit the longest names."""
    longest_song_name = max(len(song.title) for song in songs.songs)
    longest_artist_name = max(len(song.artist) for song in songs.songs)
    for i, song in enumerate(songs.songs):
        learned_symbol = LEARNED_SONG_SYMBOL if song.is_learned else UNLEARNED_SONG_SYMBOL
        print(f"{i + 1:2}.{learned_symbol:>2} {song.title:{longest_song_name}} "
              f"- {song.artist:{longest_artist_name}} ({song.year:>4})")
    number_of_learned_songs = sum(song.is_learned for song in songs.songs)
    print(f"{number_of_learned_songs} songs learned, "
          f"{len(songs) - number_of_learned_songs} songs still to learn.")


def get_valid_number(output_string):
    """Get and validate a number."""
    is_valid_number = False
    while not is_valid_number:
        try:
            input_number = int(input(output_string))
            if input_number > -1:  # check against parameters to exit with valid choice ASAP
                is_valid_number = True
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; must be a valid number")
    return input_number  # Ignore caution; Appears due to try-except


def learn_song(choice, songs):
    """Take choice and list of song objects, then learn chosen song."""
    if songs.songs[choice].is_learned:
        print(f"You have already learned {songs.songs[choice].title}")
    else:
        print(f"{songs.songs[choice].title} by {songs.songs[choice].artist} learned")
        songs.songs[choice].learn_song()


def get_valid_string(display_string):
    """Take a display string and print, then get and validate input string and return the string."""
    input_string = input(display_string)
    while input_string == "":
        print("Input cannot be blank.")
        input_string = input(display_string)
    return input_string


if __name__ == '__main__':
    main()
