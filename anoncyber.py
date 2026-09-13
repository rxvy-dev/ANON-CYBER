# ============================================================
#                     ANON CYBER CLI
# ============================================================
#
#   Created by : rxvy
#   Version    : 2.0
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
#    BEING HONEST THIS TYPING ANIMATION WAS MADE BY CLAUDE, JUST THIS LINE I JUST DONT KNOW HOW TO DO THIS IN PYTHON YET!
type_fx = lambda text, delay=0.005: [((sys.stdout.write(c), sys.stdout.flush(), time.sleep(delay))) for c in text]

# for commands
import subprocess
# for animations.
import sys
import time
def warn():
    type_fx("""
   For educational use, CTFs, security research, and
   authorized security testing only.

   Only run these tools against systems you own or have
   explicit permission to test. Unauthorized scanning is
   illegal in most jurisdictions.

   The author is not responsible for any misuse of this
   software.""")
    
def menu():
    print(RED + """
 
  ▄████████ ███▄▄▄▄    ▄██████▄  ███▄▄▄▄         ▄████████  ▄██   ▄   ▀█████████▄     ▄████████    ▄████████ 
  ███    ███ ███▀▀▀██▄ ███    ███ ███▀▀▀██▄      ███    ███ ███   ██▄   ███    ███   ███    ███   ███    ███ 
  ███    ███ ███   ███ ███    ███ ███   ███      ███    █▀  ███▄▄▄███   ███    ███   ███    █▀    ███    ███ 
  ███    ███ ███   ███ ███    ███ ███   ███      ███        ▀▀▀▀▀▀███  ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███   ███ ███    ███ ███   ███      ███        ▄██   ███ ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ███ ███   ███ ███    ███ ███   ███      ███    █▄  ███   ███   ███    ██▄   ███    █▄  ▀███████████ 
  ███    ███ ███   ███ ███    ███ ███   ███      ███    ███ ███   ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀   ▀█   █▀   ▀██████▀   ▀█   █▀       ████████▀   ▀█████▀  ▄█████████▀    ██████████   ███    ███ 
                                                                                                  ███    ███ (anonymous cybersecurity.)
|----------------------------------------------------------------|
|YOU NEED PROXYCHAINS CONNECTED TO A PROXY FOR                   |
|THIS TO WORK IF U DONT THEN REMOVE ALL MENTIONS OF "proxychain"!| 
|----------------------------------------------------------------|
install = install all needed programs.                                                                                             
1 = proxychains nmap (ip) (scans for open ports)
2 = proxychains nikto (website)
3 = proxychains whois (ip), (website)
4 = proxychains ftp (website with ftp anomynous login enabled found in nmap and more.)         
5 = proxychains dirb (website)
6 = proxychains subfinder -d (website)
7 = proxychains nmap -O (ip), (website) (tries to detect the operating system the server is currently running)
8 = TOR (proxy)
9 = Choose and install vpns!
10 = holehe (see emails website logins)
11 = exit

    """)
 
