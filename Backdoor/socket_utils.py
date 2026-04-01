import json
import struct
from typing import Optional


def send_json(connection, data):
    json_data = json.dumps(data).encode()
    json_length = struct.pack("!I", len(json_data))
    connection.sendall(json_length + json_data)


def receive_exactly(connection, length) -> Optional[bytes]:
    data = b""
    while len(data) < length:
        chunk = connection.recv(length - len(data))
        if not chunk:
            return None
        data += chunk
    return data


def receive_json(connection):
    json_length = receive_exactly(connection, 4)
    if not json_length:
        return None
    message_length = struct.unpack("!I", json_length)[0]
    json_data = receive_exactly(connection, message_length)
    if json_data is None:
        return None
    return json.loads(json_data.decode())
