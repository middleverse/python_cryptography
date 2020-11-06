# =================
# The Affine Cipher
# =================
import sys, cryptomath, random

# The affine cipher is a type of monoalphabetic substitution cipher, 
# where each letter in an alphabet is mapped to its numeric equivalent, 
# encrypted using a simple mathematical function, and converted back 
# to a letter. The formula used means that each letter encrypts to one 
# other letter, and back again, meaning the cipher is essentially a 
# standard substitution cipher with a rule governing which letter goes 
# to which. [Source: Wikipedia]

# ENCRYPTION
# ^^^^^^^^^^
# PT -> multiply by Key A -> Add Key B -> Mod by set size (m) -> CT

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Split key into KeyA and KeyB
# Not the safest trick, but gets the job done
def getTwoKeys(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    return -1

def encrypt(key, plaintext):
    # create random keys A and B
    keyA, keyB = getTwoKeys(key)
    checkKeys(keyA, keyB, 'encrypt')

def decrypt(key, ciphertext):
    return -1

def main():
    # message, key and mode configuration
    message = """"A computer would deserve to be called intelligent 
    if it could deceive a human into believing that it was human."
    -Alan Turing"""
    key = 2894
    mode = 'encrypt' # choose between 'encrypt' or 'decrypt'
    if mode == 'encrypt':
        translatedMessage = encrypt(key, message)
    elif mode == 'decrypt':
        translatedMessage = decrypt(key, message)
    
    # print output
    print('Key: %s' % key)
    print('%sed text: ' % mode.title())
    print(translatedMessage)


    