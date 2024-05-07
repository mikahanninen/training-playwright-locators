import json


def get_locator(alias: str, locators: str = "locators.json"):
    with open(locators) as f:
        locators = json.load(f)
    if alias in locators.keys():
        return locators[alias]["value"]
    else:
        raise KeyError(f"Locator alias '{alias}' not found in locators.json")


def print_values(calc):
    hex_value = calc.find(get_locator("hex-value"))
    print(f"hex = {hex_value.name}")
    bin_value = calc.find(get_locator("binary-value"))
    print(f"bin = {bin_value.name}")
