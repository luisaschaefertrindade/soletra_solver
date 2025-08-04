# Soletra puzzle helper

This tool can be used as a helper to solve g1's [Soletra](https://g1.globo.com/jogos/soletra/) puzzle, equivalent of New York Times' _Spelling Bee_. Enter a **mandatory letter** and **six complementary letters**, and the program will list all valid words from a vocabulary file.

<img width="742" height="629" alt="image" src="https://github.com/user-attachments/assets/e4f26715-52fc-486f-b075-fb5955895244" />

---

## Features

* Modern GUI built with `customtkinter` for a clean and responsive interface
* Uses spaCy's Portuguese model (`pt_core_news_sm`) for basic linguistic filtering
* Loads words from a vocabulary file, a collection of dictionary entries scraped from VOLP, Vocabulário Ortográfico da Língua Portuguesa, available in https://voc.cplp.org/index.php
* Filters and sorts words according to Soletra puzzle rules, excluding:

  * Words with uppercase letters
  * Hyphenated words
  * Words containing dots
  * Words shorter than 4 letters
* Sorts results by length, then alphabetically
* Removes simple plurals (e.g., “gostos” is excluded if “gosto” is already listed)
* Displays results in a scrollable text box

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/luisaschaefertrindade/soletra_solver.git
   cd soletra_solver
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\\Scripts\\activate  # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   python -m spacy download pt_core_news_sm
   ```

## Usage

1. **Run the application**

   ```bash
   python soletra.py
   ```

2. **In the GUI**

   * Enter the **mandatory letter** (one character).
   * Enter the **6 complementary letters** (six characters).
   * Click **Encontrar palavras**.
   * View all valid words in the scrollable box.


## License

Distributed under the MIT License.

---

© 2025 Luísa Schaefer Trindade
