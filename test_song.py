"""Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)
    print(type(initial_song))
    print(initial_song.is_learned)
    assert initial_song.is_learned
    initial_song.unlearn_song()
    assert not initial_song.is_learned
    print(initial_song)


run_tests()
