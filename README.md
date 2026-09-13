<div align="center">
⚡ RXVY RECON

A lightweight Python CLI for launching cybersecurity and reconnaissance tools from one terminal interface.

Created by rxvy · Version 2.0

<img src="image3.png" alt="RXVY RECON screenshot" width="850"> </div>
📖 Overview

RXVY RECON is a lightweight terminal-based cybersecurity toolkit that brings common reconnaissance and security-testing utilities together behind a simple interactive menu.

Instead of remembering commands and flags for every tool, select an option, enter your target, and let RXVY RECON launch the appropriate utility.

Designed for CTFs, personal labs, security research, and authorized penetration testing.

✨ Features
Tool	Purpose
Nmap	Network and port scanning
Nmap -O	Operating-system detection
Nikto	Web-server security testing
WHOIS	Domain and registration information
FTP	FTP connections
DIRB	Web-directory enumeration
Subfinder	Passive subdomain discovery
Holehe	Email-account existence checks
Sherlock	Username OSINT
SQLMap	SQL-injection testing
WPScan	WordPress security scanning
Additional Features
🔧 Built-in dependency installer
🧅 Tor management
🔐 VPN installation options
🌐 ProxyChains support
🎨 Custom ASCII interface
⚡ Lightweight Python implementation
🖥️ Interactive terminal menu
🛠️ Easy to customize and extend
📋 Requirements

RXVY RECON is primarily designed for Arch Linux / BlackArch.

Required
Python 3
sudo
pacman
proxychains
nmap
nikto
whois
ftp
dirb
subfinder
Optional
yay
holehe
sherlock
sqlmap
wpscan
Tor
VPN packages

The built-in installer can install many of the required dependencies automatically.

⚠️ Review installation commands before running them with root privileges. The installer may add external repositories or execute installation scripts.

🚀 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/rxvy-recon.git
cd rxvy-recon


Run RXVY RECON:

python3 rxvyrecon.py


You can then select the installation option from the menu to install the required dependencies.

🕹️ Usage

Start the program:

python3 rxvyrecon.py


You'll be presented with the RXVY RECON menu.

Example:

╔════════════════════════════════════════════════════════════╗
║                      RXVY RECON                            ║
╠════════════════════════════════════════════════════════════╣
║  1. Nmap                                                   ║
║  2. Nikto                                                  ║
║  3. WHOIS                                                  ║
║  4. FTP                                                    ║
║  5. DIRB                                                   ║
║  6. Subfinder                                              ║
║  7. Nmap OS Detection                                      ║
║  8. Tor                                                    ║
║  9. VPN                                                    ║
║ 10. Holehe                                                 ║
║ 11. Sherlock                                               ║
║ 12. SQLMap                                                 ║
║ 13. WPScan                                                 ║
║ 14. Exit                                                   ║
╚════════════════════════════════════════════════════════════╝


Select a tool and provide the target when prompted.

Example
Choose: 1
IP or URL: scanme.nmap.org


⚠️ Only scan systems and applications that you own or have explicit authorization to test.

🌐 ProxyChains

RXVY RECON can launch supported tools through ProxyChains.

Make sure ProxyChains is properly configured before using options that depend on it.

If you don't want to use ProxyChains, remove the proxychains portion from the corresponding command in the source code.

Important: ProxyChains/Tor does not make unauthorized activity legal or automatically guarantee anonymity.

🛠️ Customization

RXVY RECON is intentionally simple so you can modify it easily.

Ideas for customization:

🎨 Replace the ASCII banner
🌈 Change terminal colors
⚡ Add menu animations
🔧 Add additional tools
📝 Add command logging
⚙️ Add configuration files
👤 Add user profiles
🔍 Add automatic dependency detection
❌ Improve error handling
📊 Add scan-result summaries
💾 Add output-file support
🧩 Create tool-specific submenus
⚖️ Legal & Ethical Use

RXVY RECON is intended for:

CTFs
Personal cybersecurity labs
Security research
Educational purposes
Authorized penetration testing

Only use the tools against systems for which you have permission.

Unauthorized scanning, exploitation, credential attacks, or access attempts may be illegal.

The author is not responsible for misuse of this software.

🤝 Contributing

Contributions are welcome.

Feel free to:

Open issues
Submit pull requests
Suggest new tools
Improve the interface
Fix bugs
Improve documentation
🙌 Credits

Created and maintained by rxvy.

<div align="center">
⚡ RXVY RECON

Recon • Research • Learn • Secure

⭐ If you find RXVY RECON useful, consider starring the repository.

</div>
