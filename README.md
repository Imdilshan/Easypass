# 🔑 Easypass: Strong Password Generator

**Easypass** is a sleek, easy-to-use password generator built with Python's Tkinter. It allows you to quickly create highly secure, randomized passwords tailored to your specifications, making password management truly **easy**.



---

## ✨ Features

* **Customizable Length:** Define the precise length of your secure password.
* **Granular Character Selection:** Easily toggle the inclusion of essential character types:
    * **Lowercase** letters (`a-z`)
    * **Uppercase** letters (`A-Z`)
    * **Numbers** (`0-9`)
    * **Special** characters (`!@#$%...`)
* **Modern Dark Theme:** A clean, dark-themed interface built with `ttk.Style` for a professional, eye-friendly experience.
* **Instant Copy:** Use the "Copy Password" button to instantly send the generated password to your clipboard.
* **Error Prevention:** Robust checks ensure you receive alerts for invalid length inputs or if you forget to select any character types.

---

## 💻 Requirements

You only need a standard Python installation that includes **Tkinter** (which is usually bundled with Python 3.x).

* **Python 3.x**

---

## 🚀 How to Run Easypas

1.  **Save the Code:** Save the provided Python code into a file named `easypas.py`.
2.  **Execute the Script:** Open your terminal or command prompt, navigate to the file's directory, and run the following command:

    ```bash
    python easypas.py
    ```

---

## 🎨 Styling and Customization

The application uses a custom color palette for a cohesive, dark-mode look:

| Element | Color Code | Description |
| :--- | :--- | :--- |
| **Primary Background** | `#202124` | Main window background. |
| **Surface/Input Field** | `#303134` | Background for text fields and frames. |
| **Accent Color** | `#8AB4F8` | Used for active states, highlights, and primary button colors. |
| **Text Color** | `#E8EAED` | Primary text and label color. |

The **`ttk.Style`** configurations provide custom button styles:
* `Accent.TButton`: The primary, high-contrast button ("Generate Password").
* `Secondary.TButton`: The secondary, low-contrast button ("Copy Password").

---

## ⚙️ Key Functions

| Function | Description |
| :--- | :--- |
| `new_rand()` | The core generator function. It handles input validation, creates the randomized character pool based on checkboxes, and outputs the result. |
| `clipper()` | Manages clipboard operations. It checks if a password exists, clears the system clipboard, inserts the password, and confirms the action with a message box. |
