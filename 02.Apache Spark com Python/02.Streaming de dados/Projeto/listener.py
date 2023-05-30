"""
Formação Apache Spark
Streaming de Dados
Análise de Dados do Twitter
"""

# Imports

import socket
import tweepy


# Inputs

HOST = "localhost"
PORT = 9009
TOKEN = "AAAAAAAAAAAAAAAAAAAAAD9pnwEAAAAA4DgIRJAVaawyU4ZDirJO8E0nHOA%3DsNpD9Juyf8Vr2TBHD9hrQ4Op5b1dDrGQCM9EBUhzwskfmWNoju"
KEYWORD = "chess"


# Classes

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print("="*50)
        conn.send(tweet.text.encode("latin1", "ignore"))


# Main

skt = socket.socket()
skt.bind((HOST, PORT))
print(f"Aguardando conexão na porta {PORT}")

skt.listen(5)
conn, address = skt.accept()
print(f"Recebendo solicitação de {address}")

printer = GetTweets(TOKEN)
printer.add_rules(tweepy.StreamRule(KEYWORD))
printer.filter()

conn.close()
