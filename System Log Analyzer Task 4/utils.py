def save_report(content, filename="reports/report.txt"):
    with open(filename, "w") as file:
        file.write(content)

    print("✅ Report saved successfully!")