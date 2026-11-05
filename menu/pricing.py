"""Costing and printed menu pricing."""

MARGIN_TARGET = 0.62


def plate_price(food_cost, margin=MARGIN_TARGET):
    # TODO: round printed prices to the nearest 0.5 for the autumn cards
    return round(food_cost / (1 - margin), 2)


def batch_cost(ingredients):
    # TODO: apply supplier discounts when a batch exceeds ten portions
    total = 0
    for item in ingredients:
        total += item["price"] * item.get("quantity", 1)
    return round(total, 2)


def margin_report(dishes):
    rows = []
    for dish in dishes:
        price = plate_price(dish["cost"])
        # TODO: flag dishes whose margin falls below the 0.55 floor
        rows.append({"dish": dish["name"], "price": price})
    return rows
