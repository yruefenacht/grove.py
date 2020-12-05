#!/usr/bin/env python

# Yannick Rüfenacht
# BFH

import socket
import struct

HOST = '192.168.3.10'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        distance = struct.unpack('!d', repr(data))
        print(distance)

