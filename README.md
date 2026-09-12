<div align="center">

# ⚡ ANON CYBER CLI

**A lightweight Python CLI for launching common cybersecurity and reconnaissance tools through ProxyChains.**

Created by **rxvy**

</div>

---

## 📖 Overview

ANON CYBER CLI wraps a handful of well-known recon and security-testing tools behind a single, simple terminal menu — routing traffic through ProxyChains by default. Instead of memorizing flags for Nmap, Nikto, WHOIS, DIRB, and Subfinder, pick a number and enter a target.

Built for quick, authorized recon work: CTFs, labs, and pentests where you already have permission to test.

---

## ✨ Features

| Tool | Purpose |
|------|---------|
| **Nmap** | Network and port scanning |
| **Nmap `-O`** | Operating system detection |
| **Nikto** | Web server security testing |
| **WHOIS** | Domain registration lookups |
| **FTP** | Quick FTP connections |
| **DIRB** | Web directory enumeration |
| **Subfinder** | Passive subdomain discovery |

Plus:
- 🔧 Built-in dependency installer
- 🖥️ Simple interactive terminal menu
- 🎨 Customizable ASCII banner
- 🔗 All traffic routed through ProxyChains

---

## 📋 Requirements

Designed primarily for **Arch Linux / BlackArch**.

- Python 3
- ProxyChains
- Nmap
- Nikto
- WHOIS
- inetutils
- DIRB
- Subfinder

Missing tools can be installed automatically via the built-in installer in the menu.

---

## 🚀 Installation

Download `cybersec.py` from this repository, then run it:

```bash
python3 cybersec.py
```

From the menu, select the install option to pull in the required tools on Arch Linux.

---

## 🕹️ Usage

Launch the CLI:

```bash
python3 cybersec.py
```

Pick a numbered option, then enter your target when prompted.

**Example:**

```
Choose: 1
ip or url: scanme.nmap.org
```

> ⚠️ Only test targets you own or have explicit permission to test.

---

## 🛠️ Customization

ANON CYBER CLI is intentionally simple so it's easy to extend. Common tweaks:

- Change the ASCII banner
- Change terminal colors
- Add or remove tools
- Add new menu options
- Add error handling and logging
- Add configuration options
- Improve the interface

---

## ⚖️ Legal & Ethical Use

This project is intended for **educational purposes, CTFs, security research, and authorized security testing only**.

- Only run these tools against systems you own or have explicit written permission to test.
- Do not scan or test websites, networks, servers, or devices without authorization.
- The author is not responsible for misuse of this software.

---

## 🙌 Credits

Created and maintained by **rxvy**.

---

<div align="center">

⭐ If you find **ANON CYBER CLI** useful, consider starring the repository!

</div>
