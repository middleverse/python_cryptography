# ===============
# Vigenere Cipher
# ===============

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translateMessage(key, message, mode):
    translated = [] # hold translated message here
    keyIndex = 0
    key = key.upper() # for simplicity

    # for each symbol, translate it with keyIndex
    # if encrypting, add the keyIndex
    # if decrypting, subtract the keyIndex
    for symbol in message:
        symbolIndex = LETTERS.find(symbol.upper())
        # if symbol is in LETTERS, translate
        if symbolIndex != -1:
            if mode == 'encrypt':
                symbolIndex += LETTERS.find(key[keyIndex])
            elif mode =='decrypt':
                symbolIndex -= LETTERS.find(key[keyIndex])
            symbolIndex %= len(LETTERS) # wrap around
            # append with appropriate case
            if symbol.isupper():
                translated.append(LETTERS[symbolIndex].upper())
            else:
                translated.append(LETTERS[symbolIndex].lower())
            # move key to the next letter
            keyIndex = (keyIndex + 1) % len(key)

        # otherwise append as-is
        else:
            translated.append(symbol)        
    return ''.join(translated) # convert list into str


def encrypt(key, plaintext):
    return translateMessage(key, plaintext, 'encrypt')

def decrypt(key, ciphertext):
    return translateMessage(key, ciphertext, 'decrypt')

def main():
    # "Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."
    message = '''Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf.'''
    key = 'ASIMOV'
    mode = 'decrypt'

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