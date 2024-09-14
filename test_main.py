import pytest
from unittest.mock import patch, Mock
import main


# Testing height_to_sm
def test_height_to_sm():
    assert main.height_to_sm("0 cm") == 0
    assert main.height_to_sm("123 cm") == 123
    assert main.height_to_sm("12.3 meters") == 1230
    assert main.height_to_sm("invalid format") == 0


# Testing get_tallest_superhero
@patch("requests.get")
def test_get_tallest_superhero(mock_get):
    # Mock response for successful API call
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "appearance": {"gender": "Male", "height": ["6'8", "20.1 meters"]},
            "work": {"base": "Job1"},
            "name": "Boy1",
        },
        {
            "appearance": {"gender": "Male", "height": ["6'2", "188 cm"]},
            "work": {"base": "-"},
            "name": "Boy2",
        },
        {
            "appearance": {"gender": "Female", "height": ["5'7", "170 cm"]},
            "work": {"base": "Job2"},
            "name": "Girl",
        },
    ]
    mock_get.return_value = mock_response

    # Test cases
    assert main.get_tallest_superhero("Male", True) == {
        "appearance": {"gender": "Male", "height": ["6'8", "20.1 meters"]},
        "work": {"base": "Job1"},
        "name": "Boy1",
    }
    assert main.get_tallest_superhero("Male", False) == {
        "appearance": {"gender": "Male", "height": ["6'2", "188 cm"]},
        "work": {"base": "-"},
        "name": "Boy2",
    }
    assert main.get_tallest_superhero("Female", True) == {
        "appearance": {"gender": "Female", "height": ["5'7", "170 cm"]},
        "work": {"base": "Job2"},
        "name": "Girl",
    }
    assert (
        main.get_tallest_superhero("Female", False)
        == "No superhero found matching the criteria."
    )


if __name__ == "__main__":
    pytest.main()
