import os
import requests
import json
import time
from datetime import datetime
# Load configuration
with open("../gts-config.json", "r") as config_file:
    config = json.load(config_file)
BASE_URL = config["BASE_URL"]
ACCESS_TOKEN = config["ACCESS_TOKEN"]
ACCOUNT_ID = config["ACCOUNT_ID"]
EARLIEST_DATE = config["EARLIEST_DATE"]
OUTPUT_DIR = config["OUTPUT_DIR"]
# Headers for API Authorization
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)
# Convert EARLIEST_DATE to datetime object for comparison
earliest_datetime = datetime.fromisoformat(EARLIEST_DATE.replace("Z", "+00:00"))
# Function to fetch statuses with pagination
def fetch_statuses(account_id, max_id=None):
    url = f"{BASE_URL}/api/v1/accounts/{account_id}/statuses"
    params = {"limit": 20}  # Adjust limit as needed
    if max_id:
        params["max_id"] = max_id
    response = requests.get(url, headers=headers, params=params)
    # Handle rate limiting
    if response.status_code == 429:
        reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait_time = reset_time - int(time.time())
        print(f"Rate limit reached. Waiting for {wait_time} seconds...")
        time.sleep(wait_time)
        return fetch_statuses(account_id, max_id)  # Retry after wait
    if response.status_code != 200:
        print(f"Error fetching statuses: {response.status_code} - {response.text}")
        return [], None
    statuses = response.json()
    # Update max_id for pagination
    if statuses:
        next_max_id = statuses[-1]["id"]  # Use the ID of the last status for the next page
    else:
        next_max_id = None
    return statuses, next_max_id
# Save statuses to files
def save_statuses_to_files(statuses):
    for status in statuses:
        status_id = status["id"]
        created_at = status["created_at"]
        content = status["content"]
        # Convert created_at to datetime object for comparison
        created_at_datetime = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        if created_at_datetime < earliest_datetime:
            print(f"Skipping status {status_id} (created at {created_at}) - earlier than {EARLIEST_DATE}.")
            continue
        # Generate a filename and clean up content
        filename = f"{created_at}_{status_id}.json".replace(":", "-")
        filepath = os.path.join(OUTPUT_DIR, filename)
        # Save the status as a JSON file
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(status, f, indent=4)
        print(f"Saved: {filepath}")
# Main Logic
def main():
    max_id = None
    while True:
        statuses, max_id = fetch_statuses(ACCOUNT_ID, max_id)
        if not statuses:
            print("No more statuses to fetch.")
            break
        # Filter out and save only statuses newer than EARLIEST_DATE
        filtered_statuses = [
            status for status in statuses
            if datetime.fromisoformat(status["created_at"].replace("Z", "+00:00")) >= earliest_datetime
        ]
        if not filtered_statuses:
            print(f"All statuses in this batch are older than {EARLIEST_DATE}. Stopping fetch.")
            break
        save_statuses_to_files(filtered_statuses)
        if not max_id:
            print("Reached the end of available statuses.")
            break
if __name__ == "__main__":
    main()