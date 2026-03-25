import subprocess
import optparse
import re


def user_input():
    # Parse the interface and target MAC address from the command line.
    parser = optparse.OptionParser()
    parser.add_option(
        "-i", "--interface", dest="interface", help="network interface to modify"
    )
    parser.add_option(
        "-m", "--mac", dest="mac", help="new MAC address to assign"
    )

    options, _ = parser.parse_args()

    if not options.interface or not options.mac:
        parser.error("Please provide both --interface and --mac.")

    return options


def mac_changer(interface, mac):
    # Bring the interface down, apply the new MAC, and bring it back up.
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def control_new_mac(interface):
    # Read the interface details and extract the current MAC address.
    ifconfig = subprocess.check_output(["ifconfig", interface], text=True)
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)

    if new_mac:
        return new_mac.group(0)

    return None


print("Mac Changer Started")

user_inputs = user_input()
mac_changer(user_inputs.interface, user_inputs.mac)
finalized_mac = control_new_mac(user_inputs.interface)

if finalized_mac == user_inputs.mac:
    print("Mac Changer Completed")
else:
    print("Mac Changer Failed")
