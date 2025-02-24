#!/usr/bin/env python
# coding=utf-8

# Yannick Rüfenacht
# BFH

import socket
import struct
import time
import grove_ultrasonic_ranger

HOST = '192.168.3.10'
PORT = 65432

def main():
    # Setup Ultrasonic Ranger
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.GPIO)
    pin = sh.argv2pin()

    sonar = grove_ultrasonic_ranger.Grove(pin)

    # Setup Socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        connection, address = s.accept()
        with connection:
            print('Connected with ', address)
            while True:
                distance = int(sonar.get_distance())
                print('Sending {} cm'.format(distance))
                connection.send(str(distance).encode())
                time.sleep(0.1)

if __name__ == '__main__':
    main()

