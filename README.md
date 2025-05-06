# 🌐 ProxyBuster

**ProxyBuster** is a recursive URL enumerator designed to explore web directories and endpoints. It uses a wordlist to test paths and displays HTTP response codes with color-coded output for better readability.

---

## 📌 Features

- **Recursive Enumeration**: Automatically explores subdirectories up to a configurable depth.
- **Color-Coded Output**: Displays HTTP response codes in different colors:
  - **Green** (`200`): Success.
  - **Yellow** (`301-308`): Redirections.
  - **Orange** (`400-430`): Client errors.
  - **Purple** (`500-511`): Server errors.
- **Customizable Settings**: Easily configure the target URL, wordlist, and maximum recursion depth.

---

## 🛠️ Requirements

- Python 3.6+
- `requests` library (install with `pip install requests`)

---

## 🚀 Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/proxybuster.git
   cd proxybuster
   ```

2. **Edit the script**:
   - Update the `target` variable with the URL you want to scan.
   - Set the path to your wordlist in the `wordlist` variable.
   - Adjust the `max_depth` variable if needed.

3. **Run the script**:
   ```bash
   python3 Untitled-2.py
   ```

4. **Example Output**:
   ```plaintext
   [+] Scan: http://example.com/ (depth 1)
   [200] http://example.com/admin/
   [301] http://example.com/login/
   [404] http://example.com/unknown/
   ```

---

## 📂 File Structure

```bash
proxybuster/
├── Untitled-2.py       # The main script
├── README.md           # This file
└── wordlist.txt        # Example wordlist (optional)
```

---

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized penetration testing only.  
**Do not use it against systems without explicit permission.**

---

## ✉️ Author

Developed by a security enthusiast passionate about web application security and automation.  
Feel free to contribute, fork, or open an issue!
