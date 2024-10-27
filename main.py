
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys 
from Crypto.Hash import HMAC, SHA256
import time

#codigo para ser criptografado
 
data = 'Banana'.encode()

palavra_chave=input("Digite a chave:")


palavra_chave_bytes = b''

#tranforma a palavra chave em bits e verificando se é string ou int

if palavra_chave.isdigit():
 
    palavra_chave_int = int(palavra_chave)
    
    palavra_chave_bytes = palavra_chave_int.to_bytes((palavra_chave_int.bit_length() + 7) // 8, byteorder='big')                                                                                                                                          #essa linha ela tranforma o inteiro em bytes e também diminui a quantidade de byts necessario pela conta 7//8 e ainda o byteorder especifica a ordem dos bytes na representação em bytes. big significa que os bytes mais significativos vêm primeiro
else:
   
    palavra_chave_bytes = palavra_chave.encode()



hmac = HMAC.new(palavra_chave_bytes, digestmod=SHA256)
hmac.update(get_random_bytes(16))

#pega a quantidades de bits na chave e atribui seguindo a ordem os primeiros 16 e os ultimos 16
aes_key = hmac.digest()[:16]  
hmac_key = hmac.digest()[16:]  


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
 

time.sleep(2.5)
#alterar a chave 
#tag= cipher.nonce + aes_key


time.sleep(2.5)

#with open("encrypted.bin", "wb") as f:
    #f.write(tag)
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