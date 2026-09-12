A lightweight Python CLI for launching common cybersecurity and reconnaissance tools through ProxyChains.
 
Created by **rxvy**.
 
## Features
 
- Nmap — network and port scanning
- Nikto — web server security testing
- WHOIS — domain registration information
- FTP — FTP connections
- DIRB — web directory enumeration
- Subfinder — passive subdomain discovery
- Nmap `-O` — operating-system detection
- Built-in dependency installer
- Simple interactive terminal menu
- Customizable ASCII banner and colors
 
## Requirements
 
Designed primarily for Arch Linux / BlackArch.
 
The project uses:
 
- Python 3
- ProxyChains
- Nmap
- Nikto
- WHOIS
- inetutils
- DIRB
- Subfinder
 
## Installation
 
Clone the repository:
 
```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME
 
Run the program:
 
python3 cybersec.py
 
You can use the install option from the menu to install the required tools on Arch Linux.
Usage
 
Start the program:
 
python3 cybersec.py
 
Select an option from the menu and enter the target when prompted.
 
Example:
 
Choose: 1
ip or url: scanme.nmap.org
 
Only test targets where you have permission.
Customization
 
ANON CYBER CLI is designed to be easy to modify.
 
You can:
 
    Change the ASCII banner
    Change terminal colors
    Add new tools
    Remove tools
    Add new menu options
    Add error handling
    Add logging
    Add configuration options
    Improve the interface
    Add your own features
 
Legal & Ethical Use
 
This project is intended for educational purposes, CTFs, security research, and authorized security testing.
 
Only use these tools against systems you own or systems for which you have explicit permission to test.
 
Do not scan or test websites, networks, servers, or devices without authorization.
 
The author is not responsible for misuse of this software.
Credits
 
Created and maintained by rxvy.
 
ANON CYBER CLI is an open-source project. You are free to study, modify, improve, and contribute to the project according to the terms of the included license.
License
 
This project is licensed under the MIT License.
 
See the LICENSE file for details.
 
⭐ If you find ANON CYBER CLI useful, consider starring the repository!
