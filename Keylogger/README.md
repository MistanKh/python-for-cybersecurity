# Keylogger

`keylogger.py` is a basic Python keylogging practice script that records keystrokes with `pynput` and periodically sends the collected log to an email account over SMTP.

## What It Does

- Listens for keyboard keypress events with `pynput`
- Appends normal characters to an in-memory log buffer
- Records special keys such as `Key.enter` when they are not plain characters
- Uses a repeating timer to send the collected log by email every 30 seconds
- Clears the current log after each email send attempt

## Dependencies

- Python 3
- `pynput`
- network access for SMTP email delivery
- a valid email account and SMTP credentials

## Built-In Modules Used

These are part of the Python standard library and do not need separate installation:

- `threading`
- `smtplib`

## Platform Notes

- Linux, macOS, and Windows can all install `pynput`, but keyboard event capture depends on the local desktop environment and permissions.
- On Linux, graphical session access is typically required. Some Wayland setups can limit global key capture compared with X11.
- On macOS, input monitoring permissions may be required in System Settings before keyboard hooks work.
- On Windows, running the terminal with administrator privileges may be needed in some environments.
- The current script contains placeholder Gmail credentials that should be replaced before testing.

## Install Dependencies

### Debian / Ubuntu / Kali

```bash
sudo apt update
sudo apt install python3 python3-pip
python3 -m pip install pynput
```

### Fedora

```bash
sudo dnf install python3 python3-pip
python3 -m pip install pynput
```

### RHEL / CentOS

```bash
sudo yum install python3 python3-pip
python3 -m pip install pynput
```

### Arch Linux

```bash
sudo pacman -S python python-pip
python -m pip install pynput
```

### openSUSE

```bash
sudo zypper install python3 python3-pip
python3 -m pip install pynput
```

### macOS

Install Homebrew if needed, then:

```bash
brew install python
python3 -m pip install pynput
```

You may also need to grant Input Monitoring or Accessibility permissions to your terminal application.

### Windows

Install Python 3, then install `pynput`:

```powershell
py -m pip install pynput
```

Run PowerShell or Command Prompt with appropriate privileges if keyboard events are not captured.

## Configuration

Before running the script, update the sender email address and password inside `send_email()` calls:

```python
send_email("test@gmail.com", "test", log.encode("utf-8"))
```

Use an account and SMTP settings that you control in a lab environment.

## Usage

### Linux

```bash
python3 "Keylogger/keylogger.py"
```

### macOS

```bash
python3 "Keylogger/keylogger.py"
```

### Windows

```powershell
py "Keylogger/keylogger.py"
```

## Example Behavior

- Keystrokes are appended to the `log` string as you type.
- Every 30 seconds, the current contents of `log` are emailed and the buffer is reset.
- The script keeps running while the keyboard listener is active.

## Notes

- This script is educational and not production-ready.
- Email delivery depends on valid SMTP credentials and provider policy.
- Some email providers block basic username-and-password SMTP logins unless app passwords or security settings are configured.
- Keyboard monitoring behavior can differ across operating systems and desktop environments.
- Use this only in legal, controlled, and explicitly authorized environments.
