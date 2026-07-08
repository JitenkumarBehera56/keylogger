import os
import psutil
from datetime import datetime

LOG_FILE = "key.txt"

SUSPICIOUS = [
    "keylogger",
    "hook",
    "logger",
    "spy",
    "monitor"
]


def banner():
    print("=" * 50)
    print("      KEYBOARD LOGGER & BASIC DETECTOR")
    print("=" * 50)


def log_input():
    print("\nType anything.")
    print("Type 'exit' to stop.\n")

    while True:
        text = input(">> ")

        if text.lower() == "exit":
            print("Logging Stopped.")
            break

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}\n"
            )


def detect_process():
    print("\nScanning Running Processes...\n")

    found = False

    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']

            if name:
                for word in SUSPICIOUS:
                    if word.lower() in name.lower():
                        print("[!] Suspicious Process :", name)
                        found = True

        except:
            pass

    if not found:
        print("No suspicious process found.")


while True:
    banner()

    print("\n1. Start Keyboard Input Logger")
    print("2. Basic Keylogger Detector")
    print("3. Exit")

    choice = input("\nSelect : ")

    if choice == "1":
        log_input()

    elif choice == "2":
        detect_process()

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid Choice.")
