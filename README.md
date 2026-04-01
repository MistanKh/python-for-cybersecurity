# Python for Cybersecurity

Python cybersecurity practice scripts and notes built while following the Coursera course **Exploit Development, Malware, & Defensive Strategies**.

## Overview

This repository is a growing collection of small Python security tools, command-line exercises, and notes focused on networking, ethical hacking concepts, packet-level scripting, and defensive security practice.

Each tool is kept in its own folder with its script and local documentation so the repository stays easy to browse as new exercises are added.

## Repository Structure

```text
.
|-- Backdoor/
|   |-- README.md
|   |-- backdoor.py
|   `-- backdoor_listener.py
|-- Keylogger/
|   |-- README.md
|   `-- keylogger.py
|-- MAC Changer/
|   |-- README.md
|   `-- mac_changer.py
|-- MITM/
|   |-- README.md
|   `-- spoofer.py
|-- Network Scanner/
|   |-- README.md
|   `-- scanner.py
|-- Packet Listener/
|   |-- README.md
|   `-- listener_http.py
|-- Package/
|   |-- README.md
|   |-- metallica.pdf
|   `-- packaging.py
|-- LICENSE
|-- packaging.spec
`-- README.md
```

## Tool Index

| Tool | Category | Status | Summary |
| --- | --- | --- | --- |
| `MAC Changer` | Networking | Complete | Changes the MAC address of a Linux network interface |
| `Network Scanner` | Reconnaissance | Complete | Performs ARP-based local network discovery with Scapy |
| `MITM` | Man-in-the-Middle | Complete | Sends ARP spoofing packets between a target and gateway for lab-based MITM practice |
| `Packet Listener` | Packet Analysis | Complete | Sniffs HTTP traffic on a selected interface and prints raw request payload data |
| `Keylogger` | Host Monitoring | Complete | Captures keystrokes with `pynput` and periodically sends the logged data by email |
| `Backdoor` | Socket Programming | Complete | Demonstrates a simple listener/client remote command execution flow over a local TCP connection |
| `Package` | Persistence Lab | Complete | Demonstrates a Windows packaging and logon persistence workflow with a bundled decoy PDF |

## Tool Documentation

- `MAC Changer`
  - Script: `MAC Changer/mac_changer.py`
  - Docs: `MAC Changer/README.md`
- `Backdoor`
  - Scripts: `Backdoor/backdoor.py`, `Backdoor/backdoor_listener.py`
  - Docs: `Backdoor/README.md`
- `Keylogger`
  - Script: `Keylogger/keylogger.py`
  - Docs: `Keylogger/README.md`
- `Network Scanner`
  - Script: `Network Scanner/scanner.py`
  - Docs: `Network Scanner/README.md`
- `MITM`
  - Script: `MITM/spoofer.py`
  - Docs: `MITM/README.md`
- `Packet Listener`
  - Script: `Packet Listener/listener_http.py`
  - Docs: `Packet Listener/README.md`
- `Package`
  - Script: `Package/packaging.py`
  - Docs: `Package/README.md`
  - Build spec: `packaging.spec`

## Current Focus

The current set of exercises centers on:

- interface manipulation
- local network discovery
- ARP packet crafting with Scapy
- man-in-the-middle lab concepts
- packet sniffing and HTTP request inspection
- basic TCP client/server command exchange
- keyboard event monitoring with `pynput`
- timed log delivery with SMTP
- Windows packaging and registry-based persistence concepts
- building familiarity with Python-based security tooling

## Repository Convention

Each tool in this repository should live in its own folder and can include:

- a Python script, such as `tool_name/tool_name.py`
- a local README, such as `tool_name/README.md`
- optional support files for packaging or demos, such as bundled assets or a build spec

This keeps the root clean while making each exercise easy to find and easier to expand later.

## Course Context

**Exploit Development, Malware, & Defensive Strategies** is a Coursera course by Packt and part of **The Complete Ethical Hacking Course Specialization**. The course introduces Python-based security tooling and covers topics such as exploit development concepts, malware-related scripting, packet analysis, network attacks, and defensive techniques.

Course reference:
https://www.coursera.org/learn/packt-9781839210495-p4-3eje3

## Status

This is an educational practice repository. Some scripts are intentionally small and focused on learning specific concepts rather than production-ready tooling.

## Ethical Use

Use these techniques only in legal, controlled, and explicitly authorized environments.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
