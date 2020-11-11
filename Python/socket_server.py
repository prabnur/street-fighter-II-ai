import gym
import socket

s = socket.socket()
print("nice socket!")

port = 8080
s.bind(('127.0.0.1', port))
s.listen(5)

while True:
    c, addr = s.accept()
    print("hey got connection from", addr)
    while True:
        # this is where you should start accepting things from socket server
        # and do something with them
        print(c.recv(1024))