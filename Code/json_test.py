import json
# data="""
# 	{"data":
#     {"new_connection":{
#         "connected" : "true",
#         "conn":"a" ,
#         "addr":"123.123.123" 	
        
#     },
#         "message":{
#             "msg":"",
#             "sender_conn":""
#         }
    
# 	}
#     }
# 		"""
# jason_data=json.loads(data)
# print(jason_data["data"]["new_connection"])
# got_data=jason_data[data]
# print(type(jason_data))
# with open("test.json") as f:
# 	data=json.load(f)
# 	print(data['data'])
# import socket
# from time import sleep
# def send(conn):
# 	with open("test.json","rb") as f:
# 		array=bytearray(f.read())
# 		# print(len(array))
# 		conn.send(str(len(array)).encode())
# 		sleep(1)
# 		conn.send(array)



# s=socket.socket()
# s.bind(('localhost',9999))
# s.listen()
# while 1:
# 	conn,addr=s.accept()
# 	conn.send("Hello".encode())
# 	send(conn)
# 	conn.close()
# 	print('done')
# 	break