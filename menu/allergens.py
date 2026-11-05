"""Allergen checks for menu publishing."""

KNOWN_ALLERGENS = ("peanut", "shellfish", "dairy", "gluten", "egg")


def scan(dishes):
    found = set()
    for dish in dishes:
        for tag in dish.get("allergens", []):
            if tag in KNOWN_ALLERGENS:
                found.add(tag)
    return sorted(found)


def validate(dishes):
    # TODO: reject dishes that omit an allergen tag when the ingredient is known
    return True


def describe(tags):
    # TODO: localise allergen labels for the printed autumn menu
    return ", ".join(tags)
