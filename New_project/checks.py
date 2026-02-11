from reader import import_file



def find_bad_ip(path):
    a = import_file(path)
    return [x for x in a if not x[1].startswith(("192.168.", "10."))]

def find_bad_port(path):
    a = import_file(path)
    return [x for x in a if x[3] in ('22', '23', '3389')]

def find_big_size(path):
    a = import_file(path)
    return [x for x in a if int(x[-1]) > 5000]

def list_ip_plus_size(path):
    a = import_file(path)
    return [x + ["LARGE"] if int(x[-1]) > 5000 else x + ["NORMAL"] for x in a]

