<div align="center">

![rxvy-recon banner](banner.svg)

[![License](https://img.shields.io/badge/license-Open%20Source-ff1a1a?style=flat-square)](#license)
[![Python](https://img.shields.io/badge/python-3.x-ff1a1a?style=flat-square)](#requirements)
[![Platform](https://img.shields.io/badge/platform-Arch%20%2F%20BlackArch-ff1a1a?style=flat-square)](#requirements)
[![Version](https://img.shields.io/badge/version-3.0-ff1a1a?style=flat-square)](#)
[![PRs](https://img.shields.io/badge/PRs-welcome-ff1a1a?style=flat-square)](#contributing)

**One menu. Every recon tool you need. Zero flag-memorizing.**

*A lightweight Python CLI that wraps common reconnaissance and security-testing tools behind a single menu, routed through ProxyChains by default.*

</div>

---

## Table of Contents

- [Overview](#overview)
- [Why rxvy-recon](#why-rxvy-recon)
- [Tools Included](#tools-included)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [ProxyChains Setup](#proxychains-setup)
- [Menu Reference](#menu-reference)
- [Customization](#customization)
- [Roadmap Ideas](#roadmap-ideas)
- [Troubleshooting](#troubleshooting)
- [Legal & Ethical Use](#legal--ethical-use)
- [Contributing](#contributing)
- [Credits](#credits)

---

## Overview

`rxvy-recon` turns a dozen separate command-line tools into a single, numbered menu. No flags to remember, no man pages to check mid-engagement — pick a tool, supply a target, and it runs.

Everything routes through **ProxyChains** by default. Tor and VPN management are built directly into the menu, so switching your exit point doesn't mean leaving the tool.

## Why rxvy-recon

- **Fast** — every tool is one keypress and one input away
- **Consistent** — the same interaction pattern (choose &#8594; target &#8594; run) across every tool
- **Proxy-first** — ProxyChains is baked into every scan command, not an afterthought
- **Self-installing** — a built-in installer pulls every dependency in one pass
- **Hackable** — plain Python, no framework, easy to add your own tools or menus

## Tools Included

| Category | Tools |
|---|---|
| **Recon & Scanning** | Nmap &#183; Nmap `-O` (OS detection) &#183; WHOIS &#183; Subfinder &#183; DIRB |
| **Web Testing** | Nikto &#183; SQLMap &#183; WPScan |
| **OSINT** | Holehe &#183; Sherlock |
| **Social Engineering** | ZPhisher |
| **Infrastructure** | FTP &#183; Tor Control &#183; VPN Manager (Mullvad / Proton / Riseup) |
| **Network Utilities** | MacChanger |

15 tools total, all reachable from one main menu.

## Screenshots

<div align="center">

| Main Menu | Tor Control |
|:---:|:---:|
| ![Main Menu](mainmenu.png) | ![Tor Control](tormenu.png) |

| VPN Manager | MacChanger |
|:---:|:---:|
| ![VPN Manager](vpnmenu.png) | ![MacChanger](macchanger.png) |

</div>

## Requirements

- Linux (built and tested on Arch / BlackArch)
- Python 3
- `sudo` access (required for OS detection, MacChanger, and service management)
- [`yay`](https://github.com/Jguer/yay) for AUR packages (Holehe, Sherlock, Riseup VPN)

## Installation

### Option 1 — Built-in installer

Run the script and choose the install option from the main menu:

```bash
python3 rxvyrecon.py
```

Then select **`[I] Install Dependencies`**. This will:

1. Install core tools via `pacman` (Nmap, Nikto, WHOIS, DIRB, Subfinder, ProxyChains, SQLMap, MacChanger, etc.)
2. Install AUR tools via `yay` (Holehe, Sherlock)
3. Pull and run the BlackArch strap script
4. Clone [ZPhisher](https://github.com/htr-tech/zphisher)

> ⚠️ **Heads up:** the BlackArch strap script's SHA256 is **not verified** by this installer. It could theoretically be corrupted or DNS-spoofed in transit. Review `strap.sh` yourself before running if that matters for your threat model.

### Option 2 — Manual install

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

That's the whole interaction model: pick a number from the menu, answer the prompt it gives you, watch it run. Submenus (Tor, VPN Manager, MacChanger) follow the same pattern one level deeper.

## ProxyChains Setup

Every scanning command in `rxvy-recon` is prefixed with `proxychains`. Before running real scans:

1. Confirm `/etc/proxychains.conf` (or your configured path) points to a working proxy
2. Test the chain manually once outside the tool if you're unsure it's working
3. If you don't want to route through ProxyChains at all, remove it from the relevant commands directly in the script — every tool call is a single `subprocess.run([...])` line, so this is a one-word edit per tool

## Menu Reference

| # | Tool | Prompt | Notes |
|---|---|---|---|
| 1 | Nmap | `ip or url` | Standard port scan |
| 2 | Nikto | `ip or url` | Web server scan |
| 3 | WHOIS | `website/url` | Domain/IP lookup |
| 4 | FTP | `url` | Opens an FTP connection |
| 5 | DIRB | `url` | Directory enumeration |
| 6 | Subfinder | `website/url` | Passive subdomain discovery |
| 7 | Nmap `-O` | `ip or url` | OS detection — requires `sudo` |
| 8 | Tor | — | Submenu: on / off / restart |
| 9 | VPN Manager | — | Submenu: Mullvad / Proton / Riseup |
| 10 | Holehe | `email` | Checks email exposure across sites |
| 11 | ZPhisher | — | Launches the ZPhisher script |
| 12 | Sherlock | `username(s)` | Username OSINT across platforms |
| 13 | SQLMap | — | Launches the interactive wizard |
| 14 | WPScan | `URL` | WordPress security scan |
| 15 | MacChanger | — | Submenu: randomize a chosen interface — requires `sudo` |
| I | Install Dependencies | — | Runs the full installer |
| Q | Exit | — | Quits the tool |

## Customization

This project is intentionally simple and built to be modified. A few directions:

- Swap the ASCII banners and color scheme
- Add or remove tools from the menu
- Add new "Manager"-style submenus (see [Roadmap Ideas](#roadmap-ideas))
- Improve error handling for missing dependencies
- Add scan logging or session history
- Add configuration/profile support (default interface, wordlist, proxy toggle)
- Add non-interactive/argument-based usage alongside the menu

## Roadmap Ideas

Not implemented yet — listed here as a starting point for contributors:

- **Proxy Manager** — view/edit/test the ProxyChains config from inside the tool
- **Interface Manager** — detect real network interfaces instead of hardcoding names (fixes MacChanger needing manual edits per machine)
- **Scan history / logging** — record tool, target, and timestamp per run
- **Dependency checker** — verify what's installed without running the full installer
- **Config file** — persist a default interface, wordlist, or proxy toggle between sessions

## Troubleshooting

**A tool exits immediately with "command not found"**
It isn't installed yet. Run `[I] Install Dependencies`, or install that one tool manually.

**MacChanger fails or targets the wrong interface**
The interface names (`enp4s0`, `wlp5s0`) are hardcoded and specific to the original setup. Run `ip link show` to find your actual interface names and edit them into the script.

**Nmap `-O` (OS detection) fails**
This requires `sudo` — the menu option already runs it with elevated privileges, so make sure your user has sudo access.

**A scan seems to hang or fail silently**
Check that ProxyChains is actually pointed at a working, reachable proxy — see [ProxyChains Setup](#proxychains-setup).

## Legal & Ethical Use

For educational use, CTFs, security research, and authorized security testing only.

**Only run these tools against systems you own or have explicit permission to test.** Unauthorized scanning is illegal in most jurisdictions. The author is not responsible for any misuse of this software.

## Contributing

This is an open-source project — forks, pull requests, and improvements are welcome.

- Open a GitHub issue for bugs or feature requests
- Open a PR for new tools, submenus, or fixes
- Keep new menu options consistent with the existing style (boxed headers, numbered options, a way back to the main menu)

## Credits

Created and maintained by **rxvy**.

---

<div align="center">

*If rxvy-recon is useful to your workflow, consider starring the repo.*

</div>
