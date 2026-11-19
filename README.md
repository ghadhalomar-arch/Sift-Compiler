
<div align="center">

# SIFT
### A Simple Language for Data Scientists

**COMPILER DESIGN PROJECT**

Phase 01 · Lexical Analysis

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Phase_1-Completed-2E8B57?style=flat-square)
![Project](https://img.shields.io/badge/Academic-6C63FF?style=flat-square)

<br>

*A lightweight compiler front-end designed to transform*
*simple source code into structured lexical information.*

---

**Overview** · **Features** · **Architecture** · **Installation** · **Testing**

</div>

<br>

## 01 — Project Overview

**Sift** is a simple programming language designed to make data analysis more accessible through readable, structured commands.

This project is developed as part of the **Compilers** course at Imam Mohammad Ibn Saud Islamic University.

The current implementation focuses on **Phase 1: Lexical Analysis**, where source code is processed to identify valid tokens, construct a symbol table, and detect lexical errors.

The application provides an interactive interface built with Streamlit, allowing users to write or select Sift programs and inspect the scanning results.

<br>

## 02 — Core Features

| Feature | Description |
|:---|:---|
| **Lexical Scanning** | Reads and analyzes Sift source code |
| **Token Recognition** | Identifies six token categories |
| **Token Classification** | Displays token type, lexeme, and line number |
| **Symbol Table** | Records identifiers and their first occurrence |
| **Error Detection** | Detects invalid lexical patterns |
| **Line Tracking** | Reports the location of lexical errors |
| **Sample Programs** | Provides predefined programs for testing |
| **Interactive Editor** | Allows users to enter and scan source code |

<br>

## 03 — System Architecture

The application consists of two main components.

### 3.1 Lexical Analyzer

**File:** `scanner.py`

Responsible for processing the input source code through regular expressions and identifying its lexical elements.

```text
          Sift Source Code
                 |
                 v
          Lexical Scanner
                 |
         +-------+-------+
         |       |       |
         v       v       v
       Tokens  Symbol   Lexical
               Table    Errors
```

### 3.2 User Interface

**File:** `app.py`

Provides an interactive environment for entering Sift programs, running the scanner, and viewing its results.

The interface includes:

- Source code editor
- Sample program selector
- Run Scanner button
- Total token counter
- Tokens table
- Symbol table
- Lexical errors panel

<br>

## 04 — Token Specification

The lexical analyzer recognizes six primary token categories.

| Token Class | Description | Example |
|:---|:---|:---|
| `KEYWORD` | Reserved language words | `analysis`, `load`, `show` |
| `IDENTIFIER` | User-defined names | `students`, `total` |
| `NUMBER` | Integer or decimal values | `100`, `78.5` |
| `TEXT` | Double-quoted strings | `"students.csv"` |
| `OPERATOR` | Arithmetic and comparison operators | `+`, `=`, `>=` |
| `DELIMITER` | Structural punctuation | `(`, `)`, `,`, `.` |

**Scanner Rules**

- Identifiers begin with a letter and have a maximum length of 16 characters.
- Numeric values contain 1–10 digits with an optional decimal part.
- Keywords are recognized after identifier matching.
- Comments beginning with `#` are ignored.
- Tokens are matched using the longest-match principle.
- Identifiers are stored in lowercase.

<br>

## 05 — Lexical Error Handling

The scanner identifies four categories of lexical errors.

| Error Category | Example | Description |
|:---|:---|:---|
| Unknown Symbol | `@` | Character not recognized by the language |
| Malformed Number | `12abc` | Invalid numeric format |
| Unclosed Text | `"Hello` | Missing closing quotation mark |
| Long Identifier | `verylongidentifiername` | Identifier exceeds 16 characters |

Every detected error includes its corresponding **source line number**.

<br>

## 06 — Technology Stack

| Technology | Role |
|:---|:---|
| **Python** | Core implementation |
| **Regular Expressions** | Lexical pattern recognition |
| **Streamlit** | Web-based user interface |
| **Pandas** | Tabular presentation of results |
| **Git & GitHub** | Version control and repository management |

<br>

## 07 — Getting Started

### Prerequisites

Make sure Python is installed on your machine.

### Installation

**Step 1 — Clone the repository**

Download or clone the repository and open the project directory.

**Step 2 — Install dependencies**

```bash
python -m pip install streamlit pandas
```

**Step 3 — Launch the application**

```bash
python -m streamlit run app.py
```

**Step 4 — Run the scanner**

1. Open the Streamlit application.
2. Select a sample program or write your own Sift code.
3. Click **Run Scanner**.
4. Explore the generated results.

<br>

## 08 — Example

### Sample Input

```text
analysis Grades
load students from "students.csv" with (name text, score number)
let total = count(students)
show total
end
```

### Expected Output Structure

The scanner produces three main outputs:

| Output | Information |
|:---|:---|
| **Tokens** | Type, line number, and lexeme |
| **Symbol Table** | Identifier name and first appearance |
| **Lexical Errors** | Error description and source line |

> **Note:** Phase 1 performs lexical analysis only. Sift programs are scanned but not executed.

<br>

## 09 — Project Structure

```text
Sift-Compiler/
│
├── scanner.py       # Lexical analyzer
├── app.py           # Streamlit application
└── README.md        # Project documentation
```

<br>

## 10 — Development Roadmap

| Phase | Scope | Progress |
|:---|:---|:---:|
| **01** | Lexical Analysis | Completed |
| **02** | Syntax Analysis — SLR(1) Parser | Planned |
| **03** | Semantic Analysis & Code Generation | Planned |

<br>

## 11 — Academic Information

| | |
|:---|:---|
| **Project** | Sift — A Simple Language for Data Scientists |
| **Course** | CS1313 — Compilers |
| **University** | Imam Mohammad Ibn Saud Islamic University |
| **Department** | Computer Science |
| **Current Phase** | Phase 1 — Lexical Analyzer |
| **Programming Language** | Python |

<br>

---

<div align="center">

### SIFT COMPILER

**Phase 01 — Lexical Analysis**

*Computer Science · Compiler Design*

Imam Mohammad Ibn Saud Islamic University

<br>

![Project Status](https://img.shields.io/badge/PROJECT-PHASE_1_COMPLETE-6C63FF?style=for-the-badge)

</div>
