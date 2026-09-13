<div align="center">
⚡ RXVY RECON

A lightweight Python CLI for reconnaissance and authorized security testing.

Created by rxvy · Version 2.0

</div>
📖 Overview

RXVY RECON is a lightweight terminal-based Python CLI that brings commonly used reconnaissance and security-testing utilities together under one interactive menu.

Instead of remembering individual commands and options, choose a tool, provide your target, and let RXVY RECON launch it for you.

Designed for:

🔬 Security research
🧪 CTFs and intentionally vulnerable labs
🛡️ Authorized penetration testing
📚 Cybersecurity learning
🔎 Reconnaissance workflows

RXVY RECON is intentionally simple and customizable, making it easy to add your own tools, commands, and workflows.

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
🔧 Built-in dependency installation
🧅 Tor service controls
🔐 VPN installation options
🔗 ProxyChains support
🖥️ Interactive terminal interface
🎨 Custom ASCII banners and colors
⚙️ Easy-to-modify command structure
📝 Simple Python source code
🚪 Quick menu exit with Q
💻 Requirements

RXVY RECON is primarily designed for:

Arch Linux
BlackArch Linux

Basic requirements:

Python 3
sudo
pacman
ProxyChains
yay for AUR packages

Depending on which features you use, additional tools may include:

nmap
nikto
whois
inetutils
dirb
subfinder
holehe
sherlock
sqlmap
wpscan
tor


The built-in installer can install many of the required dependencies.

⚠️ The installer may download and execute third-party installation scripts with elevated privileges. Review scripts and verify their sources before running them.

🚀 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/rxvy-recon.git
cd rxvy-recon


Run RXVY RECON:

python3 rxvyrecon.py


Then select the installation option from the menu.

Manual Installation

If you prefer installing dependencies yourself:

sudo pacman -S nmap nikto whois inetutils dirb subfinder proxychains sqlmap


AUR tools can be installed separately with yay where available.

🕹️ Usage

Start the program:

python3 rxvyrecon.py


You'll be presented with the RXVY RECON menu.

Example:

╔══════════════════════════════════════════╗
║              RXVY RECON                  ║
╠══════════════════════════════════════════╣
║ 1  - Nmap                                ║
║ 2  - Nikto                               ║
║ 3  - WHOIS                               ║
║ 4  - FTP                                 ║
║ 5  - DIRB                                ║
║ 6  - Subfinder                           ║
║ 7  - Nmap OS Detection                   ║
║ 8  - Tor                                 ║
║ 9  - VPN                                 ║
║ 10 - Holehe                              ║
║ 11 - ZPhisher                            ║
║ 12 - Sherlock                            ║
║ 13 - SQLMap                              ║
║ 14 - WPScan                              ║
║ Q  - Exit                                ║
╚══════════════════════════════════════════╝


Select an option and provide the requested target.

For example:

Choose: 1
ip or url: scanme.nmap.org


⚠️ Only scan or test systems that you own or have explicit permission to assess.

🧅 ProxyChains

Several RXVY RECON tools are designed to run through ProxyChains.

Make sure ProxyChains is properly configured before using those options.

You can check your configuration with:

proxychains curl https://example.com


If you don't want to use ProxyChains, modify the corresponding subprocess.run() commands in the source code and remove the proxychains argument.

Important: ProxyChains does not make unauthorized activity legal or guarantee anonymity.

🛠️ Customization

RXVY RECON is designed to be modified.

Ideas for customization:

🎨 Replace the ASCII banner
🌈 Change terminal colors
➕ Add new tools
➖ Remove unwanted tools
⚡ Create new workflows
📋 Add command history
📝 Add logging
⚙️ Add configuration files
🔧 Improve dependency detection
🚦 Add tool availability checks
🖥️ Improve the terminal interface
📊 Add scan-result summaries

Adding a new menu option is as simple as adding another command handler to the main loop.

⚠️ Legal & Ethical Use

RXVY RECON is intended for legitimate cybersecurity use only.

Use this software for:

Your own systems
Authorized penetration tests
CTF competitions
Security laboratories
Intentionally vulnerable environments
Authorized security research

Do not use RXVY RECON to scan, attack, enumerate, or access systems without permission.

Unauthorized security testing may violate laws, contracts, or network policies.

The author is not responsible for damage, misuse, or illegal activity involving this software.

🤝 Contributing

Contributions are welcome.

You can help by:

Reporting bugs
Suggesting features
Improving documentation
Adding new tools
Improving the interface
Submitting pull requests

If you add a new tool, keep the implementation simple and document the required dependencies.

📜 License

This project is open source.

See the repository's license file for the applicable license and usage terms.

👤 Credits

Created and maintained by rxvy.

<div align="center">
⚡ RXVY RECON

Recon. Research. Learn.

⭐ If you find RXVY RECON useful, consider starring the repository.

</div>
