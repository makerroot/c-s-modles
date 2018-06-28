# C-S
实现身份认证和RSA（2048位）算法
首先使用语句openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem申请身份认证的公私钥；
使用python3 pubpriv.py生成RSA（2048位）的加密和解密的公私钥；
使用python3 Server.py来开启服务；
使用python3 Client.py来开启客户端；
接下来就可以进行通信。
