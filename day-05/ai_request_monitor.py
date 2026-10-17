ai_job = {
    "job_id": 501,
    "model": "GPT-6",
    "status": "Pending"
}

events = [
    "success",
    "failed",
    "success",
    "pending",
    "success",
    "failed"
]

ai_job["priority"] = "High"
ai_job["status"] = "Completed"


event_counts = {}
for event in events:
    event_counts[event] = event_counts.get(event, 0) + 1
print("Job:", ai_job["job_id"])
print("Model:", ai_job["model"])
print("Status:", ai_job["status"])
print("Priority:", ai_job["priority"])

if "owner" in ai_job:
    print(ai_job["owner"])
else: 
    print("Owner: Not assigned")

for keys, values in event_counts.items():
    print(keys, values)

total = 0

for value in event_counts.values():
    total += value
print("Total events:", total)