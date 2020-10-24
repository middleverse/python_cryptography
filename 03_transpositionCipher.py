# ===================================
# Columnar Transposition Cipher (CTC)
# ===================================

# Key Space <- {2,..,n/2} 
# ^^^^^^^^^  where n is length of message

# Note: longer messages allow for more key choices
# ^^^^

# Example: Encrypting an entire book using CTC
# ^^^^^^^  would allow for thousands of possible keys

def main():
    # message to be encrypted
    plaintext = 'A day without sunshine, is like you know, night.'
    
    # chosen key
    key = 8 

    # encrypt message
    ciphertext = encryptMessage(key, plaintext)
    print(ciphertext)

# function to encrypt message using key and CTC
def encryptMessage(key, message):
    # each string in ciphertext represents a column in the grid
    # No. of columns  = key
    ciphertext = [''] * key

    # loop through each column in the ciphertext
    for column in range(key):
        curIndex = column

        # keep looping until curIndex goes past the message length
        #    at the point it's time to move to next column in CT
        while curIndex < len(message):
            # Place the character at curIndex in message at the
            # end of the current column in the ciphertext list
            ciphertext[column] += message[curIndex]

            # Increment curIndex to next value (add key)
            curIndex += key

    # convert CT list into a single string value
    # return new CT
    return ''.join(ciphertext)

# if this file is not used as module, call main()
if __name__ == '__main__':
    main()




    