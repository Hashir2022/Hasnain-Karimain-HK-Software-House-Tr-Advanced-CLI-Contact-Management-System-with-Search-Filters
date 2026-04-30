import tkinter as tk
import base64

# ---------------- ENCRYPT ----------------
def encrypt(text, key):
    shifted = ""
    for c in text:
        shifted += chr(ord(c) + key)

    return base64.b64encode(shifted.encode()).decode()

# ---------------- DECRYPT ----------------
def decrypt(text, key):
    decoded = base64.b64decode(text.encode()).decode()

    original = ""
    for c in decoded:
        original += chr(ord(c) - key)

    return original

# ---------------- FUNCTIONS ----------------
def do_encrypt():
    text = entry_text.get()
    key = int(entry_key.get())

    result = encrypt(text, key)
    output.set(result)

def do_decrypt():
    text = entry_text.get()
    key = int(entry_key.get())

    result = decrypt(text, key)
    output.set(result)

# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("Encryption & Decryption Tool")
root.geometry("400x300")

# Title
label_title = tk.Label(root, text="🔐 Encryption Tool", font=("Arial", 16))
label_title.pack(pady=10)

# Input Text
entry_text = tk.Entry(root, width=40)
entry_text.pack(pady=5)
entry_text.insert(0, "Enter Text")

# Key Input
entry_key = tk.Entry(root, width=20)
entry_key.pack(pady=5)
entry_key.insert(0, "Enter Key")

# Buttons
btn_encrypt = tk.Button(root, text="Encrypt", command=do_encrypt, bg="green", fg="white")
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(root, text="Decrypt", command=do_decrypt, bg="blue", fg="white")
btn_decrypt.pack(pady=5)

# Output Label
output = tk.StringVar()
label_output = tk.Label(root, textvariable=output, font=("Arial", 12), fg="red", wraplength=350)
label_output.pack(pady=20)

# Run App
root.mainloop()