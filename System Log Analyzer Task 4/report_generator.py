def generate_report(summary, logs):
    report = []
    report.append("SYSTEM LOG REPORT")
    report.append("=================\n")

    report.append(f"Total Logs: {len(logs)}")
    report.append(f"INFO: {summary['INFO']}")
    report.append(f"WARNING: {summary['WARNING']}")
    report.append(f"ERROR: {summary['ERROR']}")

    return "\n".join(report)