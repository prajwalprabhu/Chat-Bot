import socket
c=socket.socket()
c.connect(('localhost',9999))
msg=c.recv(1024).decode()
file_name=c.recv(1024).decode()
print(msg,file_name)
sent=False
lenght=c.recv(1024).decode()
data=c.recv(int(lenght))
	
	
with open(file_name,"wb") as file:
    file.write(data) 


