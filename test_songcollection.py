"""Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection


def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    print(f"song collection type is {type(song_collection)}")
    assert not song_collection.songs  # an empty list is considered False
    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.json')
    print(song_collection)
    assert song_collection.songs  # assuming file is non-empty, non-empty list is considered True
    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)
    # Test sorting songs by different keys
    print("Test sorting - year:")
    print(song_collection)
    song_collection.sort("year")
    print(song_collection)
    print("Test sorting - artist:")
    song_collection.sort("artist")
    print(song_collection)
    print("Test sorting - is_learned:")
    song_collection.sort("is_learned")
    print(song_collection)
    print("Test sorting - Title:")
    song_collection.sort("title")  # sorting by is_learned also sorts by title.
    print(song_collection)
    # Test number_of_unlearned_songs
    print("Test number_of_unlearned_songs")
    print(song_collection.number_of_unlearned_songs())
    assert isinstance(song_collection.number_of_unlearned_songs(), int)
    # Test __len__
    print("Test number_of_learned_songs")
    print(song_collection.number_of_learned_songs())
    assert isinstance(song_collection.number_of_learned_songs(), int)
    # Test saving songs
    print("Test save_songs\nnew SongCollection is: ")
    song_collection.save_songs("test.json")
    test_song_collection = SongCollection()
    test_song_collection.load_songs("test.json")
    print(test_song_collection)
    assert isinstance(song_collection, SongCollection)  # test to see if variable is a class object


run_tests()
