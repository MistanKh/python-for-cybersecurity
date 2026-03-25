import subprocess
import optparse

def user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to use")
    parser.add_option("-m", "--mac", dest="mac", help="mac to use")

    return parser.parse_args()

def mac_changer(interface, mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

print("Mac Changer Started")

(user_inputs, arguments) = user_input()
mac_changer(user_inputs.interface, user_inputs.mac)