# Soletra puzzle helper

This tool can be used as a helper to solve g1's [Soletra](https://g1.globo.com/jogos/soletra/) puzzle, equivalent of New York Times' Spelling Bee. Enter a mandatory letter and six complementary letters, and the program will list all valid words from a vocabulary file.

<img width="523" height="463" alt="image" src="https://github.com/user-attachments/assets/f6c24edd-c330-4239-85e2-7ece49488053" />


---

## Features

* Tkinter‑based GUI for an easy, interactive experience
* Load and use your own vocabulary file (UTF‑8 encoded `.txt`)
* Automatically filters out:

  * Words with uppercase letters
  * Hyphenated words
  * Words containing dots
  * Words shorter than 4 letters
* Sorts results by length, then alphabetically
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

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

© 2025 Luísa Schaefer Trindade
