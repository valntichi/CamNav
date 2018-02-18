import os, socket

remote = '/Users/Guest/'
print os.listdir(remote)

ip = ('127.0.0.1', 445)

s = socket.socket()
s.connect(ip)