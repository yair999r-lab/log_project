from checks import *
from reader import *
a = 'C:/Intel/pycharm/pythonProject8/New_project/network_traffic.log'
logs = import_file(a)

def analyze_suspicious_behavior(file_path):

    dict_night = {row[1]: "NIGHT_ACTIVITY" for row in find_night_activity(file_path)}
    dict_port = {row[1]: "SENSITIVE_PORT" for row in find_bad_port(file_path)}
    dict_large = {row[1]: "LARGE_PACKET" for row in find_big_size(file_path)}
    dict_ext = {row[1]: "EXTERNAL_IP" for row in find_bad_ip(file_path)}

    final_report = {}
    all_dicts = [dict_night, dict_port, dict_large, dict_ext]

    for current_dict in all_dicts:
        for ip, warning in current_dict.items():
            if ip not in final_report:
                final_report[ip] = []
            final_report[ip].append(warning)

    return final_report

def find_really_suspicious(path):
    a =analyze_suspicious_behavior(path)

    return {ip: warnings for ip, warnings in a.items() if len(warnings) >= 2}



checkers = {
    "NIGHT_ACTIVITY": lambda row: int(row[0].split()[1].split(':')[0]) < 6,
    "SENSITIVE_PORT": lambda row: int(row[3]) in (22, 80, 443, 3389),
    "LARGE_PACKET": lambda row: int(row[5]) > 2000,
    "EXTERNAL_IP": lambda row: row[1].startswith(("192.168.", "10."))
}

def find_a_suspicious(row, dict_checkers):
    passed_pairs = list(filter(lambda item: item[1](row), dict_checkers.items()))
    return list(map(lambda pair: pair[0], passed_pairs))

all_results = list(map(lambda row: find_a_suspicious(row, checkers), logs))

real_threats = list(filter(lambda results: len(results) > 0, all_results))
