from datetime import datetime

def time():
    cur_time = datetime.now().time()
    return cur_time


print(time())