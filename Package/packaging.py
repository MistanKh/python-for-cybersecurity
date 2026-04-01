import subprocess
import sys
from pathlib import Path


def get_resource_path(file_name):
    # PyInstaller extracts bundled files under _MEIPASS; fall back to the script directory when run normally.
    bundle_dir = getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)
    return str(Path(bundle_dir) / file_name)


def open_bundled_file():
    # Launch the bundled PDF to demonstrate resource packaging in a benign way.
    bundled_file = get_resource_path("metallica.pdf")
    subprocess.Popen(bundled_file, shell=True)


if __name__ == "__main__":
    open_bundled_file()
    print("Opened bundled resource: metallica.pdf")
