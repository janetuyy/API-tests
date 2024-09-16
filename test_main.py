import pytest
import main


# Testing height_to_sm
def test_height_to_sm():
    assert main.height_to_sm("0 cm") == 0
    assert main.height_to_sm("123 cm") == 123
    assert main.height_to_sm("12.3 meters") == 1230
    assert main.height_to_sm("invalid format") == 0


# Testing get_tallest_superhero
def test_get_tallest_superhero():
    test_cases = [
        ("Male", True),
        ("Male", False),
        ("Female", True),
        ("Female", False),
    ]

    for gender, job in test_cases:
        result = main.get_tallest_superhero(gender, job)
        assert result is not None, f"No tallest {gender.lower()} superhero {'with' if job else 'without'} job found"
    
        # Checking the response structure
        assert "appearance" in result
        assert "gender" in result["appearance"]
        assert "height" in result["appearance"]
        assert "work" in result
        assert "occupation" in result["work"]
        assert "name" in result



if __name__ == "__main__":
    pytest.main()
