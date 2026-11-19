
<div align="center">

# 🔍 SIFT COMPILER
### A Simple Language for Data Scientists

**CS1313 – Compilers | Phase 1: Lexical Analyzer**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Phase](https://img.shields.io/badge/Phase_1-Completed-28A745?style=for-the-badge)
![Status](https://img.shields.io/badge/Scanner-Ready-9B59B6?style=for-the-badge)

*A simple lexical analyzer with an interactive interface.*

</div>

---

## 📌 Project Overview

**Sift Compiler** is a compiler project designed for a simple data analysis programming language called **Sift**.

Phase 1 focuses on implementing a **Lexical Analyzer (Scanner)** using Python.

The scanner reads source code, recognizes tokens, generates a symbol table, and detects lexical errors with their corresponding line numbers.

---

## ✨ Key Features

| Feature | Description | Status |
|:---|:---|:---:|
| 🔍 Token Recognition | Identifies different token types | ✅ |
| 🔢 Token Counter | Displays the total number of tokens | ✅ |
| 📋 Token Table | Shows type, line number, and lexeme | ✅ |
| 📚 Symbol Table | Stores identifiers and their first occurrence | ✅ |
| ⚠️ Error Detection | Detects lexical errors with line numbers | ✅ |
| 📝 Code Editor | Allows users to enter Sift programs | ✅ |
| 📂 Sample Programs | Provides predefined test examples | ✅ |
| 🖥️ Interactive Interface | Built using Streamlit | ✅ |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|:---|:---|
| **Python** | Scanner implementation |
| **Regular Expressions (re)** | Token recognition and validation |
| **Streamlit** | Interactive user interface |
| **Pandas** | Displaying token and symbol tables |
| **GitHub** | Project version control |

---

## 🧩 Token Classification

The scanner recognizes the following token categories:

| Token Type | Example |
|:---|:---|
| KEYWORD | `analysis`, `load`, `show` |
| IDENTIFIER | `students`, `total` |
| NUMBER | `100`, `78.5` |
| TEXT | `"students.csv"` |
| OPERATOR | `+`, `=`, `>=` |
| DELIMITER | `(`, `)`, `,`, `.` |

---

## ⚠️ Lexical Error Detection

The scanner detects four main types of lexical errors.

| Error Type | Example |
|:---|:---|
| Unknown Symbol | `@` |
| Unclosed Text | `"Hello` |
| Malformed Number | `12abc` |
| Long Identifier | More than 16 characters |

Each error message includes the **line number** to help locate the problem.

---

## 🖥️ Application Interface

The Streamlit interface includes:

- **Sift Code Editor** – Write or paste source code.
- **Sample Selection** – Choose a predefined program.
- **Run Scanner** – Start lexical analysis.
- **Tokens Tab** – View recognized tokens.
- **Symbol Table Tab** – View stored identifiers.
- **Lexical Errors Tab** – View detected errors.

---

## 📂 Project Structure

```text
Sift-Compiler/
│
├── scanner.py      # Lexical analyzer
├── app.py          # Streamlit interface
└── README.md       # Project documentation
```

---

## 🚀 How to Run

### Step 1 – Open the Project

Clone or download the repository and open the folder in VS Code.

### Step 2 – Install Libraries

```bash
python -m pip install streamlit pandas
```

### Step 3 – Run the Application

```bash
python -m streamlit run app.py
```

### Step 4 – Test the Scanner

1. Enter Sift code or select a sample program.
2. Click **Run Scanner**.
3. View the tokens, symbol table, and lexical errors.

---

## 🧪 Sample Sift Program

```text
analysis Grades
load students from "students.csv" with (name text, score number)
let total = count(students)
show total
end
```

### Scanner Output

| Output | Description |
|:---|:---|
| **Total Tokens** | Number of recognized tokens |
| **Tokens Table** | Token type, lexeme, and line number |
| **Symbol Table** | Identifier names and first appearance |
| **Lexical Errors** | Error descriptions and line numbers |

> **Note:** In Phase 1, programs are scanned but not executed.

---

## 📊 Project Phase

| Phase | Description | Status |
|:---|:---|:---:|
| Phase 1 | Lexical Analyzer | ✅ Completed |
| Phase 2 | Syntax Analyzer | ⏳ Upcoming |
| Phase 3 | Semantic Analysis & Code Generation | ⏳ Upcoming |

---

## 🎓 Academic Information

| Information | Details |
|:---|:---|
| **Course** | CS1313 – Compilers |
| **Project** | Sift Compiler |
| **Current Phase** | Phase 1 – Lexical Analyzer |
| **Language** | Python |
| **University** | Imam Mohammad Ibn Saud Islamic University |

---

<div align="center">

### 💻 Sift Compiler – Phase 1

**Developed as part of the CS1313 Compilers course project.**

</div>
