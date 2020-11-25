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

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.-'

# Split key into KeyA and KeyB
# Not the safest trick, but gets the job done
def getTwoKeys(key):
    keyA = key // len(SYMBOLS) # multiplication key
    keyB = key % len(SYMBOLS) # addition key
    return (keyA, keyB)

def checkForWeakKeys(keyA, keyB, mode):
    if mode == 'encrypt':
        if keyA <= 1:
            sys.exit('KeyA = 1 is a weak key. Choose a different key.')
        if keyB == 0:
            sys.exit('KeyB = 0 is a weak key. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
            sys.exit('Key A must be greater than 0 and key B must be between 0 and %s' % (len(SYMBOLS) - 1))
    # check if keyA and len(symbols) are coprime
    if cryptomath.gcd(keyA, len(SYMBOLS) - 1) != 1:
            print('here')
            sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. CHoose a different key.' % (keyA, len(SYMBOLS) - 1))

def encrypt(key, plaintext):
    # create random keys A (for multi) and B (for add)
    keyA, keyB = getTwoKeys(key)
    checkForWeakKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in plaintext:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            # E(x) = a*x + b mod m
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol
    return ciphertext

def decrypt(key, ciphertext):
    plaintext = ''
    keyA, keyB = getTwoKeys(key)
    checkForWeakKeys(keyA, keyB, 'decrypt')
    # calcualte 'c', mod inverse of 'a'
    keyC = cryptomath.findModInverse(keyA, len(SYMBOLS))
    for symbol in ciphertext:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            # D(x) = c(x-b) mod m
            plaintext += SYMBOLS[keyC * (symbolIndex - keyB) % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext

def main():
    # message, key and mode configuration
    message = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." - Alan Turing"""
    key = 340
    mode = 'encrypt' # choose between 'encrypt' or 'decrypt'
    if mode == 'encrypt':
        translatedMessage = encrypt(key, message)
    elif mode == 'decrypt':
        translatedMessage = decrypt(key, message)
    
    # print output
    print('Key: %s' % key)
    print('%sed text: ' % mode.title())
    print(translatedMessage)


main()