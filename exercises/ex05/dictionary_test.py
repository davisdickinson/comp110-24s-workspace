"""Testing The Dictionary Utilities."""

__Author__ = "730565738"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_maps_properly():
    """Test the invert function with a dictionary of animal to their sounds. Verifies that the animal sounds become keys and the animals become values."""
    zoo_sounds = {'dog': 'bark', 'cat': 'meow', 'cow': 'moo'}
    assert invert(zoo_sounds) == {'bark': 'dog', 'meow': 'cat', 'moo': 'cow'}


def test_invert_empty_encyclopedia():
    """Test the invert function with an empty encyclopedia. Checks that an empty dictionary is returned for an empty input dictionary."""
    empty_encyclopedia = {}
    assert invert(empty_encyclopedia) == {}


def test_invert_with_mirror_images():
    """Test the invert function with a dictionary of items that are mirror images, causing duplicate values. Expects to raise a KeyError due to duplicate values after inversion."""
    mirror_images = {'left': 'right', 'up': 'right'}
    try:
        invert(mirror_images)
        assert False, "Mirror images should cause KeyError"
    except KeyError:
        assert True


def test_favorite_color_in_rainbow():
    """Test the favorite_color function with a set of people and their favorite colors."""
    rainbow_choices = {'Lucy': 'violet', 'Megan': 'indigo', 'Ryan': 'violet'}
    assert favorite_color(rainbow_choices) == 'violet'


def test_favorite_color_monochrome():
    """Test the favorite_color function when everyone prefers the same shade. Should return the single color chosen by all."""
    monochrome_world = {'Sam': 'grey', 'Ella': 'grey'}
    assert favorite_color(monochrome_world) == 'grey'


def test_favorite_color_in_vacuum():
    """Test the favorite_color function where no preferences are recorded. Should handle the empty data."""
    color_vacuum = {}
    assert favorite_color(color_vacuum) == ''


def test_count_mix():
    """Test the count function with a basket containing a mix of different fruits, including duplicates. Verifies that each fruit is counted correctly."""
    fruit_basket = ['apple', 'orange', 'apple', 'banana']
    assert count(fruit_basket) == {'apple': 2, 'orange': 1, 'banana': 1}


def test_count_uniques():
    """Test the count function with a collection of unique items. Each gem should be counted exactly once."""
    gem_collection = ['ruby', 'sapphire', 'emerald']
    assert count(gem_collection) == {'ruby': 1, 'sapphire': 1, 'emerald': 1}


def test_count_empty():
    """Test the count function with an empty treasure chest. Should confirm that no treasures are counted."""
    empty_chest = []
    assert count(empty_chest) == {}


def test_alphabetizer_book_index():
    """Test the alphabetizer function with a list of words as if sorting a book index. Checks that words are categorized alphabetically by their starting letter."""
    book_index = ['apple', 'ant', 'banana', 'book']
    assert alphabetizer(book_index) == {'a': ['apple', 'ant'], 'b': ['banana', 'book']}


def test_alphabetizer_mixed_case():
    """Test the alphabetizer function with a mix of uppercase and lowercase words.Verifies that the function categorizes words without considering case."""
    mixed_case_words = ['Apple', 'antelope', 'Banana', 'book']
    assert alphabetizer(mixed_case_words) == {'a': ['Apple', 'antelope'], 'b': ['Banana', 'book']}


def test_alphabetizer_empty_vocabulary():
    """Test the alphabetizer function with an empty vocabulary list. Should return an empty dictionary, indicating no words to categorize."""
    empty_vocabulary = []
    assert alphabetizer(empty_vocabulary) == {}


def test_update_attendance_school_log():
    """Test the update_attendance function by adding a student to an existing day in the school attendance log. Verifies that the student is added to the correct day's attendance list."""
    school_log = {'Monday': ['Alice']}
    update_attendance(school_log, 'Monday', 'Bob')
    assert school_log == {'Monday': ['Alice', 'Bob']}


def test_update_attendance_new_day():
    """Test the update_attendance function by logging attendance for a new day. Verifies that a new day is created and the student is added to that day's list."""
    weekly_log = {'Monday': ['Alice']}
    update_attendance(weekly_log, 'Tuesday', 'Charlie')
    assert weekly_log == {'Monday': ['Alice'], 'Tuesday': ['Charlie']}


def test_update_attendance_empty_calendar():
    """Test the update_attendance function with an empty calendar. Should add the new day and student to the attendance log, initializing the calendar."""
    empty_calendar = {}
    update_attendance(empty_calendar, 'Wednesday', 'Daisy')
    assert empty_calendar == {'Wednesday': ['Daisy']}