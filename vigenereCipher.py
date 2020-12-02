# ===============
# Vigenere Cipher
# ===============

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(key, plaintext):
    return -1

def decrypt(key, ciphertext):
    return -1

def main():
    message = '''Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist.'''
    key = 'ASIMOV'
    mode = 'encrypt'

    if mode == 'encrypt':
        translated = encrypt(key, message)
    elif mode == 'decrypt':
        translated = decrypt(key, message)
    
    print('Mode: %s' % (mode))
    print()
    print('Original Message: "%s"' % (message))
    print()
    print('Translated Message: "%s"' % (translated))
    print()

main()