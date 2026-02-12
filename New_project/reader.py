from collections import Counter

def import_file(path):
    with open(path,'r') as file:
        list_of_list = [b.strip().split(',') for b in file]
    return list_of_list

def dict_of_ip(path):
    a = import_file(path)

    ab = [ips[1] for ips in a]
    b = {ip: ab.count(ip) for ip in set(ab)}

    return b

