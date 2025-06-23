# Bank Management System 🏦

A fully functional **Bank Management System** built using Python.  
This system supports account management, money transactions, and real-time user history using JSON-based dynamic storage.

---

## 🚀 Project Objective
The goal of this project is to **simulate a real-world banking environment** with:
- Account creation and deletion
- Deposits, withdrawals, and money transfers
- Secure PIN-based authentication
- JSON file-based data storage
- Dynamic transaction history

---

## 🛠️ Features
- 📝 **Account Creation:** Unique account number and PIN generation with email and phone verification.
- ❌ **Account Deletion:** Secure deletion with PIN verification.
- 💸 **Deposits & Withdrawals:** PIN-protected transactions with balance updates.
- 🔄 **Money Transfer:** Real-time money transfer between accounts.
- 📂 **Transaction History:** Each transaction (deposit, withdraw, send) is saved with time and date in a JSON file.
- ⚙️ **Dynamic File Handling:** System automatically creates required JSON files if they don’t exist.

---

## 🧰 Technologies Used
- Python
- JSON (for dynamic storage)
- `datetime` module for tracking transactions

---

## 📂 Project Structure
```text
Bank-Management-System/
│
├── main.py
├── users.json           # Account database (auto-generated)
├── users_hist.json      # Transaction history (auto-generated)
└── README.md
```

---

💻 How to Run
---
1. Make sure you have Python installed.

2. Run the project using:

    ```bash
    python main.py
    ```
3. The system will automatically create necessary JSON files.

4. You can create accounts, perform deposits, withdrawals, view account details, and send money between accounts.

---

🔐 Security Note
---
- All account operations are PIN-protected.

- Duplicate account creation and phone number validation are handled.

- Negative transactions are blocked by the system.

---

🤝 Contribution
---
- Feel free to fork this project and add:

- Interest calculation features

- User login/logout system

---

🧑‍💻 Author
---
Made with ❤️ by CodingWeapon

---

🔗 Connect
---
- Instagram: @codingweapon

- Threads: @codingweapon
