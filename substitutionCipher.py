from affineCipher import encrypt
import random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.-'

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
        if symbol in charsA:
            symbolIndex = charsA.find(symbol)
            translated += charsB[symbolIndex]
        else:
            translated += symbol
    return translated

if __name__ == '__main__':
    main()