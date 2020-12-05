#!/usr/bin/env python

# Yannick Rüfenacht
# BFH

import socket

HOST = '10.0.2.15'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print('Connected with ', address)
        while True:
            connection.sendall(b'Hello')

