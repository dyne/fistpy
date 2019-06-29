import ast
import socket


class FistException(Exception):
    pass


class Fist(object):
    def __init__(self, host="localhost", port=5575):
        self.host = host
        self.port = port

    def index(self, data):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(f"INDEX {data}\r\n".encode())
                s.sendall(b"EXIT\r\n")
                return s.recv(1024)
        except ConnectionResetError as cre:
            raise FistException("A very bad thing happened on the fist server") from cre

    def search(self, query):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(f"SEARCH {query}\r\n".encode())
                result = s.recv(1024).decode()
                s.sendall(b"EXIT\r\n")

            return ast.literal_eval(result)
        except ConnectionResetError as cre:
            raise FistException("A very bad thing happened on the fist server") from cre
