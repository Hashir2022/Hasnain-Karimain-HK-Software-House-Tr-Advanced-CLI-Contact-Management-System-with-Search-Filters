import json
import os
import re
from datetime import datetime

FILE_NAME = "contacts.json"


# =========================
# LOAD DATA
# =========================
def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


# =========================
# SAVE DATA
# =========================
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# =========================
# ID GENERATOR
# =========================
def generate_id(contacts):
    if not contacts:
        return 1
    return max(c["id"] for c in contacts) + 1


# =========================
# VALIDATIONS
# =========================
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def validate_phone(phone):
    pattern = r'^\+?\d{10,15}$'
    return re.match(pattern, phone)


# =========================
# ADD CONTACT
# =========================
def add_contact(contacts):
    print("\n=== ADD CONTACT ===")

    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    city = input("City: ").strip()
    company = input("Company: ").strip()

    if not all([name, phone, email, city, company]):
        print("❌ All fields are required.")
        return

    if not validate_email(email):
        print("❌ Invalid email.")
        return

    if not validate_phone(phone):
        print("❌ Invalid phone number.")
        return

    contact = {
        "id": generate_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
        "company": company,
        "favorite": False,
        "created_at": str(datetime.now())
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("✅ Contact added successfully!")


# =========================
# VIEW CONTACTS (FIXED OUTPUT)
# =========================
def view_contacts(contacts):
    if not contacts:
        print("\n⚠ No contacts found.")
        return

    print("\n================ CONTACT LIST ================\n")

    header = f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Email':<25} {'City':<15} {'Company':<15}"
    print(header)
    print("-" * len(header))

    for c in contacts:
        print(
            f"{c['id']:<5} "
            f"{c['name']:<20} "
            f"{c['phone']:<15} "
            f"{c['email']:<25} "
            f"{c['city']:<15} "
            f"{c['company']:<15}"
        )

    print("\n==============================================\n")


# =========================
# SEARCH CONTACTS
# =========================
def search_contacts(contacts):
    keyword = input("\nSearch (name/phone/email): ").lower()

    result = [
        c for c in contacts
        if keyword in c["name"].lower()
        or keyword in c["phone"]
        or keyword in c["email"].lower()
    ]

    if not result:
        print("❌ No match found.")
        return

    view_contacts(result)


# =========================
# FILTER CONTACTS
# =========================
def filter_contacts(contacts):
    print("\n1. Filter by City")
    print("2. Filter by Company")

    choice = input("Choose: ")

    if choice == "1":
        city = input("Enter city: ").lower()
        result = [c for c in contacts if c["city"].lower() == city]

    elif choice == "2":
        company = input("Enter company: ").lower()
        result = [c for c in contacts if c["company"].lower() == company]

    else:
        print("❌ Invalid choice.")
        return

    if not result:
        print("❌ No contacts found.")
        return

    view_contacts(result)


# =========================
# UPDATE CONTACT
# =========================
def update_contact(contacts):
    try:
        cid = int(input("\nEnter Contact ID: "))
    except:
        print("❌ Invalid ID")
        return

    for c in contacts:
        if c["id"] == cid:

            print("Leave blank to keep old value\n")

            name = input(f"Name ({c['name']}): ").strip()
            phone = input(f"Phone ({c['phone']}): ").strip()
            email = input(f"Email ({c['email']}): ").strip()
            city = input(f"City ({c['city']}): ").strip()
            company = input(f"Company ({c['company']}): ").strip()

            if name:
                c["name"] = name
            if phone:
                if validate_phone(phone):
                    c["phone"] = phone
            if email:
                if validate_email(email):
                    c["email"] = email
            if city:
                c["city"] = city
            if company:
                c["company"] = company

            save_contacts(contacts)
            print("✅ Updated successfully!")
            return

    print("❌ Contact not found")


# =========================
# DELETE CONTACT
# =========================
def delete_contact(contacts):
    try:
        cid = int(input("\nEnter Contact ID: "))
    except:
        print("❌ Invalid ID")
        return

    for c in contacts:
        if c["id"] == cid:
            contacts.remove(c)
            save_contacts(contacts)
            print("✅ Deleted successfully!")
            return

    print("❌ Not found")


# =========================
# SORT CONTACTS
# =========================
def sort_contacts(contacts):
    contacts.sort(key=lambda x: x["name"].lower())
    print("✅ Sorted A-Z")
    view_contacts(contacts)


# =========================
# FAVORITE CONTACT
# =========================
def favorite_contact(contacts):
    try:
        cid = int(input("\nEnter Contact ID: "))
    except:
        print("❌ Invalid ID")
        return

    for c in contacts:
        if c["id"] == cid:
            c["favorite"] = True
            save_contacts(contacts)
            print("⭐ Marked as favorite")
            return

    print("❌ Not found")


# =========================
# MAIN MENU
# =========================
def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Filter Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Sort Contacts")
        print("8. Favorite Contact")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            filter_contacts(contacts)
        elif choice == "5":
            update_contact(contacts)
        elif choice == "6":
            delete_contact(contacts)
        elif choice == "7":
            sort_contacts(contacts)
        elif choice == "8":
            favorite_contact(contacts)
        elif choice == "9":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":
    main()
