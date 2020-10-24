# =================
# The Ceasar Cipher
# =================

# key space K <- {0..25}
#   the key space is from the traditional ceasar cipher
#   where only alphabets are allowed & in one chosen case (hence mod 26)
#   but we could've chosen it to be total length of SYMBOLS below
# message space M <- (inf)
# output space O <- (inf)

# string to encrypt/decrypt
message = 'XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V'

# encryption key -> k
key = 22 

# program mode: encrypt (1), decrypt (2)
mode = 2 # currently set to decrypt

# all the symbols that could be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# store the transformed form of the message 
output = ''

# CIPHER LOGIC
# generate output by applying transformation to every
# symbol in the message, iteratively building output
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # perform transformation
        if mode == 1: # ENCRYPT
            transformedIndex = symbolIndex + key
        else: # DECRYPT
            transformedIndex = symbolIndex - key

        # handle wraparound (if needed)
        # transformedIndex may hold a higher value than len(SYMBOLS)
        if transformedIndex >= len(SYMBOLS):
            transformedIndex = transformedIndex - len(SYMBOLS)
        # transformedIndex may hold a negative value during decrypt
        elif transformedIndex < 0:
            transformedIndex = transformedIndex + len(SYMBOLS)

        output = output + SYMBOLS[transformedIndex]
    else:
        # Symbol not part of allowed symbols
        # handle it by appending without transforming
        output = output + symbol

print(output)

# END OF PROGRAM
