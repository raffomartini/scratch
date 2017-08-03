#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn,addr = s.accept()
    print('Connection address:', addr)
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        data = data.decode()
        print("received data:", data)
        data += '||ACK'
        conn.send(data.encode())  # echo