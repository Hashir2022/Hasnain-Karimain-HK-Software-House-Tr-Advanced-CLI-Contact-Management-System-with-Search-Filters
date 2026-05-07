from data_loader import save_student_data, save_company_data, load_csv
from pdf_generator import generate_pdf
from charts import generate_student_chart, generate_company_chart

student_data = []
company_data = []

while True:

    print("\n===== PDF REPORT SYSTEM =====")
    print("1. Add Data")
    print("2. Load Data")
    print("3. Generate PDF")
    print("4. Exit")

    choice = input("Enter Choice: ")

    # =========================
    # ADD DATA
    # =========================
    if choice == "1":

        print("\n1. Student Data")
        print("2. Company Data")

        type_choice = input("Select Type: ")

        # STUDENT
        if type_choice == "1":

            name = input("Name: ")
            sid = input("ID: ")
            email = input("Email: ")
            course = input("Course: ")
            marks = input("Marks: ")
            attendance = input("Attendance: ")

            row = [name, sid, email, course, marks, attendance]

            student_data.append(row)
            save_student_data(row)

            print("✅ Student Data Added & Saved!")

        # COMPANY
        elif type_choice == "2":

            name = input("Name: ")
            cid = input("ID: ")
            email = input("Email: ")
            dept = input("Department: ")
            role = input("Role: ")
            performance = input("Performance: ")

            row = [name, cid, email, dept, role, performance]

            company_data.append(row)
            save_company_data(row)

            print("✅ Company Data Added & Saved!")

        else:
            print("Invalid Type!")

    # =========================
    # LOAD DATA
    # =========================
    elif choice == "2":

        print("\n1. Load Student Data")
        print("2. Load Company Data")

        load_choice = input("Select: ")

        if load_choice == "1":

            student_data = load_csv("sample_student.csv")
            print("✅ Student Data Loaded")

        elif load_choice == "2":

            company_data = load_csv("sample_company.csv")
            print("✅ Company Data Loaded")

        else:
            print("Invalid Option")

    # =========================
    # GENERATE PDF
    # =========================
    elif choice == "3":

        print("\n1. Student Report")
        print("2. Company Report")

        report_choice = input("Select Report: ")

        # STUDENT REPORT
        if report_choice == "1":

            student_data = load_csv("sample_student.csv")

            if len(student_data) == 0:
                print("No Student Data Found")
            else:
                chart = generate_student_chart(student_data)
                generate_pdf(student_data, "Student", chart)

        # COMPANY REPORT
        elif report_choice == "2":

            company_data = load_csv("sample_company.csv")

            if len(company_data) == 0:
                print("No Company Data Found")
            else:
                chart = generate_company_chart(company_data)
                generate_pdf(company_data, "Company", chart)

        else:
            print("Invalid Option")

    # =========================
    # EXIT
    # =========================
    elif choice == "4":

        print("Program Closed 🚀")
        break

    else:
        print("Invalid Choice!")