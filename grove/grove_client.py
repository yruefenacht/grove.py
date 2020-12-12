#!/usr/bin/env python

# Yannick Rüfenacht
# BFH

import socket
import struct

HOST = '192.168.3.10'
PORT = 65432
TIMEOUT = 5

class GroveClient:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(TIMEOUT)
        self.s.connect((HOST, PORT))

    def get_distance(self):
        return self.s.recv(1024).decode()

