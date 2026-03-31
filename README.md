# Python for Cybersecurity

Python cybersecurity practice scripts and notes built while following the Coursera course **Exploit Development, Malware, & Defensive Strategies**.

## Overview

This repository is a growing collection of small Python security tools, command-line exercises, and notes focused on networking, ethical hacking concepts, packet-level scripting, and defensive security practice.

Each tool is kept in its own folder with its script and local documentation so the repository stays easy to browse as new exercises are added.

## Repository Structure

```text
.
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
|-- LICENSE
`-- README.md
```

## Tool Index

| Tool | Category | Status | Summary |
| --- | --- | --- | --- |
| `MAC Changer` | Networking | Complete | Changes the MAC address of a Linux network interface |
| `Network Scanner` | Reconnaissance | In Progress | Performs ARP-based local network discovery with Scapy |
| `MITM` | Man-in-the-Middle | In Progress | Sends ARP spoofing packets between a target and gateway for lab-based MITM practice |
| `Packet Listener` | Packet Analysis | In Progress | Sniffs HTTP traffic on a selected interface and prints raw request payload data |

## Tool Documentation

- `MAC Changer`
  - Script: `MAC Changer/mac_changer.py`
  - Docs: `MAC Changer/README.md`
- `Network Scanner`
  - Script: `Network Scanner/scanner.py`
  - Docs: `Network Scanner/README.md`
- `MITM`
  - Script: `MITM/spoofer.py`
  - Docs: `MITM/README.md`
- `Packet Listener`
  - Script: `Packet Listener/listener_http.py`
  - Docs: `Packet Listener/README.md`

## Current Focus

The current set of exercises centers on:

- interface manipulation
- local network discovery
- ARP packet crafting with Scapy
- man-in-the-middle lab concepts
- packet sniffing and HTTP request inspection
- building familiarity with Python-based security tooling

## Repository Convention

Each tool in this repository should live in its own folder and can include:

- a Python script, such as `tool_name/tool_name.py`
- a local README, such as `tool_name/README.md`

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
