import gorniy
import schedule
def start_parse():
    start = gorniy

schedule.every().day.at("13:45").do(start_parse)