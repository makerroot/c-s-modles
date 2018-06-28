import rsa
import os
print("密钥生成前的文件有：")
print(os.listdir())
# 生成密钥
(pubkey, privkey) = rsa.newkeys(2048)


# 保存密钥
fwpu=open('public.pem','w+')
fwpu.write(pubkey.save_pkcs1().decode())

fwpr=open('private.pem','w+') 
fwpr.write(privkey.save_pkcs1().decode())
print("公钥和私钥创建成功之后的文件有：")
print(os.listdir())
