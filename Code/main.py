import socket 
import threading
connected=True
s=socket.socket()
s.bind(('localhost',9999))
message="Welcome to cool server \n To disconnected send !DISCONNECT"
DISCONNECT_message="You Have been disconnected from the server "
msg=''
conn_list=[]
connected_people={}

def listen(conn,addr):
	global connected,msg
	connected=True
	while connected:
		name=connected_people[conn]
		msg=conn.recv(1024).decode()
		if len(msg)>0:
			if msg=="!DISCONNECT":
				
				name=connected_people[conn]
				print(name,"Has disconnected")
				
				send(conn,addr,DISCONNECT_message,name)
				for connn in conn_list:
					if not connn==conn:
						connn.send(name.encode())
						connn.send("Has been disconnected".encode())

				conn.close()
				index=conn_list.index(conn)
				conn_list.pop(index)
				connected=False
			else:
				for connn in conn_list:
					if not connn==conn:
				
						
						send(connn,addr,msg,name)
						# print(name)

				# print(msg)
def send(conn,addr,msg,name):
	global conn_list
	# for connn in conn_list:
	# 	if not connn==conn:
	conn.send(name.encode())
	conn.send(msg.encode())
def client_handle(conn,addr):
	global conn_list,connected_people
	
	no=str(len(conn_list)-1)
	conn.send(message.encode())
	conn.send(f"{no}are online now\n".encode())

	name=conn.recv(1024).decode()
	print(f"[Newconnection]:{name}({addr})has been connected")
	connected_people[conn]=name
	for connn in conn_list:
		if not connn==conn:
			connn.send(name.encode())
			conn.send("Connected to the server".encode())

	

	thread=threading.Thread(target=listen,args=(conn,addr))
	thread.start()
def start():
	print("[Starting] the srver is strting.....\n [Started]:server is listening......")
	s.listen()
	while 1:

		conn,addr=s.accept()
		conn_list.append(conn)
		thread=threading.Thread(target=client_handle,args=(conn,addr))
		thread.start()
start()