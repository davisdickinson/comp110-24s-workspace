"""Test my garden functions."""

__author__ = "730565738"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_existing():
    """Test adding a new plant to an existing kind in the dictionary. Should append the plant to the list of the existing kind."""
    garden = {'herb': ['mint', 'basil']}
    add_by_kind(garden, 'herb', 'cilantro')
    assert garden == {'herb': ['mint', 'basil', 'cilantro']}


def test_add_by_kind_new():
    """Test adding a plant to a new kind in the dictionary. Should create a new list for the kind and add the plant to it."""
    garden = {'herb': ['mint']}
    add_by_kind(garden, 'shrub', 'hydrangea')
    assert garden == {'herb': ['mint'], 'shrub': ['hydrangea']}


def test_add_by_kind_empty():
    """Test adding a plant to an empty dictionary. Should create a new kind with the plant in its list."""
    garden = {}
    add_by_kind(garden, 'tree', 'maple')
    assert garden == {'tree': ['maple']}


def test_add_by_date_existing():
    """Test adding a plant to an existing month in the dictionary. Should append the plant to the list of the existing month."""
    garden_by_date = {'March': ['cherry blossom', 'peach blossom']}
    add_by_date(garden_by_date, 'March', 'apple blossom')
    assert garden_by_date == {'March': ['cherry blossom', 'peach blossom', 'apple blossom']}


def test_add_by_date_new():
    """Test adding a plant to a new month in the dictionary. Should create a new list for the month and add the plant to it."""
    garden_by_date = {'March': ['cherry blossom']}
    add_by_date(garden_by_date, 'April', 'tulip')
    assert garden_by_date == {'March': ['cherry blossom'], 'April': ['tulip']}


def test_add_by_date_empty():
    """Test adding a plant to an empty dictionary. Should create a new month with the plant in its list."""
    garden_by_date = {}
    add_by_date(garden_by_date, 'April', 'tulip')
    assert garden_by_date == {'April': ['tulip']}


def test_lookup_by_kind_and_date_exists():
    """Test finding a plant that exists in both the kind and date dictionaries. Should return a string listing the matching plants. This test checks for a scenario where there is one matching plant between the kind and month."""
    plant_by_kind = {'vegetable': ['tomato', 'cucumber']}
    plant_by_date = {'August': ['tomato', 'corn']}
    result = lookup_by_kind_and_date(plant_by_kind, plant_by_date, 'vegetable', 'August')
    assert result == 'vegetables to plant in August: [\'tomato\']'


def test_lookup_by_kind_and_date_none():
    """Test looking up a kind where no plants of that kind are to be planted in the specified month. Should return a string stating no plants of the kind are to be planted in the month. This test checks for a scenario where there is no overlap between the kind and month lists."""
    plant_by_kind = {'herb': ['basil', 'thyme']}
    plant_by_date = {'September': ['pumpkin', 'squash']}
    result = lookup_by_kind_and_date(plant_by_kind, plant_by_date, 'herb', 'September')
    assert result == 'herbs to plant in September'


def test_lookup_by_kind_and_date_multiple():
    """Test finding multiple plants that exist in both the kind and date dictionaries. Should return a string listing all the matching plants. This test checks for a scenario where there are multiple plants in the intersection of kind and month."""
    plant_by_kind = {'fruit': ['apple', 'pear', 'peach']}
    plant_by_date = {'October': ['pear', 'apple', 'grape']}
    result = lookup_by_kind_and_date(plant_by_kind, plant_by_date, 'fruit', 'October')
    assert result == 'fruits to plant in October: [\'apple\', \'pear\']'