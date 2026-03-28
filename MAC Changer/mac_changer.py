import subprocess
import optparse
import re


def user_input():
    # Parse the interface name and desired MAC address from the command line.
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to use")
    parser.add_option("-m", "--mac", dest="mac", help="mac to use")

    return parser.parse_args()


def mac_changer(interface, mac):
    # Bring the interface down, update the MAC address, and bring it back up.
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def control_new_mac(interface):
    # Read the interface details and extract the MAC address currently applied.
    ifconfig = subprocess.check_output(["ifconfig", interface], text=True)
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
    if new_mac:
        return new_mac.group(0)
    else:
        return None


# Start the script, apply the requested MAC change, and verify the result.
print("Mac Changer Started")

(user_inputs, arguments) = user_input()
mac_changer(user_inputs.interface, user_inputs.mac)
finalized_mac = control_new_mac(user_inputs.interface)

if finalized_mac == user_inputs.mac:
    print("Mac Changer Completed")
else:
    print("Mac Changer Failed")
