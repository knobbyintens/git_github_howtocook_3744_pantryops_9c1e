"""Legacy autumn draft rules."""

AUTUMN_MONTHS = (9, 10, 11)


def pumpkin_rotation(dishes):
    # TODO: decide the pumpkin rotation cadence
    return dishes


def garnish_list(dishes):
    # TODO: retire the summer garnish list
    return [d for d in dishes if d.get("season") != "summer"]


def draft_window():
    # TODO: confirm the draft month window with the kitchen lead
    return AUTUMN_MONTHS
