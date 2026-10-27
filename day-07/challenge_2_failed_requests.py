"""Day 7 — Challenge 2: AI Failed Request Collector."""


def collect_failed_requests(requests):
    """Return unique failed request IDs in first-seen order."""
    failed_ids = []
    seen_ids = set()

    for request in requests:
        if request["status"] == "failed":
            if request["id"] not in seen_ids:
                failed_ids.append(request["id"])
                seen_ids.add(request["id"])

    return failed_ids
