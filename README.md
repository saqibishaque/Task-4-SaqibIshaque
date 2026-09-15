# General Knowledge Quiz Engine

An interactive, deterministic decision-engine quiz application developed in Python. Built as part of the **DecodeLabs Python Programming Industrial Training Kit (Project 4: Control Flow Mastery Track)**.

---

## 📌 Project Overview

This project transitions from static linear scripts to an **Input-Process-Output-Storage (IPOS)** state machine architecture. It evaluates real-time user input via strict sanitization pipelines and dynamic conditional branching (Control Flow).

### Key Concepts Implemented
- **IPOS Architecture:** Maps the full lifecycle of data from standard input capture to terminal output feedback.
- **Data Sanitization Pipeline:** Mitigates the "Chaos of Human Input" and ASCII case-sensitivity traps using `.strip()` and `.lower()`.
- **State Management:** Employs an integer accumulator (`score`) to sustain runtime session memory[cite: 1].
- **Dynamic F-String Interpolation:** Aligns and outputs score summaries using runtime string formatting (`{score:>2}`)[cite: 1].

---

## ⚙️ Features

- **Leading/Trailing Whitespace Stripping:** Eliminates accidental spaces, tabs (`\t`), and newlines (`\n`)[cite: 1].
- **Case Normalization:** Guarantees that inputs such as `Paris`, `paris`, and `PARIS` evaluate uniformly[cite: 1].
- **Explicit Branching:** Employs clean `if-else` gates ensuring deterministic outcomes for both valid and invalid answers[cite: 1].
- **Aligned CLI Output:** Uses field width alignment for formatted score reporting[cite: 1].

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+** installed on your machine.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/general-knowledge-quiz.git](https://github.com/your-username/general-knowledge-quiz.git)
   cd general-knowledge-quiz
  Run the script:
   ```bash
   python quiz.py
