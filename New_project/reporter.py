from reader import *

def list_of_hours(path):
    a = import_file(path)
    hours = list(map(lambda x: int(((x[0].split())[1].split(':'))[0]), a))
    return hours

def list_of_size_in_kilo(path):
    a = import_file(path)
    return list(map(lambda x: round(int(x[-1]) / 1024,0),a))

