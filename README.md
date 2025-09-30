# 🔑 Easypass: Strong Password Generator

**Easypass** is a robust and visually appealing password generator built with Python's Tkinter and `ttk`. It simplifies the process of creating highly secure, randomized passwords, allowing you to tailor them to any complexity requirements.

---

## ✨ Features

* **Customizable Length:** Define the exact number of characters for your password using the input field.
* **Granular Character Selection:** Easily toggle the character sets to include:
    * **Lowercase** letters (`a-z`)
    * **Uppercase** letters (`A-Z`)
    * **Numbers** (`0-9`)
    * **Special** characters (`!@#$%...`)
* **Modern Dark Theme:** A clean, dark-themed interface built using custom `ttk.Style` for a comfortable user experience.
* **Instant Copy:** Use the "Copy Password" button to immediately send the generated password to your clipboard.
* **Error Prevention:** Includes input validation to alert you about invalid password lengths or when no character types are selected.

---

## 💻 Requirements

To run this application, you only need a standard installation of **Python 3.x**, which includes the **Tkinter** library.

---

## 🚀 How to Run Easypass

1.  **Save the Code:** Save the provided Python code into a file named **`easypass.py`**.
2.  **Execute the Script:** Open your terminal or command prompt, navigate to the file's directory, and run the following command:

    ```bash
    python easypass.py
    ```

---

## 🎨 Styling and Design

The application uses a custom dark-mode color palette:

| Element | Color Code | Description |
| :--- | :--- | :--- |
| **Primary Background** | `#202124` | Main window background. |
| **Surface/Input Field** | `#303134` | Background for text fields and frames. |
| **Accent Color** | `#8AB4F8` | Used for active states, highlights, and the primary button. |
| **Text Color** | `#E8EAED` | Primary text and label color. |

---

## ⚙️ Key Functions

| Function | Description |
| :--- | :--- |
| `new_rand()` | The core generator function. It handles input validation, creates the randomized character pool based on checkboxes, and outputs the result. |
| `clipper()` | Manages clipboard operations. It checks if a password exists, clears the system clipboard, inserts the password, and confirms the action with a message box. |
