"""Standard-library tests for all four Day 7 coding challenges.

Run from within day-07: python -m unittest -v test_day_07.py
"""

import unittest

from challenge_1_status_counter import count_statuses
from challenge_2_failed_requests import collect_failed_requests
from challenge_3_latency_analyzer import find_slowest_success
from challenge_4_health_summary import analyze_ai_requests


class Day7Tests(unittest.TestCase):
    def test_challenge_1_mixed(self):
        self.assertEqual(count_statuses(["success", "failed", "success", "pending", "failed", "failed"]), {"success": 2, "failed": 3, "pending": 1})

    def test_challenge_1_failed_only(self):
        self.assertEqual(count_statuses(["failed", "failed"]), {"success": 0, "failed": 2, "pending": 0})

    def test_challenge_1_empty(self):
        self.assertEqual(count_statuses([]), {"success": 0, "failed": 0, "pending": 0})

    def test_challenge_1_unknown(self):
        self.assertEqual(count_statuses(["cancelled", "success", "retrying"]), {"success": 1, "failed": 0, "pending": 0})

    def test_challenge_2_mixed_and_deduped(self):
        items = [{"id": 101, "status": "success"}, {"id": 102, "status": "failed"}, {"id": 103, "status": "failed"}, {"id": 102, "status": "failed"}, {"id": 104, "status": "pending"}]
        self.assertEqual(collect_failed_requests(items), [102, 103])

    def test_challenge_2_no_failure(self):
        self.assertEqual(collect_failed_requests([{"id": 201, "status": "success"}, {"id": 202, "status": "pending"}]), [])

    def test_challenge_2_duplicates(self):
        self.assertEqual(collect_failed_requests([{"id": 301, "status": "failed"}, {"id": 302, "status": "failed"}, {"id": 301, "status": "failed"}]), [301, 302])

    def test_challenge_2_empty(self):
        self.assertEqual(collect_failed_requests([]), [])

    def test_challenge_3_mixed(self):
        items = [{"id": 201, "status": "success", "latency_ms": 120}, {"id": 202, "status": "failed", "latency_ms": 900}, {"id": 203, "status": "success", "latency_ms": 250}, {"id": 204, "status": "success", "latency_ms": 180}]
        self.assertEqual(find_slowest_success(items), 203)

    def test_challenge_3_all_failed(self):
        self.assertIsNone(find_slowest_success([{"id": 1, "status": "failed", "latency_ms": 50}]))

    def test_challenge_3_empty(self):
        self.assertIsNone(find_slowest_success([]))

    def test_challenge_3_tie(self):
        items = [{"id": 301, "status": "success", "latency_ms": 400}, {"id": 302, "status": "success", "latency_ms": 400}]
        self.assertEqual(find_slowest_success(items), 301)

    def test_challenge_3_zero(self):
        self.assertEqual(find_slowest_success([{"id": 401, "status": "success", "latency_ms": 0}]), 401)

    def test_challenge_4_mixed(self):
        items = [{"id": 101, "status": "success", "latency_ms": 120}, {"id": 102, "status": "failed", "latency_ms": 900}, {"id": 103, "status": "success", "latency_ms": 250}, {"id": 104, "status": "pending", "latency_ms": 0}, {"id": 105, "status": "success", "latency_ms": 180}]
        self.assertEqual(analyze_ai_requests(items), {"success": 3, "failed": 1, "pending": 1, "slowest_success_id": 103})

    def test_challenge_4_failed_only(self):
        items = [{"id": 1, "status": "failed", "latency_ms": 10}, {"id": 2, "status": "failed", "latency_ms": 12}]
        self.assertEqual(analyze_ai_requests(items), {"success": 0, "failed": 2, "pending": 0, "slowest_success_id": None})

    def test_challenge_4_empty(self):
        self.assertEqual(analyze_ai_requests([]), {"success": 0, "failed": 0, "pending": 0, "slowest_success_id": None})

    def test_challenge_4_tie(self):
        items = [{"id": 301, "status": "success", "latency_ms": 400}, {"id": 302, "status": "success", "latency_ms": 400}]
        self.assertEqual(analyze_ai_requests(items), {"success": 2, "failed": 0, "pending": 0, "slowest_success_id": 301})

    def test_challenge_4_zero_and_unknown(self):
        items = [{"id": 401, "status": "success", "latency_ms": 0}, {"id": 402, "status": "cancelled", "latency_ms": 999}]
        self.assertEqual(analyze_ai_requests(items), {"success": 1, "failed": 0, "pending": 0, "slowest_success_id": 401})


if __name__ == "__main__":
    unittest.main()
