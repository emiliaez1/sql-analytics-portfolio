import csv
import random
from datetime import datetime, timedelta

random.seed(42)

# USERS DATASET CREATION
countries = ["US", "CA", "UK", "IN", "DE", "AU"]

users = []
for user_id in range(1, 101):
    signup_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 30))
    country = random.choice(countries)
    users.append([user_id, signup_date.date(), country])

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "signup_date", "country"])
    writer.writerows(users)

# USER ACTIVITY DATASET CREATION
activity = []
for _ in range(300):
    user_id = random.randint(1, 100)
    activity_date = datetime(2024, 2, 1) + timedelta(days=random.randint(0, 14))
    activity.append([user_id, activity_date.date()])

with open("user_activity.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "activity_date"])
    writer.writerows(activity)

# CAMPAIGNS DATASET CREATION
campaigns = [
    [1, "Spring Sale"],
    [2, "New User Promo"],
    [3, "Holiday Discount"],
    [4, "Referral Boost"],
    [5, "Brand Awareness"]
]

with open("campaigns.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["campaign_id", "campaign_name"])
    writer.writerows(campaigns)

# CAMPAIGN EVENTS DATASET CREATION
events = []
for _ in range(100):
    campaign_id = random.randint(1, 5)
    event_date = datetime(2024, 2, 1) + timedelta(days=random.randint(0, 14))
    clicks = random.randint(20, 400)
    impressions = clicks * random.randint(5, 15)
    events.append([campaign_id, event_date.date(), clicks, impressions])

with open("campaign_events.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["campaign_id", "event_date", "clicks", "impressions"])
    writer.writerows(events)

print("CSV files generated successfully.")
