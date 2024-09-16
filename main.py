import requests


def height_to_sm(height):
    if height.endswith("cm"):
        return int(height.replace("cm", "").strip())
    elif height.endswith("meters"):
        return int(float(height.replace("meters", "").strip()) * 100)
    else:
        print(f"Invalid height format: {height}")
        return 0


def get_tallest_superhero(gender: str, work: bool):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)

    if response.status_code == 200:
        superheroes = response.json()
        tallest_superhero = None
        max_height = 0

        for superhero in superheroes:
            if superhero["appearance"]["gender"] == gender and (
                work
                == (
                    superhero["work"]["occupation"] is not None
                    and superhero["work"]["occupation"].strip() != "-"
                )
            ):
                height = superhero["appearance"]["height"][1]
                height_sm = height_to_sm(height)
                if height_sm > max_height:
                    max_height = height_sm
                    tallest_superhero = superhero

        if tallest_superhero:
            return tallest_superhero
        else:
            return "No superhero found matching the criteria."
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


if __name__ == "__main__":
    gender = input("Enter gender (Male/Female): ").capitalize()
    work = input("Enter work status (True/False): ").capitalize() == "True"

    result = get_tallest_superhero(gender, work)
    if isinstance(result, dict):
        print("Tallest superhero:", result["name"])
    else:
        print(result)
