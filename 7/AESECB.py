from Crypto.Cipher import AES


def aes_ecb(cipherfile, key):
    with open(cipherfile, 'r+') as f:
        ciphertext = f.read().decode('base64')
        mycipher = AES.new(key, AES.MODE_ECB)
        plaintext = mycipher.decrypt(ciphertext)
        return plaintext