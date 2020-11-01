# ===================================
# Test Cases for Transposition Cipher
# ===================================

import random
import sys # what does this do?
import importlib
dtc = importlib.__import__('04_decryptTranspositionCipher')
etc = importlib.__import__('03_transpositionCipher')

# TODO: rename files to remove leading numbers -> things are breaking


def main():
    random.seed(40)

    # Generate 20 random test messages
    for i in range(20):
        # each message has random length
        messsage = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

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
        for key in range(1, len(message)/2):
            ciphertext = 
