#encoding=utf-8
import socket, ssl, time
import rsa
frpr=open('private.pem','r')
privkey = rsa.PrivateKey.load_pkcs1(frpr.read().encode())



def do_something(connstream, data):
		
		print("客户端发送的加密信息为：",data)
		data=rsa.decrypt(data,privkey).decode()
		print("服务器端解密后的信息为：",data)
		
		
		

def recv_from_client(connstream):
    data = connstream.recv(BUFSIZE)
    while data:
        backdata = do_something(connstream,data)
        if not backdata:
            break
        connstream.send(backdata)
        data = connstream.recv(BUFSIZE)
        # data =rsa.decrypt(data,privkey).decode()
    return data

def sslstart():
	
	while True:
	    newsocket, fromaddr = bindsocket.accept()
	    print ("客户端ip信息为： ",fromaddr)

	    connstream = ssl.wrap_socket(newsocket, "key.pem", "cert.pem", server_side=True, ssl_version = ssl.PROTOCOL_TLSv1)

	    try:
	    	recv_from_client(connstream)

	    finally:
	        connstream.shutdown(socket.SHUT_RDWR)
	        connstream.close()
if __name__ == '__main__':
	while True:
		HOST = ''
		PORT = 8088
		BUFSIZE = 2048
		ADDR = (HOST,PORT)
		#创建套接字
		bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#绑定
		bindsocket.bind(ADDR)
		#监听
		bindsocket.listen(5)
		sslstart()

