
# ⌨️ Keyboard Input Logger & Basic Detector

A modern Python-based educational cybersecurity project that demonstrates **keyboard input logging within the application** and **basic suspicious process detection**.

> ⚠️ This project is developed **only for educational and defensive cybersecurity learning purposes.** It does **not** capture system-wide keyboard input.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-success)
![Security](https://img.shields.io/badge/Cybersecurity-Educational-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Features

- ✅ Keyboard Input Logger
- ✅ Automatic `key.txt` Log File Creation
- ✅ Timestamp for Every Logged Input
- ✅ Basic Suspicious Process Detection
- ✅ Menu Driven Interface
- ✅ Lightweight & Easy to Use
- ✅ Beginner Friendly
- ✅ Defensive Cybersecurity Project

---

# ⚙️ Requirements

- Python 3.x
- psutil

Install dependency

```bash
pip install psutil
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Keylogger.git
```

Go into the project folder

```bash
cd Keylogger
```

Run the application

```bash
python keylogger.py
```

---

# 📂 Project Structure

```
Keylogger/
│── keylogger.py
│── key.txt
└── README.md
```

---

# 📝 Keyboard Input Logger

This module records **only the text entered inside this application**.

Features

- Automatic log file creation
- Timestamp logging
- Unlimited logging
- Type `exit` to stop

Example

```
>> Hello

>> Cyber Security

>> Python

>> exit
```

Generated Log

```
[2026-07-08 10:15:21] Hello

[2026-07-08 10:15:30] Cyber Security

[2026-07-08 10:15:45] Python
```

---

# 🔍 Basic Keylogger Detector

The detector scans currently running processes and searches for suspicious keywords such as

- keylogger
- logger
- hook
- spy
- monitor

Example Output

```
Scanning Running Processes...

[!] Suspicious Process : keylogger.exe
```

or

```
No suspicious process found.
```

---

# 💻 Built With

- Python
- psutil
- os
- datetime

---

# ▶️ Run

```bash
python keylogger.py
```

---

# 📷 Sample Menu

```
==================================================
      KEYBOARD LOGGER & BASIC DETECTOR
==================================================

1. Start Keyboard Input Logger
2. Basic Keylogger Detector
3. Exit
```

---

# 🎯 Project Objective

This project demonstrates:

- Python File Handling
- User Input Logging
- Process Enumeration
- Basic Suspicious Process Detection
- Defensive Cybersecurity Concepts

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create your feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Jiten Kumar Behera**

### GitHub

https://github.com/ImJitenBehera

### Repository

https://github.com/ImJitenBehera/keylogger

---

⭐ If you like this project, don't forget to Star the repository.
