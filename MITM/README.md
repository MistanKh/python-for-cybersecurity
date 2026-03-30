# MITM Spoofer

`spoofer.py` is a basic ARP spoofing practice script built with Python and Scapy for controlled man-in-the-middle lab exercises.

## What It Does

- Accepts a target IP address with `-t` or `--target`
- Accepts a gateway IP address with `-g` or `--gateway`
- Resolves the MAC address for each host with ARP requests
- Repeatedly sends forged ARP replies so the target and gateway associate the attacker's MAC address with each other
- Attempts to restore ARP entries when the script is stopped with `Ctrl+C`

## Dependencies

- Python 3
- `scapy`
- administrator or root privileges for raw packet operations
- access to a local Ethernet or Wi-Fi network where ARP is in use

## Platform Notes

- Linux is the most common environment for this kind of lab exercise and is the best fit for the current script.
- macOS can run Scapy-based packet scripts, but you still need elevated privileges and local testing may vary by interface and system protections.
- Windows can install the Python dependencies, but packet injection typically also requires Npcap. Some Scapy workflows are less predictable on Windows than on Linux.
- This script should only be used in a private lab or an explicitly authorized test environment.

## Install Dependencies

### Debian / Ubuntu / Kali

```bash
sudo apt update
sudo apt install python3 python3-pip
python3 -m pip install scapy
```

### Fedora

```bash
sudo dnf install python3 python3-pip
python3 -m pip install scapy
```

### RHEL / CentOS

```bash
sudo yum install python3 python3-pip
python3 -m pip install scapy
```

### Arch Linux

```bash
sudo pacman -S python python-pip
python -m pip install scapy
```

### openSUSE

```bash
sudo zypper install python3 python3-pip
python3 -m pip install scapy
```

### macOS

Install Homebrew if needed, then:

```bash
brew install python
python3 -m pip install scapy
```

Run the script with `sudo` so Scapy can send ARP packets.

### Windows

1. Install Python 3.
2. Install Npcap from https://npcap.com/
3. Install Scapy:

```powershell
py -m pip install scapy
```

Run PowerShell or Command Prompt as Administrator before executing the script.

## Usage

### Linux

```bash
sudo python3 "MITM/spoofer.py" -t 192.168.1.10 -g 192.168.1.1
```

### macOS

```bash
sudo python3 "MITM/spoofer.py" -t 192.168.1.10 -g 192.168.1.1
```

### Windows

```powershell
py "MITM/spoofer.py" -t 192.168.1.10 -g 192.168.1.1
```

## Example Arguments

- `-t 192.168.1.10` selects the victim or target host
- `-g 192.168.1.1` selects the network gateway or router

## Example Output

```text
Sending Packets 2
Sending Packets 4
Sending Packets 6
```

When interrupted:

```text
Exiting... and resting
```

## Notes

- The script uses ARP, so it is intended for local IPv4 network segments.
- On Linux and macOS, `sudo` is typically required.
- On Windows, administrator privileges and Npcap are usually required.
- The current script is educational and does not include forwarding, packet capture, or safety checks for production use.
- If the script is stopped unexpectedly, the ARP restoration step may not fully complete.
