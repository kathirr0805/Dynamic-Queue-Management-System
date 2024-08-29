import requests
import time

# Base URL for the Flask app
base_url = "http://127.0.0.1:5000"

# Simulate customers joining the queue
customers = ["Customer1", "Customer2", "Customer3"]

for customer in customers:
    response = requests.post(f"{base_url}/join_queue", json={"name": customer})
    print(response.json())
    time.sleep(1)  # Pause for 1 second between requests

# Check the queue status
status_response = requests.get(f"{base_url}/queue_status")
print("Queue Status:", status_response.json())

# Notify the next customer
notify_response = requests.get(f"{base_url}/notify_customer")
print(notify_response.json())