def main():
   warn()
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

        elif choice == '8':
            print("""                                                              
                                                              
TTTTTTTTTTTTTTTTTTTTTTT     OOOOOOOOO     RRRRRRRRRRRRRRRRR   
T:::::::::::::::::::::T   OO:::::::::OO   R::::::::::::::::R  
T:::::::::::::::::::::T OO:::::::::::::OO R::::::RRRRRR:::::R 
T:::::TT:::::::TT:::::TO:::::::OOO:::::::ORR:::::R     R:::::R
TTTTTT  T:::::T  TTTTTTO::::::O   O::::::O  R::::R     R:::::R
        T:::::T        O:::::O     O:::::O  R::::R     R:::::R
        T:::::T        O:::::O     O:::::O  R::::RRRRRR:::::R 
        T:::::T        O:::::O     O:::::O  R:::::::::::::RR  
        T:::::T        O:::::O     O:::::O  R::::RRRRRR:::::R 
        T:::::T        O:::::O     O:::::O  R::::R     R:::::R
        T:::::T        O:::::O     O:::::O  R::::R     R:::::R
        T:::::T        O::::::O   O::::::O  R::::R     R:::::R
      TT:::::::TT      O:::::::OOO:::::::ORR:::::R     R:::::R
      T:::::::::T       OO:::::::::::::OO R::::::R     R:::::R
      T:::::::::T         OO:::::::::OO   R::::::R     R:::::R
      TTTTTTTTTTT           OOOOOOOOO     RRRRRRRR     RRRRRRR
                                                              
                                                              
1 = ON
2 = OFF 
3 = RESTART                                                             
                                                              
                                                              
                                                              
                                                              """)
            torchoice = input("?:")
            if torchoice == '1':
                sure = input("Are you sure you want to preform this action? (y/n):")
                if sure == 'y':
                    subprocess.run(['sudo', 'pacman', '-S', '--needed', 'tor'])
                    subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'tor'])

            elif torchoice == '2':
                sure2 = input("Are you sure you want to preform this action? (y/n):")
                if sure2 == 'y':
                    subprocess.run(['sudo', 'pacman', '-S', '--needed', 'tor'])
                    subprocess.run(['sudo', 'systemctl', 'disable', '--now', 'tor'])

            elif torchoice == '3':
                sure3 = input("Are you sure you want to preform this action? (y/n):")
                if sure3 == 'y':
                    subprocess.run(['sudo', 'pacman', '-S', '--needed', 'tor'])
                    subprocess.run(['sudo', 'systemctl', 'restart', 'tor'])
 
        elif choice == "install":
            installchoice = input("are u sure you want to install? (y/n) (WARNING: BlackArch SHA256 ISNT verified from this tool, IT could be dns spoofed, corrupted downloads, etc.):")
            if installchoice == 'y':
                type_fx(r"""
  ___         _        _ _      _   _          
 |_ _|_ _  __| |_ __ _| | |__ _| |_(_)___ _ _  
  | || ' \(_-<  _/ _` | | / _` |  _| / _ \ ' \ 
 |___|_||_/__/\__\__,_|_|_\__,_|\__|_\___/_||_|
                                               
                                               
                                               """)
                subprocess.run(['sudo', 'pacman', '-S', 'nmap', 'nikto', 'whois', 'inetutils', 'dirb', 'subfinder', 'proxychains', 'python-requests'])
                subprocess.run(['yay', '-S', 'holehe'])
                subprocess.run(['curl', '-O', 'https://blackarch.org/strap.sh'])
                subprocess.run(['chmod', '+x', 'strap.sh'])
                subprocess.run(['sudo', './strap.sh'])
                type_fx(r"""
                  
  ___ _      _    _           _   ___         _        _ _      _   _          
 | __(_)_ _ (_)__| |_  ___ __| | |_ _|_ _  __| |_ __ _| | |__ _| |_(_)___ _ _  
 | _|| | ' \| (_-< ' \/ -_) _` |  | || ' \(_-<  _/ _` | | / _` |  _| / _ \ ' \ 
 |_| |_|_||_|_/__/_||_\___\__,_| |___|_||_/__/\__\__,_|_|_\__,_|\__|_\___/_||_|
                                                                               
                                                                               
                                                                               """)
 
            else:
                 print("OKAY")
 
        elif choice == '9':
            type_fx("""
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█▓▒▒▓█▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
  ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
  ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
   ░▒▓██▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                                                      
                                                      
1 = Mullvad VPN (Official Repos)
2 = Proton VPN  (Official Repos)
3 = Riseup VPN  (AUR - Requires YAY)
(open a github issue if u want more added.)
""")
            vpnchoice = input("What VPN? (1,2,3):")

            if vpnchoice == '1':
                subprocess.run(['sudo', 'pacman', '-S', 'mullvad-vpn'])

            elif vpnchoice == '2':
                vpnproton = input("GUI or CLI? (1,2):")
                if vpnproton == '1':
                    subprocess.run(['sudo', 'pacman', '-S', 'proton-vpn-gtk-app'])

                elif vpnproton == '2':
                    subprocess.run(['sudo', 'pacman', '-S', 'proton-vpn-cli'])

            elif vpnchoice == '3':
                print("Warning: You need YAY installed.")
                subprocess.run(['yay', '-S', 'riseup-vpn'])

        elif choice == '10':
            holechoice = input("email?:")
            subprocess.run(['holehe', holechoice])

        elif choice == '11':
            break

        else:
             print("please pick a valid option.")
try:
   main()
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit(0)
