# Password Generator & Manager

A command-line password tool built in Python. Checks password strength, generates random secure passwords, and stores saved passwords behind a master password login.

## Features

- **Password Strength Checker** — checks a password against length, uppercase, lowercase, number, and special character requirements.
- **Password Generator** — generates a random password of a chosen length using letters, numbers, and special characters.
- **Password Manager** — save and view passwords per service/site, stored locally in `passwords.json`.
- **Master Password Login** — the manager is protected by a master password. The master password itself is never stored in plain text; it's hashed with `hashlib.pbkdf2_hmac` (SHA-256, salted) and saved in `master.json`.

## Requirements

- Python 3.x (no external libraries — uses only the standard library: `random`, `json`, `os`, `sys`, `hashlib`)

## Running from source

```bash
python main.py
```

On first run, you'll be asked to set a master password. On every run after that, you'll need to enter it correctly to access the menu.

## Running the compiled executable

Pre-built executables are available for Windows and Linux (see Releases).

- **Windows**: run `main.exe`
- **Linux**: run `./main`

The executable creates `passwords.json` and `master.json` in the same folder it's run from. Don't move the executable without its data files if you want to keep your saved passwords.

## Menu options

1. **Check Password** — enter a password and a required length to see if it meets strength requirements.
2. **Generate Password** — enter a desired length to generate a random password.
3. **Save Password** — save a password for a service/site. Leave the password blank to auto-generate one.
4. **View Saved Passwords** — list all saved service/password pairs.
5. **Exit** — close the program.

## Security notes

- The master password is hashed (not stored in plain text) using PBKDF2-HMAC-SHA256 with a random salt.
- Saved service passwords in `passwords.json` are currently stored in **plain text**. Encryption for this file is planned but not yet implemented — don't rely on this tool for sensitive passwords until that's added.
- Never share your own `passwords.json` or `master.json` files — each user should start with a fresh copy of the executable and set up their own master password on first run.

## Building the executable yourself

Requires [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

The executable will be created in the `dist/` folder (`main.exe` on Windows, `main` on Linux — build separately on each OS, PyInstaller does not cross-compile).

## Roadmap

 Encrypt saved service passwords (e.g. using `cryptography`'s Fernet)
 Limit master password attempts with lockout/delay
