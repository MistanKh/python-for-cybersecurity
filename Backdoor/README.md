# Backdoor Socket Demo

`backdoor_listener.py` and `backdoor.py` form a simple Python socket exercise for studying remote command execution flow in a controlled lab.

## Files

- `backdoor_listener.py` starts a TCP listener on `127.0.0.1:8080`, accepts one incoming connection, reads commands from the terminal, sends them to the client, and prints the returned output.
- `backdoor.py` connects to `127.0.0.1:8080`, waits for commands from the listener, executes them with `subprocess.check_output(..., shell=True)`, and sends the command output back.

## What It Does

- opens a local TCP connection between the listener and client
- sends command text from the listener to the connected client
- executes received commands on the client side
- returns command output to the listener
- exits cleanly when the listener sends `exit`

## Requirements

- Python 3
- a controlled local lab environment
- both scripts running on the same host or on systems you explicitly own and authorize

## Usage

Start the listener first.

### Windows

```powershell
py "Backdoor/backdoor_listener.py"
```

Open a second terminal and start the client.

```powershell
py "Backdoor/backdoor.py"
```

### Linux / macOS

```bash
python3 "Backdoor/backdoor_listener.py"
python3 "Backdoor/backdoor.py"
```

## Example Session

```text
Listening on port 8080
Connection Ok from127.0.0.1
Enter a command: whoami
desktop-user
Enter a command: exit
```

## Notes

- The current scripts use the loopback address `127.0.0.1`, so they are configured for local testing by default.
- `backdoor_listener.py` accepts a single connection and then enters an input loop.
- `backdoor.py` executes commands with `shell=True`, which is intentionally risky and should only be studied in an isolated environment.
- Command failures are not fully handled yet. A failing command may terminate the client script.
- This code is educational and not suitable for production, real operations, or uncontrolled networks.

## Ethical Use

Use these scripts only in legal, isolated, and explicitly authorized environments.
