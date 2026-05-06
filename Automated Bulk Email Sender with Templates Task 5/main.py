from contacts import load_contacts
from template import load_template, personalize
from email_sender import send_email
from utils import save_history

def menu():
    contacts = []
    template = ""

    sender = input("Enter your email: ")
    password = input("Enter app password: ")

    while True:
        print("\n===== EMAIL SYSTEM MENU =====")
        print("1. Load Contacts")
        print("2. Choose Template")
        print("3. Send Email")
        print("4. View History")
        print("5. Exit")

        choice = input("Enter choice: ")

        # Load Contacts
        if choice == "1":
            contacts = load_contacts("contacts.csv")
            print(f"Loaded {len(contacts)} contacts")

        #  Load Template
        elif choice == "2":
            template = load_template("templates/welcome.txt")
            print("Template loaded successfully")

        # Send Emails
        elif choice == "3":
            if not contacts or not template:
                print("❌ Load contacts and template first!")
                continue

            subject = input("Enter subject: ")

            for c in contacts:
                body = personalize(template, c)

                status = send_email(
                    sender,
                    password,
                    c["email"],
                    subject,
                    body
                )

                save_history(c["email"], subject, status)
                print(c["email"], "->", status)

        # View History
        elif choice == "4":
            try:
                import json
                with open("history.json", "r") as f:
                    data = json.load(f)
                    for h in data:
                        print(h)
            except:
                print("No history found")

        #  Exit
        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

menu()