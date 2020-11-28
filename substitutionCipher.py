# ===================
# Substitution Cipher
# ===================

from affineCipher import encrypt
import random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(key, plaintext):
    return translatedMessage(key, plaintext, 'encrypt')

def decrypt(key, ciphertext):
    return translatedMessage(key, ciphertext, 'decrypt')

# return trnaslated message
def translatedMessage(key, message, mode):
    translated = ''
    charsA = SYMBOLS 
    charsB = key
    if mode == 'decrypt': # decryption happens with swapped symbol indexes
        charsA, charsB = charsB, charsA
    # translate each symbol in message, adding it to translated string
    for symbol in message:
        if symbol.upper() in charsA:
            symbolIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symbolIndex].upper()
            else:
                translated += charsB[symbolIndex].lower()
        else:
            translated += symbol
    return translated

def main():
    message = 'This is a run of the substitution cipher'
    letters = list(SYMBOLS) # generate random key
    random.shuffle(letters)
    key = ''.join(letters)

    mode = 'encrypt'
    if mode == 'encrypt':
        translated = encrypt(key, message)
    elif mode == 'decrypt':
        translated = decrypt(key, message)
    print('Using key: %s' % (key))
    print('The %sed message is:' % (mode))
    print(translated)

if __name__ == '__main__':
    main()