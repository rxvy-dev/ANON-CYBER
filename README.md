<div align="center">

![rxvy-recon banner](banner.svg)

**A lightweight Python CLI for launching common recon and security-testing tools through ProxyChains — pick a number, enter a target, done.**

</div>

---

## Overview

`rxvy-recon` wraps a set of well-known reconnaissance, OSINT, and security-testing tools behind a single menu-driven terminal interface. Instead of memorizing flags for a dozen different tools, you pick a number and enter a target. Traffic routes through ProxyChains by default.

Built for CTFs, homelabs, and authorized security testing.

## Tools Included

| Category | Tools |
|---|---|
| **Recon & Scanning** | Nmap, Nmap `-O` (OS detection), WHOIS, Subfinder, DIRB |
| **Web Testing** | Nikto, SQLMap, WPScan |
| **OSINT** | Holehe, Sherlock |
| **Social Engineering** | ZPhisher |
| **Infrastructure** | FTP, Tor, VPN Manager (Mullvad / Proton / Riseup) |
| **Network Utilities** | MacChanger |

All tool commands run through `proxychains` by default — remove it from the relevant command if you're not using it.

## Screenshots

<div align="center">

**Main Menu**
![Main Menu](mainmenu.png)

**Tor Control**
![Tor Control](tormenu.png)

**VPN Manager**
![VPN Manager](vpnmenu.png)

**MacChanger**
![MacChanger](macchanger.png)

</div>

## Installation

Dependencies can be installed directly from the tool itself:

```bash
python3 rxvyrecon.py
```

Then choose `[I] Install Dependencies` from the main menu. This installs the core tool set via `pacman`, additional tools via `yay`, and clones ZPhisher.

> **Note:** the BlackArch strap script's SHA256 is **not verified** by this tool. It could theoretically be DNS-spoofed or corrupted in transit — review it yourself before running if that matters to you.

### Manual install

If you'd rather install everything yourself:

```bash
sudo pacman -S nmap nikto whois inetutils dirb subfinder proxychains python-requests sqlmap macchanger
yay -S holehe sherlock
git clone --depth=1 https://github.com/htr-tech/zphisher.git
```

## Usage

```bash
$ python3 rxvyrecon.py
Choose: 1
ip or url: scanme.nmap.org
```

Pick a numbered option from the main menu, supply a target when prompted, and the corresponding tool runs through ProxyChains automatically.

Submenus (Tor, VPN Manager, MacChanger) follow the same pattern — pick a number, confirm if prompted, done.

## ProxyChains

Make sure ProxyChains is configured with a working proxy before running scans that depend on it. If you don't want to route traffic through ProxyChains, remove it from the relevant `subprocess` calls in the script.

## Customization

This project is intentionally simple and built to be modified. Ideas for extending it:

- Swap the ASCII banners and color scheme
- Add or remove tools from the menu
- Add new menu options, workflows, or "Manager" submenus
- Improve error handling for missing dependencies
- Add scan logging or session history
- Add configuration/profile support (default interface, wordlist, proxy settings)
- Improve the interface further

## Legal & Ethical Use

For educational use, CTFs, security research, and authorized security testing only.

**Only run these tools against systems you own or have explicit permission to test.** Unauthorized scanning is illegal in most jurisdictions. The author is not responsible for any misuse of this software.

## Contributing

This is an open-source project — forks, pull requests, and improvements are welcome. Open a GitHub issue if you'd like to see a tool or feature added.

## Credits

Created and maintained by **rxvy**.

---

<div align="center">

*If rxvy-recon is useful to your workflow, consider starring the repo.*

</div>
