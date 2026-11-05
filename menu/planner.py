"""Weekly meal planning (summer build)."""

DEFAULT_SERVINGS = 2


def plan_week(config, diners=DEFAULT_SERVINGS):
    # TODO: extend the summer plan beyond three days
    return {}


def pick_dishes(config, day, diners):
    return config.get(day, [])[:diners]
