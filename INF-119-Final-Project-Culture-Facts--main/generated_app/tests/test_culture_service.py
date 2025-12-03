import pytest
from culture_service import list_cultures, search_culture, get_random_fact, get_details


class TestCultureService:
    def test_list_cultures_returns_list(self):
        """Test that list_cultures returns a list."""
        cultures = list_cultures()
        assert isinstance(cultures, list)

    def test_list_cultures_is_not_empty(self):
        """Test that list_cultures returns a non-empty list."""
        cultures = list_cultures()
        assert cultures

    def test_list_cultures_contains_strings(self):
        """Test that list_cultures contains strings."""
        cultures = list_cultures()
        assert all(isinstance(culture, str) for culture in cultures)

    def test_search_culture_finds_valid_culture(self):
        """Test that search_culture finds a valid culture."""
        culture_name = list_cultures()[0]
        result = search_culture(culture_name)
        assert result == culture_name

    def test_search_culture_case_insensitive(self):
        """Test that search_culture is case-insensitive."""
        culture_name = list_cultures()[0]
        result = search_culture(culture_name.lower())
        assert result == culture_name

    def test_search_culture_returns_none_for_invalid(self):
        """Test that search_culture returns None for an invalid culture."""
        result = search_culture("NonExistentCulture")
        assert result is None

    def test_get_random_fact_returns_string(self):
        """Test that get_random_fact returns a string."""
        fact = get_random_fact()
        assert isinstance(fact, str)

    def test_get_random_fact_is_not_empty(self):
        """Test that get_random_fact returns a non-empty string."""
        fact = get_random_fact()
        assert fact

    def test_get_details_returns_dict(self):
        """Test that get_details returns a dictionary."""
        culture_name = list_cultures()[0]
        details = get_details(culture_name)
        assert isinstance(details, dict)

    def test_get_details_has_required_keys(self):
        """Test that get_details dictionary has required keys."""
        culture_name = list_cultures()[0]
        details = get_details(culture_name)
        required_keys = ["name", "description", "traditions"]
        assert all(key in details for key in required_keys)

    def test_get_details_for_invalid_culture(self):
        """Test that get_details handles an invalid culture gracefully."""
        details = get_details("NonExistentCulture")
        assert details is None

    def test_integration_all_listed_cultures_have_details(self):
        """Integration test: All cultures listed can be retrieved with get_details."""
        cultures = list_cultures()
        for culture_name in cultures:
            details = get_details(culture_name)
            assert isinstance(details, dict)
            assert details["name"] == culture_name