# Case_Converter_Program
A program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.

# 🐍 CamelCase / PascalCase to Snake Case Converter

This Python program converts strings formatted in **CamelCase** or **PascalCase** to **snake_case**. It demonstrates two implementations: one using a standard `for` loop, and another using list comprehension.

---

## 🚀 Features

- Converts any CamelCase or PascalCase string into snake_case.
- Includes two versions of the function for learning purposes:
  - **Phase 1**: For-loop implementation.
  - **Phase 2**: List comprehension implementation.
- Simple and easy to understand.
- Clear `main()` function to demonstrate usage.

---

## 🧪 Example Outputs

```python
Input:  'aLongAndComplexString'  → Output: 'a_long_and_complex_string'
Input:  'ALongAndComplexString'  → Output: 'a_long_and_complex_string'
Input:  'simpleTest'             → Output: 'simple_test'
Input:  'SimpleTest'             → Output: 'simple_test'
```
---

## 📄 File structure
```bash
convert_to_snake_case/
├── convert_to_snake_case.py  # Main Python script
├── README.md                 # Project documentation (this file)
```
---

## 🛠 Future Improvement
- Acronym Handling: Improve conversion to avoid splitting acronyms like HTTP into h_t_t_p.
✅ Goal: 'parseHTTPResponse' → 'parse_http_response'
⏳ Status: Logic ready, but not integrated into current version.

- Add CLI support for user input.

- Include automated tests with unittest or pytest.

- Package as a Python module.

---

### 🧑‍💻 How to Use
- Clone the repo or download the files.

- Open in VS Code (or another Python-friendly editor).

- Run the script with Python:

```bash
python convert_to_snake_case.py
```

---

##✅ Best Practices Followed

- Developed and edited in VS Code.

- Version controlled with Git and GitHub Desktop.

- Code structured for readability and maintainability.

- Future improvements tracked and documented.

---

## 📄 License

MIT License. Feel free to use, modify, and share.
