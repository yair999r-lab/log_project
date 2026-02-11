from reader import import_file

def find_ip(phta):
    a = import_file(phta)
    return [x for x in a if not x[1].startswith(("192.168.", "10."))]