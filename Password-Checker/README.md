# 🔐 Password Guess

A simple Python project that simulates a password verification system. The user has a limited number of attempts to enter the correct password before access is denied.

---

## 📌 Features

* 🔑 Prompts the user to enter a password.
* 🔄 Allows multiple login attempts.
* 📉 Decreases the number of remaining attempts after each incorrect password.
* ⚠️ Displays a warning message for incorrect passwords.
* ✅ Grants access when the correct password is entered.
* ❌ Stops the program when all attempts are used.

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
Password_Guess/
│── Password_Guess.py
│── README.md
```

---

## ▶️ How It Works

1. The user enters a password.
2. If the password is incorrect:

   * The remaining attempts decrease.
   * The user is asked to try again.
3. If the correct password is entered:

   * Access is granted.
4. If all attempts are used:

   * The program ends.

---

## 💻 Concepts Practiced

This project demonstrates:

* Variables
* User Input (`input()`)
* `while` Loops
* Conditional Statements (`if` / `else`)
* Loop Control (`break`)
* Formatted Strings (f-strings)

---

## 📷 Example

```text
Please, Your password: 123456

The password you entered is incorrect; please try again.
Wrong, 4 chances left.

Please, Your password: Ahmed@123

Correct password.
```

---

## 🚀 Future Improvements

* Hide the password while typing.
* Store the password securely using hashing.
* Validate password strength.
* Save login attempts to a file.
* Lock the account after too many failed attempts.
* Allow users to create and change passwords.

---

## 📜 License

This project was created for learning Python programming and practicing loops, conditional statements, and user input handling.
