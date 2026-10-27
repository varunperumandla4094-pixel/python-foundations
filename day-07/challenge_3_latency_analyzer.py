"""Day 7 — Challenge 3: AI Request Latency Analyzer."""


def find_slowest_success(requests):
    """Return the ID of the first slowest successful request, or None."""
    slowest_id = None
    slowest_latency = None

    for request in requests:
        if request["status"] == "success":
            if slowest_latency is None or request["latency_ms"] > slowest_latency:
                slowest_latency = request["latency_ms"]
                slowest_id = request["id"]

    return slowest_id
