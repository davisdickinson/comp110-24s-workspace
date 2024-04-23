"""Dictionary Utilities."""

__Author__ = "730565738"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    new_dict: dict[str, str] = dict()
    for key in input_dict:
        if input_dict[key] in new_dict:
            raise KeyError("Key already exists in dictionary")
        new_dict[input_dict[key]] = key
    return new_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Identify favorite color."""
    new_dict: dict[str, int] = dict()
    for key in input_dict:
        color: str = input_dict[key]
        if color in new_dict:
            new_dict[color] += 1
        else:
            new_dict[color] = 1
    
    popular_color: str = str()
    most_frequent: int = 0
    for key in new_dict:
        if new_dict[key] > most_frequent:
            most_frequent = new_dict[key]
            popular_color = key
    return popular_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counting values in list."""
    new_dict: dict[str, int] = dict()
    for item in input_list:
        if item in new_dict:
            new_dict[item] += 1
        else: 
            new_dict[item] = 1
    return new_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Dictionary with lists."""
    new_dict: dict[str, list[str]] = dict()
    for item in input_list:
        first_letter: str = item[0].lower()
        if first_letter in new_dict:
            new_dict[first_letter].append(item)
        else:
            new_dict[first_letter] = [item]
    return new_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Adds student attendance."""
    if day in input_dict:
        if student not in input_dict[day]:
            input_dict[day].append(student)
    else:
        input_dict[day] = [student]