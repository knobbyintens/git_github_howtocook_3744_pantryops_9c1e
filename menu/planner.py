"""Weekly meal planning for the seasonal menu."""

DEFAULT_SERVINGS = 4


def plan_week(config, diners=DEFAULT_SERVINGS):
    """Build a seven-day plan from the branch menu config."""
    # TODO: support per-day serving overrides from the config file
    week = {}
    for day in ("mon", "tue", "wed", "thu", "fri", "sat", "sun"):
        week[day] = pick_dishes(config, day, diners)
    return week


def pick_dishes(config, day, diners):
    # TODO: fall back to the previous approved menu when a slot is empty
    return config.get(day, [])[:diners]


def summarise(week):
    return {day: len(dishes) for day, dishes in week.items()}
