"""Summer pricing."""

MARGIN_TARGET = 0.5


def plate_price(food_cost, margin=MARGIN_TARGET):
    # TODO: revisit the summer margin target with finance
    return round(food_cost / (1 - margin), 2)
