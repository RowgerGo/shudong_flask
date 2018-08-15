import datetime

def getCurrentData(format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(format)