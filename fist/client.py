import ast
import socket


class Fist(object):
    def __init__(self, host="localhost", port=5575):
        self.host = host
        self.port = port

    def index(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"INDEX {data}\r\n".encode())
            return s.recv(1024)

    def search(self, query):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"SEARCH {query}\r\n".encode())
            result = s.recv(1024).decode()

        return ast.literal_eval(result)

    def exit(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"EXIT\r\n".encode())

    def version(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(f"VERSION\r\n".encode())
            result = s.recv(1024).decode()
        self.exit()

        return result.split()
