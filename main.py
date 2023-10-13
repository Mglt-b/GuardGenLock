import tkinter as tk
from tkinter import ttk
import random
import string
import json

def generate_random_password(min_length, max_length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    length = random.randint(min_length, max_length)
    password = "".join(random.choice(characters) for _ in range(length))

    return password

def generate_password_from_phrase(phrase):
    replacements = {'a': '@', 'o': '0', 's': '$', 'i': '!', 'e': '3',
                    'u': 'ù', 'c': 'ç'}
    words = phrase.split()
    password = ""
    for word in words:
        password += word[0] + word[-1]
    for original, replacement in replacements.items():
        password = password.replace(original, replacement)
    random_index = random.randint(0, len(password)-1)
    password = password[:random_index] + password[random_index].upper() + password[random_index+1:]
    password += str(len(words))
    return password

def on_generate_random_password():
    min_length = int(entry_min_length.get())
    max_length = int(entry_max_length.get())
    use_uppercase = var_uppercase.get()
    use_lowercase = var_lowercase.get()
    use_digits = var_digits.get()
    use_special_chars = var_special_chars.get()
    password = generate_random_password(min_length, max_length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    entry_password_random.delete(0, tk.END)
    entry_password_random.insert(0, password)

def on_generate_phrase_password():
    phrase = entry_phrase.get()
    password = generate_password_from_phrase(phrase)
    entry_password_phrase.delete(0, tk.END)
    entry_password_phrase.insert(0, password)

def generate_random_phrase(num_words=10):
    with open('words.json', 'r') as file:
        data = json.load(file)

    # Vérifier que num_words n'est pas supérieur au nombre de thèmes disponibles
    num_words = min(num_words, len(data.keys()))
    
    # Sélectionner num_words thèmes de manière aléatoire
    selected_themes = random.sample(data.keys(), num_words)
    
    # Sélectionner un mot aléatoire de chaque thème choisi
    phrase_words = [random.choice(data[theme]) for theme in selected_themes]
    
    # Construire et afficher la phrase
    phrase = " ".join(phrase_words)
    entry_phrase.delete(0, tk.END)
    entry_phrase.insert(0, phrase)

# GUI Setup
window = tk.Tk()
window.title("GuardGenLock")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Random Password')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Phrase-Based Password')

# --- Random Password Tab (tab1) ---
entry_min_length = tk.Entry(tab1, width=5)
entry_min_length.pack(pady=5)
entry_min_length.insert(0, "10")

entry_max_length = tk.Entry(tab1, width=5)
entry_max_length.pack(pady=5)
entry_max_length.insert(0, "16")

var_uppercase = tk.BooleanVar(value=True)
chk_uppercase = tk.Checkbutton(tab1, text="Uppercase", variable=var_uppercase)
chk_uppercase.pack(pady=5)

var_lowercase = tk.BooleanVar(value=True)
chk_lowercase = tk.Checkbutton(tab1, text="Lowercase", variable=var_lowercase)
chk_lowercase.pack(pady=5)

var_digits = tk.BooleanVar(value=True)
chk_digits = tk.Checkbutton(tab1, text="Digits", variable=var_digits)
chk_digits.pack(pady=5)

var_special_chars = tk.BooleanVar(value=True)
chk_special_chars = tk.Checkbutton(tab1, text="Special Characters", variable=var_special_chars)
chk_special_chars.pack(pady=5)

btn_generate_random = tk.Button(tab1, text="Generate Password", command=on_generate_random_password)
btn_generate_random.pack(pady=20)

entry_password_random = tk.Entry(tab1, width=40)
entry_password_random.pack(pady=10)

# --- Phrase-Based Password Tab (tab2) ---
tk.Label(tab2, text="Enter a Phrase:").pack(pady=5)

# Bouton pour générer une phrase aléatoire
btn_generate_random_phrase = tk.Button(tab2, text="Generate Random Phrase", command=generate_random_phrase)
btn_generate_random_phrase.pack(pady=5)

entry_phrase = tk.Entry(tab2, width=40)
entry_phrase.pack(pady=5)

btn_generate_phrase = tk.Button(tab2, text="Generate Password", command=on_generate_phrase_password)
btn_generate_phrase.pack(pady=20)

entry_password_phrase = tk.Entry(tab2, width=40)
entry_password_phrase.pack(pady=10)

# Finalize layout and enter main loop
tab_control.pack(expand=1, fill='both')
window.mainloop()