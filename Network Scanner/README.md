# Network Scanner

`scanner.py` is a basic ARP-based network scanner built with Python and Scapy.

## What It Does

- Takes an IP range or CIDR block with `-i` or `--ip`
- Sends ARP requests on the local network
- Prints the devices that respond

## Requirements

- Python 3
- `scapy`
- administrator or root privileges for packet operations

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

### Windows

Install Python 3, then install Scapy:

```powershell
py -m pip install scapy
```

For packet features on Windows, installing Npcap is usually required.

## Usage

```bash
sudo python3 "Network Scanner/scanner.py" -i 192.168.29.0/24
```

## Example Output

```text
Ether / ARP who has 192.168.29.23 says 192.168.29.23 ==> Ether / ARP is at 70:08:10:a2:8b:81 says 192.168.29.23
```

## Notes

- This script is meant for local network scanning with ARP.
- Run it only on networks you own or are explicitly authorized to test.
- On Linux and macOS, `sudo` is typically needed.
