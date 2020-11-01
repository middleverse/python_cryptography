# =============
# Rverse Cipher
# =============

plaintext = '.daed era meht fo owt fi ,terces a peek nac eerhT'
ciphertext = ''

# starting from end of plaintext, move backwards
# build ciphertext character by character
i = len(plaintext) - 1

while i >=0:
    # add current character i to end of ciphertext
    ciphertext = ciphertext + plaintext[i]
    i = i - 1

print(ciphertext)

# END OF PROGRAM