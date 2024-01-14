#!/usr/bin/python3
import socket

PORT = 2020
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", PORT))
while 1:
    data, addr = s.recvfrom(1024)
    print("\nFrom: %s:%s\nReceived: %s" % (addr[0], addr[1], data))

    if data:
        sent = s.sendto(b"Server received: %b" % data, addr)
        print("Sent %s bytes back to %s:%s" % (sent, addr[0], addr[1]))
