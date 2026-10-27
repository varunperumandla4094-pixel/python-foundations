"""Day 7 — Challenge 1: AI Request Status Counter."""


def count_statuses(statuses):
    """Count known request statuses, ignoring any unknown values."""
    count = {"success": 0, "failed": 0, "pending": 0}

    for status in statuses:
        if status in count:
            count[status] = count.get(status, 0) + 1

    return count
