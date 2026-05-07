import matplotlib.pyplot as plt
import os

def generate_student_chart(data):

    if not os.path.exists("charts"):
        os.makedirs("charts")

    names = []
    marks = []

    for row in data:
        names.append(row[0])
        marks.append(int(row[4]))

    plt.figure(figsize=(6,4))

    plt.bar(names, marks)

    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.title("Student Marks Chart")

    chart_path = "charts/student_chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path


def generate_company_chart(data):

    if not os.path.exists("charts"):
        os.makedirs("charts")

    performance_count = {
        "Excellent": 0,
        "Good": 0,
        "Average": 0
    }

    for row in data:

        performance = row[5]

        if performance in performance_count:
            performance_count[performance] += 1

    plt.figure(figsize=(6,4))

    plt.bar(
        performance_count.keys(),
        performance_count.values()
    )

    plt.xlabel("Performance")
    plt.ylabel("Employees")
    plt.title("Company Performance Chart")

    chart_path = "charts/company_chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path