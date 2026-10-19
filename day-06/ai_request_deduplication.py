
# Day 6 - AI Request Deduplication System

# Step 1: Incoming and previously processed requests
incoming_requests = [501, 502, 501, 503, 504, 502, 505]
processed_requests = {501, 503}

# Step 2: Find unique requests
updated_set = set(incoming_requests)

# Step 3: Identify previously processed requests
already_processed = processed_requests.intersection(updated_set)

# Step 4: Identify new requests
new_requests = updated_set.difference(processed_requests)

# Step 5: AI model configuration
model_config = ("GPT-6", 1000, "Production")

# Step 6: Generate monitoring report
def print_report(incoming_requests, unique_requests, already_processed, new_requests, model_config):
    print("AI Request Monitoring Report")
    print("Total requests received:", len(incoming_requests))
    print("Unique request IDs:", len(unique_requests))
    print("Previously processed requests:", len(already_processed))
    print("New requests to process:", len(new_requests))
    print("AI Model:", model_config[0])
    print("Max Tokens:", model_config[1])
    print("Environment:", model_config[2])


# Run the report
print_report(incoming_requests, updated_set, already_processed, new_requests, model_config)
