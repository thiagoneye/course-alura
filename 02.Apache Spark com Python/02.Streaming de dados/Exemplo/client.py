"""
Formação Apache Spark
Streaming de Dados
"""

# Imports

import socket
import time


# Inputs

HOST = "localhost"
PORT = 3000
NUMBER_OF_BYTES = 1024

# Main

skt = socket.socket()
skt.connect((HOST, PORT))

while True:
    data = skt.recv(NUMBER_OF_BYTES)
    print(data.decode("utf-8"))
    time.sleep(3)
