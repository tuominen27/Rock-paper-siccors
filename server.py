import socket
from _thread import *
import sys

server = "192.168.0.20"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.erros as e:
    str(e)

s.listen(2)
print("Odotetaan yhteyttä, Serveri käynnistyi")

def threaded_client(conn):
    
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Yhteys katkesi")
                break
            else:
                print("Vastaanotettu: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

while True:
    conn, addr = s.accept()
    print("Yhdistetty: ", addr)
    
    start_new_thread(threaded_client(), (conn, ))