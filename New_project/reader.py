def import_file(path):
    with open(path,'r') as file:
        list_of_list = [b.strip().split(',') for b in file]
    return list_of_list
