import socket
import threading
c=socket.socket()
name=input("Enter your name")
msg=''
c.connect(('localhost',9999))
c.send(name.encode())
message=c.recv(1024).decode()
print(message)
message=c.recv(1024).decode()
print(message)
def send():
	global c
	while 1:
		global msg
		msg=input("You_message:")
		if len(msg)>0:
			c.send(msg.encode())
		if msg=="!DISCONNECT":
			break
def recv():
	global c
	while 1:
		global msg
		if msg=="!DISCONNECT":
			break
		msg3=c.recv(1024).decode() 
		msg2=c.recv(2048).decode()
		print(f"\n{msg3}\t:{msg2}")

recv_thread=threading.Thread(target=recv)
send_thread=threading.Thread(target=send)

send_thread.start()
recv_thread.start()




