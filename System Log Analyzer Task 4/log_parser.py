import re

LOG_PATTERN = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>INFO|ERROR|WARNING) (?P<message>.*)'

def parse_log_line(line):
    match = re.match(LOG_PATTERN, line)
    if match:
        return match.groupdict()
    return None

def analyze_logs(file_path):
    logs = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed = parse_log_line(line.strip())
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print("❌ File not found!")
        return []

    return logs

def count_logs(logs):
    summary = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    for log in logs:
        level = log["level"]
        summary[level] += 1

    return summary

def search_logs(logs, keyword):
    result = []

    keyword = keyword.lower()

    for log in logs:
        if (keyword in log["message"].lower() or
            keyword in log["level"].lower() or
            keyword in log["date"] or
            keyword in log["time"]):
            result.append(log)

    return result

def filter_by_level(logs, level):
    return [log for log in logs if log["level"] == level]