import tkinter as tk
from tkinter import messagebox, scrolledtext
import re

# Path to your own vocabulary file
VOCAB_FILE = 'palavras.txt'

def load_vocabulary(filepath):
    pattern1 = re.compile(r'[A-Z]+')     # Remove words with capital letters
    pattern2 = re.compile(r'\w+-\w+')    # Remove words with hyphens
    pattern3 = re.compile(r'\.')         # Remove words with dots

    vocabulary = []

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()

            if pattern1.search(word) or pattern2.search(word) or pattern3.search(word):
                continue

            if len(word) >= 4:
                vocabulary.append(word.lower())

    return vocabulary

def filter_words(vocabulary, mandatory_letter, complementary_letters):
    filtered = []
    allowed_chars = set(complementary_letters + mandatory_letter)

    for word in vocabulary:
        if mandatory_letter in word and all(char in allowed_chars for char in word):
            filtered.append(word)

    return sorted(filtered, key=lambda x: (len(x), x))

def run_filter():
    mandatory = entry_mandatory.get().lower()
    complementary = entry_complementary.get().lower()

    if not mandatory or len(mandatory) != 1 or len(complementary) != 6:
        messagebox.showerror("Input error", "Inclua caracteres válidos:\n• Uma letra obrigatória\n• Seis letras complementares")
        return

    try:
        vocab = load_vocabulary(VOCAB_FILE)
        results = filter_words(vocab, mandatory, complementary)

        output.delete(1.0, tk.END)
        if results:
            output.insert(tk.END, f"{len(results)} palavras encontradas:\n\n")
            for word in results:
                output.insert(tk.END, word + '\n')
        else:
            output.insert(tk.END, "Nenhuma palavra encontrada.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# GUI setup
root = tk.Tk()
root.title("Resolve-Soletra")

# Mandatory letter
tk.Label(root, text="Letra obrigatória:").grid(row=0, column=0, sticky='w')
entry_mandatory = tk.Entry(root, width=5)
entry_mandatory.grid(row=0, column=1, sticky='w')

# Complementary letters
tk.Label(root, text="6 letras complementares:").grid(row=1, column=0, sticky='w')
entry_complementary = tk.Entry(root, width=10)
entry_complementary.grid(row=1, column=1, sticky='w')

# Filter button
tk.Button(root, text="Encontrar palavras", command=run_filter, bg="#4CAF50", fg="white").grid(row=2, column=1, pady=10)

# Output
output = scrolledtext.ScrolledText(root, width=60, height=20)
output.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
