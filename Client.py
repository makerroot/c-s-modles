#encoding=utf-8
import socket, ssl, pprint,time
import rsa
# 导入密钥
frpu=open('public.pem','r')
pubkey = rsa.PublicKey.load_pkcs1(frpu.read().encode())


def main():
	while True:
		HOST = ''
		PORT = 8088
		BUFSIZE = 2048
		ADDR = (HOST,PORT)

		#创建套接字
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 从服务器请求一个ca证书
		ssl_sock = ssl.wrap_socket(s,ca_certs="cert.pem",cert_reqs=ssl.CERT_REQUIRED)
		#套接字连接
		ssl_sock.connect(ADDR)
		print("证书认证信息如下：")
		#显示证书
		pprint.pprint(ssl_sock.getpeercert())

		while True:
			# data="JKKKKKKKJJJL"
		    data =str(input('请输入你要发送的信息:'))
		    data =rsa.encrypt(data.encode(),pubkey)
		    #print("使用RSA加密后的信息")
		    #print(data)
		    if not data:
		        break
		    ssl_sock.send(data)
		    
		    data=ssl_sock.recv(BUFSIZE)
		    if not data:
		    	break
		    print(data)
		ssl_sock.close()
if __name__ == '__main__':
	main()


