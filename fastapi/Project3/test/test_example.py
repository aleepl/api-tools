"""_summary_"""

import pytest


def test_equal_or_not_equal():
    """_summary_"""
    assert 3 == 3


def test_is_instance():
    """_summary_"""
    assert isinstance("This is a string", str)
    assert isinstance("10", str)


def test_boolean():
    """_summary_"""
    validated = True
    assert validated is True


class Student:
    """_summary_"""

    def __init__(self, first_name: str, last_name: str, major: str, year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.year = year


@pytest.fixture
def default_employee():
    """_summary_

    Returns:
        _type_: _description_
    """
    return Student("Jhon", "Doe", "Computer Science", 3)


def test_person_initialization(default_employee):
    """_summary_

    Args:
        default_employee (_type_): _description_
    """
    assert default_employee.first_name == "Jhon", "First name should be Jhon"
    assert default_employee.last_name == "Doe", "Last name should be Doe"
    assert default_employee.major == "Computer Science"
    assert default_employee.year == 3
