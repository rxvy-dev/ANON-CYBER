# ============================================================
#                        rxvy-recon CLI
# ============================================================
#
#   Created by : rxvy
#   Version    : 3,0
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
def asdians(text, delay=0.05):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    return ""

def menus(text, delay=0.03):
    for line in text.splitlines():
        print(line, flush=True)
        time.sleep(delay)



# for commands
import subprocess
# for animations.
import sys
import time
import random

def menu():
    menus(RED + """     
   For educational use, CTFs, security research, and
   authorized security testing only.

   Only run these tools against systems you own or have
   explicit permission to test. Unauthorized scanning is
   illegal in most jurisdictions.

   The author is not responsible for any misuse of this
   software.                                                                                                                                                                                                                                                                                                   
 ██████▒   ██▓  ▓██  ██▒  ▒██ ███    ███           ██████▒   ████████    ▒████▒   ░████░   ███   ██ 
 ███████▓  ▒██  ██▒  ██▓  ▓██ ░██▒  ▒██░           ███████▓  ████████   ▓██████   ██████   ███   ██ 
 ██   ▒██   ██▓▓██   ▒██  ██▒  ███  ███            ██   ▒██  ██        ▒██▒  ░█  ▒██  ██▒  ███▒  ██ 
 ██    ██   ▒████▒   ▒██  ██▒   ██▒▒██             ██    ██  ██        ██▓       ██▒  ▒██  ████  ██ 
 ██   ▒██    ████     ██ ░██    ▓████▓             ██   ▒██  ██        ██░       ██    ██  ██▒█▒ ██ 
 ███████▒    ▒██▒     ██▒▒██     ████              ███████▒  ███████   ██        ██    ██  ██ ██ ██ 
 ██████▓     ▒██▒     ██▒▒██     ▒██▒              ██████▓   ███████   ██        ██    ██  ██ ██ ██ 
 ██  ▓██░    ████     ▒████▒      ██               ██  ▓██░  ██        ██░       ██    ██  ██ ▒█▒██ 
 ██   ██▓   ▒████▒    ░████░      ██               ██   ██▓  ██        ██▓       ██▒  ▒██  ██  ████ 
 ██   ▒██   ██▒▒██     ████       ██               ██   ▒██  ██        ▒██▒  ░█  ▒██  ██▒  ██  ▒███ 
 ██    ██▒ ▒██  ██▒    ████       ██               ██    ██▒ ████████   ▓██████   ██████   ██   ███ 
 ██    ███ ██▓  ▓██    ▓██▓       ██               ██    ███ ████████    ▒████▒   ░████░   ██   ███ 
                                                                                                    
╔══════════════════════════════════════════════════════════════════════╗
║                        ⚠ PROXYCHAINS                                 ║
╠══════════════════════════════════════════════════════════════════════╣
║  Make sure ProxyChains is configured with a working proxy.           ║
║  If you are not using ProxyChains, remove it from the commands.      ║
╚══════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════╗
║                         RXVY-RECON v3.0                              ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  [1] Nmap              Scan for open ports                           ║
║  [2] Nikto             Web server security scanner                   ║
║  [3] WHOIS             Domain / IP registration information          ║
║  [4] FTP               Connect to FTP servers                        ║
║  [5] DIRB              Web directory enumeration                     ║
║  [6] Subfinder         Passive subdomain discovery                   ║
║  [7] Nmap -O           Operating-system detection                    ║
║                                                                      ║
║  [8] Tor               Tor service / proxy management                ║
║  [9] VPN Manager       Install and manage VPN options                ║
║                                                                      ║
║  [10] Holehe           Check email account exposure                  ║
║  [11] ZPhisher         Phishing simulation tool                      ║
║  [12] Sherlock         Username OSINT                                ║
║                                                                      ║
║  [13] SQLMap           SQL injection testing                         ║
║  [14] WPScan           WordPress security scanner                    ║
║  [15] MacChanger       Change your mac address whenever              ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  [I] Install Dependencies                         [Q] Exit           ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
 
def main():
   while True:
        global RED
        menu()

        choice = input("Choose:")
 
        if choice == '1':
            nmapchoice = input(asdians("ip or url:"))
            subprocess.run(['proxychains', 'nmap', nmapchoice])
 
        elif choice == '2':
            niktochoice = input(asdians("ip or url:"))
            subprocess.run(['proxychains', 'nikto', '-host', niktochoice])
 
        elif choice == '3':
            whoischoice = input(asdians("website/url:"))
            subprocess.run(['proxychains', 'whois', whoischoice])
 
        elif choice == '4':
            ftpchoice = input(asdians("url:"))
            subprocess.run(['proxychains', 'ftp', ftpchoice])
 
        elif choice == '5':
            dirbchoice = input(asdians("url:"))
            subprocess.run(['proxychains', 'dirb', dirbchoice])
 
        elif choice == '6':
            subfinderchoice = input(asdians("website/url:"))
            subprocess.run(['proxychains', 'subfinder', '-d', subfinderchoice])
 
 
        elif choice == '7':
            nmapOchoice = input(asdians("ip or url:"))
 
#       SUDO IS NEEDED FOR -O ON NMAP!
 
            subprocess.run(['sudo', 'proxychains', 'nmap', '-O', nmapOchoice])

        elif choice == '8':
            menus("""                                                              
                                                              
╔══════════════════════════════════════════╗
║             T O R   C O N T R O L        ║
╚══════════════════════════════════════════╝
      _____                   _______                   _____          
     /\    \                 /::\    \                 /\    \         
    /::\    \               /::::\    \               /::\    \        
    \:::\    \             /::::::\    \             /::::\    \       
     \:::\    \           /::::::::\    \           /::::::\    \      
      \:::\    \         /:::/~~\:::\    \         /:::/\:::\    \     
       \:::\    \       /:::/    \:::\    \       /:::/__\:::\    \    
       /::::\    \     /:::/    / \:::\    \     /::::\   \:::\    \   
      /::::::\    \   /:::/____/   \:::\____\   /::::::\   \:::\    \  
     /:::/\:::\    \ |:::|    |     |:::|    | /:::/\:::\   \:::\____\ 
    /:::/  \:::\____\|:::|____|     |:::|    |/:::/  \:::\   \:::|    |
   /:::/    \::/    / \:::\    \   /:::/    / \::/   |::::\  /:::|____|
  /:::/    / \/____/   \:::\    \ /:::/    /   \/____|:::::\/:::/    / 
 /:::/    /             \:::\    /:::/    /          |:::::::::/    /  
/:::/    /               \:::\__/:::/    /           |::|\::::/    /   
\::/    /                 \::::::::/    /            |::| \::/____/    
 \/____/                   \::::::/    /             |::|  ~|          
                            \::::/    /              |::|   |          
                             \::/____/               \::|   |          
                              ~~                      \:|   |          
                                                       \|___|          
╔══════════════════════════════════════════╗
║  [1] Turn ON                             ║
║  [2] Turn OFF                            ║
║  [3] Restart                             ║
║                                          ║
║  [4] Back                                ║
╚══════════════════════════════════════════╝                                            
                                                              
                                                              
                                                              """)
            torchoice = input("?:")
            if torchoice == '1':
                sure = input(asdians("Are you sure you want to preform this action? (y/n):"))
                if sure == 'y':
                    subprocess.run(['sudo', 'pacman', '-S', '--needed', 'tor'])
                    subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'tor'])

            elif torchoice == '2':
                sure2 = input(asdians("Are you sure you want to preform this action? (y/n):"))
                if sure2 == 'y':
                    subprocess.run(['sudo', 'pacman', '-S', '--needed', 'tor'])
                    subprocess.run(['sudo', 'systemctl', 'disable', '--now', 'tor'])

            elif torchoice == '3':
                sure3 = input(asdians("Are you sure you want to preform this action? (y/n):"))
                if sure3 == 'y':
                    subprocess.run(['sudo', 'pacman', '-S', '--needed', 'tor'])
                    subprocess.run(['sudo', 'systemctl', 'restart', 'tor'])

            elif torchoice == "4":
                exit
 
        elif choice == "i":
            installchoice = input(asdians("are u sure you want to install? (WARNING: BlackArch SHA256 ISNT verified from this tool, IT could be dns spoofed, corrupted downloads, etc.) (y/n):"))
            if installchoice == 'y':
                menus(r"""
  ___         _        _ _      _   _          
 |_ _|_ _  __| |_ __ _| | |__ _| |_(_)___ _ _  
  | || ' \(_-<  _/ _` | | / _` |  _| / _ \ ' \ 
 |___|_||_/__/\__\__,_|_|_\__,_|\__|_\___/_||_|
                                               
                                               
                                               """)
                subprocess.run(['sudo', 'pacman', '-S', 'nmap', 'nikto', 'whois', 'inetutils', 'dirb', 'subfinder', 'proxychains', 'python-requests', 'sqlmap', 'macchanger'])
                subprocess.run(['yay', '-S', 'holehe', 'sherlock'])
                subprocess.run(['curl', '-O', 'https://blackarch.org/strap.sh'])
                subprocess.run(['chmod', '+x', 'strap.sh'])
                subprocess.run(['sudo', './strap.sh'])
                subprocess.run(['git', 'clone', '--depth=1', 'https://github.com/htr-tech/zphisher.git'])
                menus(r"""
                  
  ___ _      _    _           _   ___         _        _ _      _   _          
 | __(_)_ _ (_)__| |_  ___ __| | |_ _|_ _  __| |_ __ _| | |__ _| |_(_)___ _ _  
 | _|| | ' \| (_-< ' \/ -_) _` |  | || ' \(_-<  _/ _` | | / _` |  _| / _ \ ' \ 
 |_| |_|_||_|_/__/_||_\___\__,_| |___|_||_/__/\__\__,_|_|_\__,_|\__|_\___/_||_|
                                                                               
                                                                               
                                                                               """)
 
            else:
                 asdians("OKAY")
 
        elif choice == '9':
            menus("""
╔══════════════════════════════════════════════════════════════════════╗
║                          VPN MANAGER                                 ║
╠══════════════════════════════════════════════════════════════════════╣
║        ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░         ║
║        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ║
║         ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ║
║         ░▒▓█▓▒▒▓█▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░          ║
║          ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ║
║          ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ║
║           ░▒▓██▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░          ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  [1] Mullvad VPN        Official Repos                               ║
║  [2] Proton VPN         Official Repos                               ║
║  [3] Riseup VPN         AUR - Requires YAY                           ║
║                                                                      ║
║  [4] Back                                                            ║
╚══════════════════════════════════════════════════════════════════════╝
   (open a github issue if u want more added.)
""")
            vpnchoice = input(asdians("What VPN? (1,2,3):"))

            if vpnchoice == '1':
                subprocess.run(['sudo', 'pacman', '-S', 'mullvad-vpn'])

            elif vpnchoice == '2':
                vpnproton = input(asdians("GUI or CLI? (1,2):"))
                if vpnproton == '1':
                    subprocess.run(['sudo', 'pacman', '-S', 'proton-vpn-gtk-app'])

                elif vpnproton == '2':
                    subprocess.run(['sudo', 'pacman', '-S', 'proton-vpn-cli'])

            elif vpnchoice == '3':
                asdians("Warning: You need YAY installed.")
                subprocess.run(['yay', '-S', 'riseup-vpn'])

            elif vpnchoice == "4":
                exit

        elif choice == '10':
            holechoice = input(asdians("email?:"))
            subprocess.run(['holehe', holechoice])

        elif choice == '11':
            subprocess.run(['bash', 'zphisher.sh'], cwd='zphisher')

        elif choice == '12':
            osintchoice = input(asdians("Username(S):"))
            subprocess.run(['sherlock', osintchoice])

        elif choice == '13':
            subprocess.run(['sqlmap', '--wizard'])

        elif choice == '14':
            wpchoice = input("URL:")
            subprocess.run(['wpscan', '--url', wpchoice])

        elif choice == '15':
            macchoice = input("""
SUDO IS USED IN THIS TOOL! 
╔══════════════════════════════════════════╗
║           M A C   C H A N G E R          ║
╚══════════════════════════════════════════╝

  ███╗   ███╗ █████╗  ██████╗
  ████╗ ████║██╔══██╗██╔════╝
  ██╔████╔██║███████║██║     
  ██║╚██╔╝██║██╔══██║██║     
  ██║ ╚═╝ ██║██║  ██║╚██████╗
  ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝

╔══════════════════════════════════════════╗
║  [1] Randomize enp4s0  (Ethernet)        ║
║  [2] Randomize wlp5s0  (WiFi)            ║
║                                          ║
║  [3] Back                                ║
╚══════════════════════════════════════════╝

""")
            if macchoice == '1':
                subprocess.run(['sudo', 'macchanger', 'enp4s0', '--random'])

            elif macchoice == '2':
                subprocess.run(['sudo', 'macchanger', 'wlp5s0', '--random'])

            elif macchoice == '3':
                exit
try:
   main()
except KeyboardInterrupt:
    asdians("\nExiting...")
    sys.exit(0)
