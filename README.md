<div align="center">

# ⚡ RXVY RECON

**Recon • Research • Security**

A lightweight terminal-based cybersecurity toolkit for Arch Linux.

![Platform](https://img.shields.io/badge/platform-Arch%20%2F%20BlackArch-1793D1?logo=arch-linux&logoColor=white)
![Python](https://img.shields.io/badge/python-3-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-Educational%20Use-orange)
![Version](https://img.shields.io/badge/version-v3.0-success)

<img src="image3.png" alt="RXVY RECON" width="900">

</div>

---

## ⚡ What is RXVY RECON?

**RXVY RECON** is a simple terminal interface for launching commonly used cybersecurity, reconnaissance, and security-testing utilities — without the hassle of memorizing dozens of commands and flags.

One menu. Every tool you need.

```
                         RXVY-RECON v3.0
        ══════════════════════════════════════════════

        [1]  Nmap              Scan for open ports
        [2]  Nikto             Web server security scanner
        [3]  WHOIS             Domain / IP registration info
        [4]  FTP               Connect to FTP servers
        [5]  DIRB              Web directory enumeration
        [6]  Subfinder         Passive subdomain discovery
        [7]  Nmap -O           Operating-system detection

        [8]  Tor               Tor service / proxy management
        [9]  VPN Manager       Install and manage VPN options

        [10] Holehe            Check email account exposure
        [11] ZPhisher          Phishing simulation tool
        [12] Sherlock          Username OSINT

        [13] SQLMap            SQL injection testing
        [14] WPScan            WordPress security scanner

        [I]  Install Dependencies         [Q] Exit
```

Choose a tool → enter your target → run.

Designed for CTFs, labs, learning, research, and **authorized** security testing.

---

## 🧰 Tools

| Tool | Category | Function |
|------|----------|----------|
| **Nmap** | Network | Port & service scanning |
| **Nmap -O** | Network | OS detection |
| **Nikto** | Web | Web-server testing |
| **WHOIS** | OSINT | Domain information |
| **FTP** | Network | FTP connections |
| **DIRB** | Web | Directory enumeration |
| **Subfinder** | Recon | Passive subdomain discovery |
| **Tor** | Anonymity | Enable / disable / restart the Tor service |
| **VPN Manager** | Anonymity | Installs Mullvad, Proton VPN, or Riseup VPN |
| **Holehe** | OSINT | Email account checks |
| **ZPhisher** | Social Engineering | Phishing simulation for awareness training |
| **Sherlock** | OSINT | Username searching |
| **SQLMap** | Web | SQL injection testing |
| **WPScan** | Web | WordPress security testing |

> ⚠️ **ZPhisher** creates phishing-style login pages for **authorized security-awareness testing only** — e.g. testing your own organization's phishing resilience with informed consent. Using it against people or systems without explicit authorization is illegal in most jurisdictions.

---

## 🔥 Features

- ✅ Interactive terminal interface
- ✅ ProxyChains support
- ✅ Tor management
- ✅ VPN installation menu
- ✅ Automatic dependency installation
- ✅ Nmap OS detection
- ✅ Web reconnaissance tools
- ✅ OSINT utilities
- ✅ Phishing-awareness simulation (ZPhisher)
- ✅ WordPress scanning
- ✅ SQL injection testing
- ✅ Customizable source code
- ✅ Designed for Arch / BlackArch

---

## 🖥️ Requirements

RXVY RECON is primarily designed for **Arch Linux / BlackArch**.

<table>
<tr>
<td valign="top">

**Core**
- Python 3
- pacman
- sudo
- ProxyChains

</td>
<td valign="top">

**Recon (pacman)**
- nmap
- nikto
- whois
- inetutils
- dirb
- subfinder
- sqlmap
- python-requests

</td>
<td valign="top">

**Optional (yay / manual)**
- holehe
- sherlock
- wpscan
- tor
- zphisher (cloned from GitHub)
- BlackArch strap.sh

</td>
</tr>
</table>

> The `[I] Install Dependencies` menu option automates most of this — installing pacman packages, pulling `holehe`/`sherlock` via `yay`, running the official BlackArch `strap.sh` bootstrap script, and cloning the ZPhisher repo.
>
> ⚠️ The installer downloads and executes `strap.sh` directly from blackarch.org. This tool does **not** verify its SHA256 checksum before running it — review the script yourself first if you want to confirm it hasn't been tampered with or corrupted in transit.

---

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/rxvy-recon.git
cd rxvy-recon
```

**2. Launch**

```bash
python3 rxvyrecon.py
```

**3. Install dependencies**

Use the install option from the main menu.

---

## 🎯 Usage

Start RXVY RECON:

```bash
python3 rxvyrecon.py
```

You'll see the interactive menu. For example:

```
Choose: 1
ip or url: scanme.nmap.org
```

RXVY RECON then launches the corresponding tool.

---

## 🌐 ProxyChains

Several RXVY RECON options are designed to run through ProxyChains. Configure ProxyChains **before** using those options.

```
ProxyChains
     │
     ▼
 RXVY RECON
     │
     ├── Nmap
     ├── Nikto
     ├── DIRB
     └── Subfinder
```

> ⚠️ ProxyChains or Tor does not make unauthorized activity legal or guarantee anonymity.

---

## 🧅 Tor & VPN

RXVY RECON includes a small menu (options `[8]` and `[9]`) for managing Tor and installing supported VPN packages.

```
TOR ([8])                     VPN ([9])
 ├── 1  Enable                 ├── 1  Mullvad     (pacman)
 ├── 2  Disable                ├── 2  Proton VPN  (GUI or CLI, pacman)
 ├── 3  Restart                ├── 3  Riseup VPN  (AUR — requires yay)
 └── exit                      └── exit
```

Tor actions ask for a **y/n confirmation** before installing or changing the service state. Riseup VPN requires `yay` to be installed first.

---

## 🎨 Customization

The project is intentionally lightweight and easy to modify:

- ASCII banners
- Colors
- Menu layout
- Animations
- Tools
- Commands
- Dependency installation
- Error handling
- Logging
- Configuration
- Output handling

Want another tool? Add it to the menu and wire it into `subprocess.run()`.

---

## ⚠️ Legal

RXVY RECON is intended for:

- CTFs
- Cybersecurity education
- Personal labs
- Security research
- Authorized penetration testing

**Only test systems you own or have explicit permission to test.**

Do not use RXVY RECON to gain unauthorized access, attack systems, steal credentials, or disrupt services.

**ZPhisher specifically** must only be used against your own accounts/infrastructure or as part of a sanctioned, consent-based phishing-awareness exercise (e.g. an internal security team testing employees with prior authorization). Using it to target real third parties without consent is credential theft/fraud in most jurisdictions.

The author is not responsible for misuse of this project.

---

## 🤝 Contributing

Found a bug? Have an idea? Want to add another tool?

Feel free to:

- 🐛 Open an issue
- 🔧 Submit a pull request
- 🎨 Improve the interface
- 🛠️ Add new tools
- 📖 Improve documentation
- 🩹 Fix bugs

---

<div align="center">

### ⚡ RXVY RECON

**RECON • RESEARCH • LEARN • SECURE**

Created and maintained by **rxvy**

⭐ *Star the repository if you find it useful.*

</div>
