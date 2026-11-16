# FNB App Academy 2026 – Python Programming

My coursework from the **FNB App Academy 2026** Python Programming course. The repo is organised by unit. Each unit has a `lesson` file (code written while following the video lessons) and one or more practical tasks and challenges that apply the lesson on my own.

All programs are small command-line scripts that use `input()` and `print()`.

## Requirements

- Python 3.12 or newer (`contact_book.py` uses nested quotes inside f-strings, which older versions reject)
- No external libraries

## Running a script

```bash
cd "Unit 1"
python lesson1.py
```

## Repository structure

```
FNB_App_Acad/
├── Unit 1/   Input, variables and data types
├── Unit 2/   Strings and string methods
├── Unit 3/   Arithmetic and type conversion
├── Unit 4/   Conditional logic (if / elif / else)
└── Unit 5/   Loops, functions, lists and dictionaries
```

## What I built in each unit

### Unit 1 – Input, variables and data types
| File | Description |
|------|-------------|
| `lesson1.py` | Takes a name and age from the user and greets them with an f-string. |
| `student_info.py` | Collects a name, age and favourite number. Converts types with `int()` and `float()`, formats the name with `.upper()` and `.title()`, converts age to months, rounds a decimal and prints each variable's `type()`. |

**Challenge:** a ticket confirmation message that uses the user's name and favourite artist.

**Concepts:** `input()`, variables, `int` / `float` / `str`, f-strings, `round()`, `type()`

### Unit 2 – Strings
| File | Description |
|------|-------------|
| `lesson2.py` | Indexing (`name[0]`, `name[-1]`), string methods, and a professional email address generator (first initial + surname). |
| `string_formatter.py` | Builds a username, formats a full name, and creates a bio string using `.strip()`, `.replace()` and `len()`. |

**Challenge:** a password hint generator that reveals the first and last characters of a password.

**Concepts:** indexing, negative indexing, `.upper()`, `.lower()`, `.title()`, `.strip()`, `.replace()`, `len()`

### Unit 3 – Arithmetic and type conversion
| File | Description |
|------|-------------|
| `lesson3.py` | Basic arithmetic on user input, a tip and total calculator for a bill in rand (R), and a fuel cost calculator. |
| `calculator.py` | Two-number calculator covering addition, subtraction, multiplication, division, exponentiation, modulus and floor division. |
| `test.py` | A short experiment with string slicing (`text[3:7]`). |

**Challenge:** a trip fuel cost calculator from distance and fuel price, assuming 10 km per litre.

**Concepts:** converting input types, arithmetic operators (`+ - * / ** % //`), rounding, string slicing

### Unit 4 – Conditional logic
| File | Description |
|------|-------------|
| `lesson4.py` | A venue access check (age and VIP ticket) built on `if` / `elif` / `else` and logical operators. |
| `grade_classifier.py` | Averages three subject marks and assigns a grade (A–D pass, F fail). Flags the student for intervention if any single mark is below 40. |

**Challenge:** a Smart ATM withdrawal simulator that checks balance and rejects invalid amounts.

**Concepts:** comparison operators, `and` / `or`, `if` / `elif` / `else`, branching on multiple conditions

### Unit 5 – Loops, functions, lists and dictionaries
| File | Description |
|------|-------------|
| `lesson5.py` | A `while` countdown, a `for` loop with `range()`, and a "guess the language" game using `while True` and `break`. |
| `high_score.py` | An experiment combining a `for` loop, a counter and an early `break`. |
| `contact_book.py` | **Main project.** A menu-driven contact book that stores contacts as a list of dictionaries. Users can add, search, delete and view contacts. |

**Concepts:** `while` and `for` loops, `range()`, `break`, functions with parameters and return values, lists, dictionaries, building a menu loop

#### Contact book features
1. **Add** a contact (name, number, email)
2. **Search** for a contact by name
3. **Delete** a contact
4. **View** all contacts
5. **Exit**

Each action is its own function (`add_student`, `search_contact`, `delete_contact`, `view_contacts`), and a `menu()` loop ties them together.

## Skills practised

- Reading and validating user input
- Working with Python's core data types
- String manipulation and formatting
- Arithmetic, type conversion and rounding
- Decision making with conditionals
- Repetition with loops
- Organising code into reusable functions
- Storing structured data in lists and dictionaries

## Known issues and next steps

These are things I've spotted while reviewing my own code and plan to improve:

- **Contact book:** `search_contact` and `delete_contact` only check the first contact in the list, because a `return` and a `print` sit inside the loop and need to move outside it.
- **Contact book:** `add_student` should be renamed `add_contact`, and it shouldn't store the whole list inside each new contact.
- **Contact book:** phone numbers are stored as `int`, which drops leading zeros. A string would be better.
- **Contact book:** contacts aren't saved between runs. A next step is writing them to a file.
- **Calculator:** division and modulus crash on a zero input, so they need error handling with `try` / `except` or an `if` check.
- **Calculator:** the subtraction is `num2 - num1`, so the order should be corrected.
- **ATM simulator:** the balance prints with a `$` symbol instead of `R`. The invalid-amount check should also come before the balance check, so a negative withdrawal can't pass.
- **General:** add input validation so that typing text instead of a number doesn't crash the program.

## About

I'm an IT student building my software development skills. This repo records my progress through the course.
