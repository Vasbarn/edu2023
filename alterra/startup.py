import gorniy
import schedule
def start_parse():
    start = gorniy

schedule.every(5).minutes.do(start_parse)