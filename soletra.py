import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import re
import spacy

# Load spaCy Portuguese model
nlp = spacy.load("pt_core_news_sm")

# Path to your own vocabulary file
VOCAB_FILE = 'palavras.txt'

def load_vocabulary(filepath):
    pattern1 = re.compile(r'[A-Z]+')
    pattern2 = re.compile(r'\w+-\w+')
    pattern3 = re.compile(r'\.')

    vocabulary = []

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if pattern1.search(word) or pattern2.search(word) or pattern3.search(word):
                continue
            if len(word) >= 4:
                vocabulary.append(word.lower())

    return vocabulary

def is_valid_token(word):
    doc = nlp(word)
    if len(doc) == 1:
        token = doc[0]
        # Consider valid if it's alphabetic and not punctuation or number
        return token.is_alpha and not token.is_punct and token.pos_ not in ["PUNCT", "SYM", "NUM", "X"]
    return False



def filter_words(vocabulary, mandatory_letter, complementary_letters):
    filtered = []
    allowed_chars = set(complementary_letters + mandatory_letter)
    for word in vocabulary:
        if mandatory_letter in word and all(char in allowed_chars for char in word):
            filtered.append(word)
    return sorted(filtered, key=lambda x: (len(x), x))

# ---- App Setup ----
ctk.set_appearance_mode("System")  # Light / Dark / System
ctk.set_default_color_theme("soletra_theme.json")

app = ctk.CTk()
app.title("🔤 Soletreiro")
app.geometry("370x600")
app.resizable(False, False)

# ---- UI Layout ----

# Header
header = ctk.CTkLabel(
    app,
    text="📘 Resolvedor de Soletra",
    font=ctk.CTkFont(size=22, weight="bold")
)
header.pack(pady=(20, 10))

# Letter inputs frame
input_frame = ctk.CTkFrame(app, corner_radius=10)
input_frame.pack(pady=10, padx=20, fill="x")

entry_width = 100

# Mandatory letter
label_mandatory = ctk.CTkLabel(input_frame, text="Letra obrigatória:", anchor="w")
label_mandatory.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_mandatory = ctk.CTkEntry(input_frame, width=entry_width, placeholder_text="Ex: A")
entry_mandatory.grid(row=0, column=1, padx=10, pady=10)

# Complementary letters
label_complementary = ctk.CTkLabel(input_frame, text="Letras complementares:", anchor="w")
label_complementary.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_complementary = ctk.CTkEntry(input_frame, width=entry_width, placeholder_text="Ex: BCDEFG")
entry_complementary.grid(row=1, column=1, padx=10, pady=10)

# Run button directly under inputs
run_button = ctk.CTkButton(
    app,
    text="🔍 Encontrar palavras",
    command=lambda: run_filter(),
    width=150
)
run_button.pack(pady=(5, 15))

# Output box
output_font = ctk.CTkFont(family="Courier", size=12)
output_box = ctk.CTkTextbox(app, width=350, height=280, wrap="word")
output_box.pack(padx=20, pady=(0, 10))
output_box.configure(font=output_font)

# Filter and display logic
def run_filter():
    mandatory = entry_mandatory.get().lower()
    complementary = entry_complementary.get().lower()

    if not mandatory or len(mandatory) != 1 or len(complementary) != 6:
        messagebox.showerror("Erro", "Insira:\n• Uma letra obrigatória\n• Seis letras complementares")
        return

    try:
        vocab = load_vocabulary(VOCAB_FILE)
        results = filter_words(vocab, mandatory, complementary)

        output_box.delete("0.0", "end")
        if results:
            output_box.insert("end", f"{len(results)} palavras encontradas:\n\n")
            singular_words = set(results)

            for word in results:
                if word.endswith("s") and word[:-1] in singular_words:
                    continue  # Skip plural if singular is already in the list
                output_box.insert("end", word + "\n")

        else:
            output_box.insert("end", "Nenhuma palavra encontrada.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Spacer to push theme button to bottom
spacer = ctk.CTkLabel(app, text="")
spacer.pack(expand=True)

# Theme toggle at bottom
def toggle_theme():
    mode = ctk.get_appearance_mode()
    ctk.set_appearance_mode("Dark" if mode == "Light" else "Light")

theme_button = ctk.CTkButton(
    app,
    text="🌓 Alternar tema",
    command=toggle_theme,
    width=150
)
theme_button.pack(pady=(5, 15))

# ---- Start App ----
app.mainloop()
