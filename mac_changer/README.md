# MAC Changer

`mac_changer.py` is a simple Python script that changes the MAC address of a network interface on Linux.

## What It Does

- Accepts a network interface with `-i` or `--interface`
- Accepts a target MAC address with `-m` or `--mac`
- Uses `ifconfig` to bring the interface down, change the MAC address, and bring the interface back up

## Requirements

- Python 3
- `sudo`
- `ifconfig`

`ifconfig` is usually provided by the `net-tools` package on most Linux distributions.

## Requirements Note

This tool is intended for Linux systems and requires:

- Python 3
- `net-tools` for `ifconfig`
- sufficient privileges to modify a network interface

## Install Dependencies

### Debian / Ubuntu / Kali

```bash
sudo apt update
sudo apt install net-tools
```

### Fedora

```bash
sudo dnf install net-tools
```

### RHEL / CentOS

```bash
sudo yum install net-tools
```

### Arch Linux

```bash
sudo pacman -S net-tools
```

### openSUSE

```bash
sudo zypper install net-tools
```

## Usage

```bash
sudo python3 mac_changer/mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

Example:

- `-i eth0` selects the network interface
- `-m 00:11:22:33:44:55` sets the new MAC address

## Example Output

Example terminal output:

```text
Mac Changer Started
Mac Changer Completed
```

You can replace this with an actual screenshot or a fuller terminal capture later if you want the repository page to feel more complete.

## Notes

- This script is intended for Linux systems where `ifconfig` is available.
- You typically need root privileges to change a MAC address.
- Use the correct interface name for your system, such as `eth0`, `wlan0`, or similar.
