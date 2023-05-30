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

# Main

skt = socket.socket()
skt.bind((HOST, PORT))

print(f"Aguardando conexão na porta {PORT}")

skt.listen(5)
conn, address = skt.accept()

print(f"Recebendo solicitação de {address}")

messages = ["Mensagem A", "Mensagem B", "Mensagem C",
            "Mensagem D", "Mensagem E", "Mensagem F",
            "Mensagem G"]

for message in messages:
    message = bytes(message, "utf-8")
    conn.send(message)
    time.sleep(3)

conn.close()
