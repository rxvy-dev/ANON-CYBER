<div align="center">
⚡ RXVY RECON
Recon • Research • Security

A lightweight terminal-based cybersecurity toolkit for Arch Linux.

Built by rxvy · v2.0

<img src="image3.png" alt="RXVY RECON" width="900"> <br>







</div>
⚡ What is RXVY RECON?

RXVY RECON is a simple terminal interface for launching commonly used cybersecurity, reconnaissance, and security-testing utilities.

Instead of remembering dozens of commands, RXVY RECON gives you a single menu:

             RXVY RECON
        ─────────────────────

        [01] Nmap
        [02] Nikto
        [03] WHOIS
        [04] FTP
        [05] DIRB
        [06] Subfinder
        [07] Nmap OS Detection
        [08] Tor
        [09] VPN
        [10] Holehe
        [11] Sherlock
        [12] SQLMap
        [13] WPScan
        [14] Exit


Choose a tool → enter your target → run.

Designed for CTFs, labs, learning, research, and authorized security testing.

🧰 Tools
Tool	Category	Function
Nmap	Network	Port & service scanning
Nmap -O	Network	OS detection
Nikto	Web	Web-server testing
WHOIS	OSINT	Domain information
FTP	Network	FTP connections
DIRB	Web	Directory enumeration
Subfinder	Recon	Passive subdomain discovery
Holehe	OSINT	Email account checks
Sherlock	OSINT	Username searching
SQLMap	Web	SQL injection testing
WPScan	Web	WordPress security testing
🔥 Features
✓ Interactive terminal interface
✓ ProxyChains support
✓ Tor management
✓ VPN installation menu
✓ Automatic dependency installation
✓ Nmap OS detection
✓ Web reconnaissance tools
✓ OSINT utilities
✓ WordPress scanning
✓ SQL injection testing
✓ Customizable source code
✓ Designed for Arch / BlackArch

🖥️ Requirements

RXVY RECON is primarily designed for:

Arch Linux / BlackArch

Core
Python 3
pacman
sudo
ProxyChains

Recon
nmap
nikto
whois
inetutils
dirb
subfinder

Optional
yay
holehe
sherlock
sqlmap
wpscan
tor


The built-in installer can handle many of these dependencies.

🚀 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/rxvy-recon.git
cd rxvy-recon


Launch:

python3 rxvyrecon.py


Then use the install option from the main menu.

🎯 Usage

Start RXVY RECON:

python3 rxvyrecon.py


You'll see the interactive menu.

For example:

Choose: 1
ip or url: scanme.nmap.org


RXVY RECON then launches the corresponding tool.

🌐 ProxyChains

Several RXVY RECON options are designed to run through ProxyChains.

Configure ProxyChains before using those options.

ProxyChains
     │
     ▼
 RXVY RECON
     │
     ├── Nmap
     ├── Nikto
     ├── DIRB
     └── Subfinder


ProxyChains or Tor does not make unauthorized activity legal or guarantee anonymity.

🧅 Tor & VPN

RXVY RECON includes a small menu for managing Tor and installing supported VPN packages.

Available options include:

TOR
 ├── Enable
 ├── Disable
 └── Restart

VPN
 ├── Mullvad
 ├── Proton VPN
 └── Riseup VPN

🎨 Customization

The project is intentionally lightweight.

You can easily modify:

ASCII banners
Colors
Menu layout
Animations
Tools
Commands
Dependency installation
Error handling
Logging
Configuration
Output handling

Want another tool?

Add it to the menu and wire it into subprocess.run().

⚠️ Legal

RXVY RECON is intended for:

CTFs
Cybersecurity education
Personal labs
Security research
Authorized penetration testing

Only test systems you own or have explicit permission to test.

Do not use RXVY RECON to gain unauthorized access, attack systems, steal credentials, or disrupt services.

The author is not responsible for misuse of this project.

🤝 Contributing

Found a bug?

Have an idea?

Want to add another tool?

Feel free to:

→ Open an issue
→ Submit a pull request
→ Improve the interface
→ Add new tools
→ Improve documentation
→ Fix bugs

<div align="center">
⚡ RXVY RECON

RECON • RESEARCH • LEARN • SECURE

Created and maintained by rxvy

⭐ Star the repository if you find it useful.

</div>
