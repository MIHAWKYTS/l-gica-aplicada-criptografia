from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys 
from Crypto.Hash import HMAC, SHA256


#codigo para criptografar 
data = 'Banana'.encode()
aes_key = get_random_bytes(16)
hmac_key = get_random_bytes(16)

cipher = AES.new(aes_key, AES.MODE_CTR)
ciphertext = cipher.encrypt(data)

#criar um arquivo e escrever e colocar as tag,cipher,ciphertext
hmac = HMAC.new(hmac_key, digestmod=SHA256)
tag = hmac.update(cipher.nonce + ciphertext).digest()
with open("encrypted.bin", "wb") as f:
    f.write(tag)
    f.write(cipher.nonce)
    f.write(ciphertext)
#precisamos alterar algumas das tag ,para mostrar que o codigo consegue editar alteração
 

#ler o arquivo criado e checa pra ver se tem alteração
with open("encrypted.bin", "rb") as f:
    tag = f.read(32)
    nonce = f.read(8)
    ciphertext = f.read()  

try:
    hmac = HMAC.new(hmac_key, digestmod=SHA256)
    tag = hmac.update(nonce + ciphertext).verify(tag)
except ValueError:
    print("The message was modified!")
    sys.exit(1)
#descriptografa e exibi a mensagem
cipher = AES.new(aes_key, AES.MODE_CTR, nonce=nonce)
message = cipher.decrypt(ciphertext)
print("Message:", message.decode())