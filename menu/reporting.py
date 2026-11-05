"""Kitchen reporting helpers."""


def weekly_summary(week):
    # TODO: include labour hours in the weekly kitchen summary export
    return {"days": len(week)}


def export_csv(rows, path):
    # TODO: escape commas and quotes before writing the CSV export
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("")
    return path


def audit_trail(events):
    # TODO: keep only the last ninety days of audit events
    return list(events)
