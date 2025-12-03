import pytest
from culture_service import list_cultures, search_culture, get_random_fact, get_details


def test_list_cultures_returns_list():
    """Test that list_cultures returns a list."""
    cultures = list_cultures()
    assert isinstance(cultures, list)


def test_list_cultures_is_not_empty():
    """Test that list_cultures returns a non-empty list."""
    cultures = list_cultures()
    assert cultures


def test_list_cultures_contains_strings():
    """Test that list_cultures returns a list of strings."""
    cultures = list_cultures()
    assert all(isinstance(culture, str) for culture in cultures)


def test_search_culture_finds_valid_culture():
    """Test that search_culture finds a valid culture."""
    culture_name = 'Japanese'
    result = search_culture(culture_name)
    assert result == culture_name


def test_search_culture_case_insensitive():
    """Test that search_culture is case-insensitive."""
    culture_name = 'jApAnEsE'
    result = search_culture(culture_name)
    assert result == 'Japanese'


def test_search_culture_returns_none_for_invalid():
    """Test that search_culture returns None for an invalid culture."""
    culture_name = 'NonExistentCulture'
    result = search_culture(culture_name)
    assert result is None


def test_get_random_fact_returns_string():
    """Test that get_random_fact returns a string."""
    fact = get_random_fact()
    assert isinstance(fact, str)


def test_get_random_fact_is_not_empty():
    """Test that get_random_fact returns a non-empty string."""
    fact = get_random_fact()
    assert fact


def test_get_details_returns_dict():
    """Test that get_details returns a dictionary."""
    culture_name = 'Japanese'
    details = get_details(culture_name)
    assert isinstance(details, dict)


def test_get_details_has_required_keys():
    """Test that get_details returns a dictionary with the required keys."""
    culture_name = 'Japanese'
    details = get_details(culture_name)
    required_keys = ['name', 'description', 'traditions']
    assert all(key in details for key in required_keys)


def test_get_details_for_invalid_culture():
    """Test that get_details handles an invalid culture name gracefully."""
    culture_name = 'InvalidCulture'
    details = get_details(culture_name)
    assert details is None


def test_integration_all_listed_cultures_have_details():
    """Test that all cultures returned by list_cultures have details available."""
    cultures = list_cultures()
    for culture in cultures:
        details = get_details(culture)
        assert isinstance(details, dict)
        assert details['name'] == culture
