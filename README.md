<div align="center">

# ⚡ ANON CYBER CLI

**A lightweight Python CLI for launching common cybersecurity and reconnaissance tools through ProxyChains.**

Created by **rxvy** · Version 2.0

![ANON CYBER CLI screenshot](image3.png)

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
| **Holehe** | Check an email against site logins |

Plus:
- 🔧 Built-in dependency installer (Arch/BlackArch)
- 🧅 Tor install / enable / disable / restart from the menu
- 🔐 VPN installer (Mullvad, Proton, Riseup)
- 🖥️ Simple interactive terminal menu with a typing intro
- 🎨 Customizable ASCII banner and colors
- 🔗 All traffic routed through ProxyChains

---

## 📋 Requirements

Designed primarily for **Arch Linux / BlackArch**.

- Python 3
- ProxyChains (configured and connected to a proxy before use)
- Nmap
- Nikto
- WHOIS (inetutils)
- FTP client
- DIRB
- Subfinder
- Holehe
- `yay` (for AUR packages, used by the Tor/VPN/Holehe install steps)

Missing tools can be installed automatically via the built-in `install` option in the menu.

> ⚠️ The `install` option also downloads and runs BlackArch's `strap.sh` as root. This script's integrity is **not verified** by this tool (no hash check) — you'll see an in-app warning before confirming. Review [BlackArch's install docs](https://blackarch.org) if you want to verify it yourself first.

---

## 🚀 Installation

Download `anoncyber.py` from this repository, then run it:

```bash
python3 anoncyber.py
```

From the menu, select `install` to pull in the required tools (Arch/BlackArch only).

---

## 🕹️ Usage

Launch the CLI:

```bash
python3 anoncyber.py
```

Make sure ProxyChains is installed and pointed at a working proxy — the menu options assume it's available and will fail otherwise. (If you don't want to use ProxyChains, remove the `proxychains` argument from the relevant commands in the source.)

Pick a numbered option, then enter your target when prompted.

**Example:**

Choose: 1
ip or url: scanme.nmap.org


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
- Unauthorized scanning is illegal in most jurisdictions.
- The author is not responsible for misuse of this software.

---

## 🙌 Credits

Created and maintained by **rxvy**.

---

<div align="center">

⭐ If you find **ANON CYBER CLI** useful, consider starring the repository!

</div>
