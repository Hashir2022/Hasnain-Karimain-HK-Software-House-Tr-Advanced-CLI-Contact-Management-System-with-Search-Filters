from log_parser import analyze_logs, count_logs, search_logs, filter_by_level
from report_generator import generate_report
from utils import save_report

logs_data = []

def menu():
    global logs_data

    while True:
        print("\n===== LOG ANALYZER MENU =====")
        print("1. Load Log File")
        print("2. Analyze Logs")
        print("3. Search Logs")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            path = input("Enter file path: ")
            logs_data = analyze_logs(path)
            print(f"Loaded {len(logs_data)} logs")

        elif choice == "2":
            summary = count_logs(logs_data)
            print(summary)

        elif choice == "3":
            keyword = input("Enter keyword: ")
            results = search_logs(logs_data, keyword)
            for r in results:
                print(r)

        elif choice == "4":
            summary = count_logs(logs_data)
            report = generate_report(summary, logs_data)
            save_report(report)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

menu()