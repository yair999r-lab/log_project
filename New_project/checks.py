from reader import import_file

def find_ip(path):
    a = import_file(path)
    return [x for x in a if not x[1].startswith(("192.168.", "10."))]

def find_port(path):
    a = import_file(path)
    return [x for x in a if x[3] in ('22', '23', '3389')]

