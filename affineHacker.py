# ========================
# The Affine Cipher Hacker
# ========================

import affineCipher, detectEnglish, cryptomath
from affineCipher import SYMBOLS

SILENT_MODE = False

# return None if not able to crack the code, otherwise returns potential plaintext
def hackAffine(ciphertext):
    print('Hacking...')
    print('(Print CTRL-C to quit at any time.)')
    # total number of possible keys is len of SYMBOLS ** 2 
    for key in range(len(SYMBOLS) ** 2):
        keyA = affineCipher.getTwoKeys(key)[0] 
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue
        plaintext = affineCipher.decrypt(key, ciphertext)
        if not SILENT_MODE:
            print('Tried Key %s: %s' % (key, plaintext[:50]))
        if detectEnglish.isEnglish(plaintext, 50, 20):
            # Check with the user if this decryption is acceptable
            print()
            print('Possible decrypted plaintext found.')
            print('Key: %s' % (key))
            print('Decrypted message: ' + plaintext[:50])
            print()
            print('Enter A for accept, or Enter for continue hacking...')
            response = input('> ')
            if response.strip().upper().startswith('A'):
                return plaintext
    return None

def main():
    ciphertext = """"FvLE0JidVTvsEi5QvQVYVTnVvdEvGVvLB55VQvp-dV55pfV-dvpavpdvLEi5QvQVLVpnVvBvki0B-vp-dEvGV5pVnp-fvdkBdvpdvsBYvki0B- "vAvF5B-vhiTp-f"""
    hackedMessage = hackAffine(ciphertext)    
    if hackedMessage == None:
        print('Failed to hack the ciphertext.')
    else:
        print(hackedMessage)
    
if __name__ == '__main__':
    main()
