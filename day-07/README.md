# Day 7 — Python Revision & AI Backend Coding Challenges

## Focus

Revise Python foundations (Days 1–6) and combine functions, loops, lists, dictionaries, sets, conditions, and `return` in small AI backend tasks.

## Learning activities

- **Session 1:** 10-question Python revision quiz (completed after feedback and retries)
- **Session 2:** 5 debugging exercises (completed after feedback and retries)
- **15-minute refresher:** dictionary counting, lists/sets, function returns, and a small coding exercise
- **Session 3:** four AI/backend coding challenges (Challenges 1–3 independently corrected; Challenge 4 combined with guidance)

## Coding challenges

| File | Description |
| --- | --- |
| `challenge_1_status_counter.py` | Counts success, failed, and pending; ignores unknown statuses |
| `challenge_2_failed_requests.py` | Collects unique failed request IDs while keeping first-seen order |
| `challenge_3_latency_analyzer.py` | Finds the ID of the slowest successful request; handles ties and empty input |
| `challenge_4_health_summary.py` | Counts recognized statuses and finds the slowest successful request in one pass |
| `test_day_07.py` | Unit tests for normal and edge cases |

## Run tests

From this folder:

```bash
python -m unittest -v test_day_07.py
```

On Windows you can use `py` instead of `python` if needed.

## Key takeaways

- Use `request["status"]` or `request["id"]` to access values inside a dictionary.
- Update a dictionary entry with `counts[key] += 1` rather than replacing the whole dictionary.
- A list preserves insertion order; a set helps detect duplicates efficiently.
- Initialize tracking variables to `None` when there is no valid candidate yet.
- Use `>` rather than `>=` to keep the first item in a tie.
- Place final `return` statements after the loop when the entire input must be processed.

## What's next

**Day 8:** New Python concepts and exercises building toward backend and AI engineering.
