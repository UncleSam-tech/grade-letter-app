# Grade Letter App

A simple Python CLI tool that converts numeric exam scores to letter grades based on a common grading scale. Designed for beginners to practice Python conditionals, functions, validation, and input/output handling.

---

## 🧠 Purpose

This project helps new Python learners understand:
- Function definition and reuse
- Conditional branching (`if/elif/else`)
- Input validation with exceptions
- Basic command-line interaction
- Using helper functions for clean logic separation

---

## 🔧 Features

- `is_valid_score(score)`: Ensures that the score is between 0 and 100.
- `grade_letter(score)`: Returns a letter grade (`A–F`) based on the provided score.
- CLI interface with `input()` to accept user score input and display the result.

---

## 📁 File Structure

```
grade_letter.py   # Main application script
README.md         # This file
```

---

## 🔗 Dependencies

This app uses **pure Python**.  
No external libraries or packages are required.

- ✅ Compatible with Python 3.6+

---

## 🚀 How to Run

1. Clone or download this repository.
2. Open your terminal or command prompt.
3. Run the script with:

```bash
python grade_letter.py
```

4. Enter your score when prompted. You'll receive a letter grade or an error if the score is invalid.

---

## 🧪 Optional: Run Doctests

If you add doctest examples in the future, you can run them using:

```bash
python -m doctest grade_letter.py
```

---

## 📦 Deployment Notes

This is a local CLI tool for learning purposes. No deployment needed.

However, you could:
- Wrap it in a simple web form using Flask or Django.
- Build a GUI version with Tkinter or PyQt.
- Turn it into an API for educational grading apps.

---

## ✅ Example

```bash
$ python grade_letter.py
Enter your score: 88
Your Grade is: B
```

---

## 🧠 Author

Created as part of a 30-day Python learning sprint.
