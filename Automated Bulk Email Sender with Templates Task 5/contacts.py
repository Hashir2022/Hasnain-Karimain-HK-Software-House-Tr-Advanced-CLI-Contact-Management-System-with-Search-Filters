import csv

def load_contacts(file_path):
    contacts = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)

    return contacts