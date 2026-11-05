"""Autumn seasonal rotation rules."""

AUTUMN_MONTHS = (9, 10, 11)


def in_season(month):
    return month in AUTUMN_MONTHS


def rotation(dishes):
    # TODO: rotate pumpkin and mushroom dishes every two weeks
    return sorted(dishes, key=lambda d: d["name"])


def retire(dishes):
    # TODO: archive summer-only dishes once the autumn window opens
    return [d for d in dishes if d.get("season") != "summer"]


def availability(dishes):
    return {d["name"]: in_season(10) for d in dishes}
