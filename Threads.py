from threading import Thread
import time

"""Thread(target=func, args=(arg1, arg2...)).start()"""

def privet(x: int):
    print(f"Hello WOrld {x}")

    time.sleep(5)

potoks = list()
for i in range(5):
    tz = Thread(target=privet, args=(i,))
    potoks.append(tz)

def start(elem: Thread):
    elem.start()

(map(start, potoks))

