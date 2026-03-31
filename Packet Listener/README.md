# HTTP Packet Listener

`listener_http.py` is a basic HTTP packet listener built with Python and Scapy for capturing HTTP request payload data on a selected network interface.

## What It Does

- Accepts a network interface with `-i` or `--interface`
- Starts sniffing traffic on the selected interface
- Checks packets for the `HTTPRequest` layer
- Prints the raw payload when HTTP request traffic includes packet data

## Requirements

- Python 3
- `scapy`
- administrator or root privileges for packet capture
- `Npcap` on Windows for interface access and sniffing support

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

Run the script with `sudo` so Scapy can sniff packets.

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
sudo python3 "Packet Listener/listener_http.py" -i wlan0
```

### macOS

```bash
sudo python3 "Packet Listener/listener_http.py" -i en0
```

### Windows

```powershell
py "Packet Listener/listener_http.py" -i "\Device\NPF_{YOUR-INTERFACE-GUID}"
```

## Example Output

```text
b'username=admin&password=secret'
```

## Notes

- This script listens for unencrypted HTTP traffic only. HTTPS payloads will not be readable.
- The script requires a valid interface name. Interface naming differs between Linux, macOS, and Windows.
- On Linux and macOS, `sudo` is typically needed.
- On Windows, administrator privileges and Npcap are usually required.
- This script is educational and should only be used in legal, controlled, and authorized environments.
