from checks import *

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
