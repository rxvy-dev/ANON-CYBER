# ============================================================
#                     ANON CYBER CLI
# ============================================================
#
#   Created by : rxvy
#   Version    : 1.0
#   License    : Open Source
#
# ------------------------------------------------------------
#   Description
# ------------------------------------------------------------
#
#   A lightweight Python command-line interface for launching
#   common cybersecurity and reconnaissance tools through
#   ProxyChains.
#
#   Built to make everyday recon utilities faster to reach —
#   pick an option from the menu, enter a target, done.
#
# ------------------------------------------------------------
#   Tools Included
# ------------------------------------------------------------
#
#   Nmap        - Network and port scanning
#   Nmap -O     - Operating-system detection
#   Nikto       - Web server security testing
#   WHOIS       - Domain registration information
#   FTP         - FTP connections
#   DIRB        - Web directory enumeration
#   Subfinder   - Passive subdomain discovery
#
# ------------------------------------------------------------
#   Customization
# ------------------------------------------------------------
#
#   This project is open source and built to be modified.
#   Ideas for extending it:
#
#     - Swap the ASCII banner and color scheme
#     - Add or remove tools from the menu
#     - Add new menu options or workflows
#     - Improve error handling
#     - Add logging
#     - Add configuration/profile support
#     - Improve the interface
#     - Add your own features
#
# ------------------------------------------------------------
#   Legal & Ethical Use
# ------------------------------------------------------------
#
#   For educational use, CTFs, security research, and
#   authorized security testing only.
#
#   Only run these tools against systems you own or have
#   explicit permission to test. Unauthorized scanning is
#   illegal in most jurisdictions.
#
#   The author is not responsible for any misuse of this
#   software.
#
# ------------------------------------------------------------
#   Contributing
# ------------------------------------------------------------
#
#   This is an open-source project — forks, pull requests,
#   and improvements are welcome.
#
# ------------------------------------------------------------
#   Credits
# ------------------------------------------------------------
#
#   Created and maintained by rxvy
#
# ============================================================

 
RED = "\033[91m"
 
import subprocess
 
def menu():
    print(RED + """
 
  ▄▄▄▄   ▄▄▄    ▄▄▄   ▄▄▄▄▄   ▄▄▄    ▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄   ▄▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄     
▄██▀▀██▄ ████▄  ███ ▄███████▄ ████▄  ███   ███▀▀▀▀▀ ███   ███ ███▀▀███▄ ███▀▀▀▀▀ ███▀▀███▄   
███  ███ ███▀██▄███ ███   ███ ███▀██▄███   ███      ▀███▄███▀ ███▄▄███▀ ███▄▄    ███▄▄███▀   
███▀▀███ ███  ▀████ ███▄▄▄███ ███  ▀████   ███        ▀███▀   ███  ███▄ ███      ███▀▀██▄    
███  ███ ███    ███  ▀█████▀  ███    ███   ▀███████    ███    ████████▀ ▀███████ ███  ▀███   
 

YOU NEED PROXYCHAINS CONNECTED TO A PROXY FOR THIS TO WORK IF U DONT THEN REMOVE ALL MENTIONS OF "proxychain"!

install = install all needed programs.                                                                                             
1 = proxychains nmap (ip) (scans for open ports)
2 = proxychains nikto (website)
3 = proxychains whois (ip), (website)
4 = proxychains ftp (website with ftp anomynous login enabled found in nmap and more.)         
5 = proxychains dirb (website)
6 = proxychains subfinder -d (website)
7 = proxychains nmap -O (ip), (website) (tries to detect the operating system the server is currently running)
8 = exit
    """)
 
def main():
   while True:
        menu()
 
        choice = input("Choose:")
 
        if choice == '1':
            nmapchoice = input("ip or url:")
            subprocess.run(['proxychains', 'nmap', nmapchoice])
 
        elif choice == '2':
            niktochoice = input("ip or url:")
            subprocess.run(['proxychains', 'nikto', '-host', niktochoice])
 
        elif choice == '3':
            whoischoice = input("website/url:")
            subprocess.run(['proxychains', 'whois', whoischoice])
 
        elif choice == '4':
            ftpchoice = input("url:")
            subprocess.run(['proxychains', 'ftp', ftpchoice])
 
        elif choice == '5':
            dirbchoice = input("url:")
            subprocess.run(['proxychains', 'dirb', dirbchoice])
 
        elif choice == '6':
            subfinderchoice = input("website/url:")
            subprocess.run(['proxychains', 'subfinder', '-d', subfinderchoice])
 
 
        elif choice == '7':
            nmapOchoice = input("ip or url:")
 
#       SUDO IS NEEDED FOR -O ON NMAP!
 
            subprocess.run(['sudo', 'proxychains', 'nmap', '-O', nmapOchoice])
 
        elif choice == "install":
            installchoice = input("are u sure you want to install? (y/n):")
            if installchoice == 'y':
                subprocess.run(['sudo', 'pacman', '-S', 'nmap', 'nikto', 'whois', 'inetutils', 'dirb', 'subfinder', 'proxychains'])
 
            else:
                 print("OKAY")
 
        elif choice == '8':
            break

        else:
             print("please pick a valid option.")
main()
