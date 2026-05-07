import pandas as pd
import csv
import os
# =========================
# LOAD CSV
# =========================

def load_csv(file_path):

    try:

        data = pd.read_csv(file_path)

        return data.values.tolist()

    except Exception as e:

        print("Error Loading CSV:", e)

        return []

# =========================
# SAVE STUDENT DATA
# =========================

def save_student_data(data):

    file_exists = os.path.isfile(
        "sample_student.csv"
    )

    with open(
        "sample_student.csv",
        mode="a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # Header
        if not file_exists:

            writer.writerow([
                "Name",
                "ID",
                "Email",
                "Course",
                "Marks",
                "Attendance"
            ])

        writer.writerow(data)


# =========================
# SAVE COMPANY DATA
# =========================

def save_company_data(data):

    file_exists = os.path.isfile(
        "sample_company.csv"
    )

    with open(
        "sample_company.csv",
        mode="a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # Header
        if not file_exists:

            writer.writerow([
                "Name",
                "ID",
                "Email",
                "Department",
                "Role",
                "Performance"
            ])

        writer.writerow(data)