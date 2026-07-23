import schedule
import time

from fetch_data import fetch_new_documents
from update_kb import update_database

def job():

    print("Checking for updates...")

    fetch_new_documents()

    update_database()

schedule.every(1).hours.do(job)

print("Scheduler Started...")

while True:

    schedule.run_pending()

    time.sleep(60)
