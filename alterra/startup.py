import gorniy
import schedule
import time
def start_parse():
    start = gorniy

schedule.every().day.at("7:25").do(start_parse)

while True:
    schedule.run_pending()
    time.sleep(1)