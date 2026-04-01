# Windows Packaging Persistence Demo

`packaging.py` is a Windows-focused lab script that demonstrates three behaviors commonly analyzed in malware and persistence exercises:

- copying the current executable into `%APPDATA%`
- creating a `Run` registry entry for logon persistence
- opening a bundled decoy file after launch

This folder should be treated as a malware-analysis exercise for an isolated lab only.

## Files

- `packaging.py` contains the persistence and decoy-launch logic
- `metallica.pdf` is the bundled file opened by the script
- `../packaging.spec` is the PyInstaller spec file used to bundle the script and PDF together

## What It Does

- checks whether `%APPDATA%\upgradeable.exe` already exists
- copies the current executable to that location when it does not exist yet
- adds `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\upgrade` so the copied executable starts at user logon
- resolves the runtime path for bundled files through `sys._MEIPASS` when launched from a PyInstaller build
- opens `metallica.pdf`
- prints `You Got Hacked!` in a timed loop

## Requirements

- Python 3 on Windows
- permission to write to the current user profile
- a disposable and explicitly authorized lab VM

## Code Notes

- `add_to_registry()` assumes the process is running from a packaged executable and copies `sys.executable` into `%APPDATA%`.
- `get_resource_path()` supports both normal script execution and PyInstaller extraction at runtime.
- `open_added_file()` launches the bundled PDF with the default Windows handler.
- The persistence logic uses the current user hive (`HKCU`), so it does not require system-wide registry access.

## Analysis Focus

This example is useful for studying:

- basic Windows persistence through the `Run` key
- how PyInstaller-bundled resources are accessed with `_MEIPASS`
- how decoy documents can be launched alongside another action
- simple indicators to check during malware triage

## Safety Notes

- Do not run this on a personal machine or shared system.
- The script modifies the current user's startup behavior.
- If executed from a bundled build, it can copy itself into `%APPDATA%` and persist across logons.
- Review the code in a VM before any execution.

## Ethical Use

Use this material only for legal, isolated, and explicitly authorized education, testing, or defensive analysis.
