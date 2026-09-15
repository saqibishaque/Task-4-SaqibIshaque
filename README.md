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

## 🏗️ Architecture: The IPOS Flow
