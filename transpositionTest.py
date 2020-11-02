# ===================================
# Test Cases for Transposition Cipher
# ===================================

import random
from datetime import datetime
import sys # what does this do?
import transpositionCipher, decryptTranspositionCipher


def main():
    # get the RNG warmed up
    random.seed(datetime.now())

    # Generate 20 random test messages
    for i in range(20):
        # each message has random length
        message = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Shuffle the message characters for more randomization
        # convert to list, then shuffle
        message = list(message)
        random.shuffle(message)
        # convert list back to string
        message = ''.join(message)

        # show each test message as it's first 50 characters for convenience
        print('Test #%s: "%s..."' % (i+1, message[:50]))

        # Check message using all possible keys
        # Remember: key's range from 1 to half of message size
        for key in range(1, int(len(message)/2)):
            ciphertext = transpositionCipher.encryptMessage(key, message)
            plaintext = decryptTranspositionCipher.decryptMessage(key, ciphertext)

            # if the decryption is not equal to the plaintext
            # display error message then quit
            if message != plaintext:
                print('Error decrypting message %s with key %s' % (message, key))
                print('Decrypted as: ' + plaintext)
                sys.exit()

    # if here, then all test messages encrypt and decrypt properly
    print('Transposition cipher test passed.')

# if run directly, call main
if __name__ == '__main__':
    main()