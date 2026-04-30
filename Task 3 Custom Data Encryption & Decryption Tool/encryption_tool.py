import base64
import json
import os
from datetime import datetime

FILE_NAME = "encrypted_data.json"

# ---------------- ENCRYPTION ----------------
def encrypt(text, key):
    shifted_text = ""

    # Step 1: character shifting
    for char in text:
        shifted_text += chr(ord(char) + key)

    # Step 2: base64 encoding
    encoded = base64.b64encode(shifted_text.encode()).decode()

    return encoded

# ---------------- DECRYPTION ----------------
def decrypt(encoded_text, key):
    try:
        decoded = base64.b64decode(encoded_text.encode()).decode()

        original_text = ""

        # reverse shifting
        for char in decoded:
            original_text += chr(ord(char) - key)

        return original_text

    except:
        return "Invalid Data or Key!"

# ---------------- SAVE DATA ----------------
def save_data(encrypted_text):
    data = {
        "timestamp": str(datetime.now()),
        "encrypted_data": encrypted_text
    }

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

    print("Data Saved Successfully!")

# ---------------- LOAD DATA ----------------
def load_data():
    if not os.path.exists(FILE_NAME):
        print("No file found!")
        return None

    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        print("File Corrupted!")
        return None

# ---------------- MAIN PROGRAM ----------------
def main():
    encrypted_text = ""

    while True:
        print("\n===== ENCRYPTION TOOL =====")
        print("1. Encrypt Data")
        print("2. Decrypt Data")
        print("3. Save Data")
        print("4. Load & Decrypt Data")
        print("5. Exit")

        choice = input("Enter Choice: ")

        # Encrypt
        if choice == "1":
            text = input("Enter Text: ")
            key = int(input("Enter Key: "))

            encrypted_text = encrypt(text, key)
            print("Encrypted Text:", encrypted_text)

        # Decrypt
        elif choice == "2":
            text = input("Enter Encrypted Text: ")
            key = int(input("Enter Key: "))

            print("Decrypted Text:", decrypt(text, key))

        # Save
        elif choice == "3":
            if encrypted_text == "":
                print("No data to save!")
            else:
                save_data(encrypted_text)

        # Load & Decrypt
        elif choice == "4":
            data = load_data()

            if data:
                print("Encrypted Data:", data["encrypted_data"])
                key = int(input("Enter Key: "))

                print("Decrypted Text:", decrypt(data["encrypted_data"], key))

        # Exit
        elif choice == "5":
            print("Program Ended")
            break

        else:
            print("Invalid Choice!")

# Run program
main()


def multi_encrypt(text, key):
    step1 = text[::-1]
    step2 = "".join(chr(ord(c)+key) for c in step1)
    step3 = base64.b64encode(step2.encode()).decode()
    return step3