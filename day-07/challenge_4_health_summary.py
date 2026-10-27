"""Day 7 — Challenge 4: AI Request Health Summary."""


def analyze_ai_requests(requests):
    """Count known statuses and return the ID of the slowest success."""
    summary_dict = {"success": 0, "failed": 0, "pending": 0}
    slowest_success_id = None
    slowest_latency = None

    for request in requests:
        # Count only recognized statuses.
        if request["status"] in summary_dict:
            summary_dict[request["status"]] += 1

        # Find the first successful request with the greatest latency.
        if request["status"] == "success":
            if slowest_latency is None or request["latency_ms"] > slowest_latency:
                slowest_latency = request["latency_ms"]
                slowest_success_id = request["id"]

    summary_dict["slowest_success_id"] = slowest_success_id
    return summary_dict
