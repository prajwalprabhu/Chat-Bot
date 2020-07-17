import socket
s=socket.socket()
# s.bind(('localhost',9999))
s.connect(('localhost',9999))
msg=s.recv(1024).decode()
print(msg)
length=s.recv(1024).decode()
print(length)
data=s.recv(int(length))
# print(data)
with open('file.json',"wb") as f:
    f.write(data)
# print("done")
