# =================================
# Columnar Transposition Decryption
# =================================

# Assumption: Encryption key known
# ^^^^^^^^^^  -> Won't work without assumption

# PT: Plaintext, CT: Ciphertext
# ^^             ^^  

# Decryption Process
# ^^^^^^^^^^^^^^^^^^
# Calculate grid:
# No. of rows = key
# No. of columns = Ceil(CT Length / Key)
# No. of boxes to shade in = grid size - CT length
#   => Do this in the bottom of rightmost column
# Fill rows from left to right with CT
# Read the columns from left to right for PT

import math

def main():
    ciphertext = 'Atniy, hsso doh unauil iytnikg  eknhws,eotiu  w.'
    key = 8 # see assumption above

    plaintext = decryptMessage(key, ciphertext)

    print(plaintext)

# decrypt a given columnar transpositional CT
def decryptMessage(key, ciphertext):
    ciphertextLen = len(ciphertext)

    # calculate no. of columns in grid
    numCols = int(math.ceil(ciphertextLen / float(key)))
    # calculate no. of rows 
    numRows = key
    # calculate no. of shaded boxes
    numShaded = (numCols * numRows) - ciphertextLen
    # each string in plaintext represents a column in the grid
    plaintext = [''] * numCols
    # initialization 
    col = 0
    row = 0

    # main logic for decryption
    for symbol in ciphertext:
        plaintext[col] += symbol # add next plaintext symbol
        col +=1 # iterate to next column

        # if there are no more columns or we are at a shaded box
        #   start again from column 0 and next row
        if (col == numCols) or (col == numCols - 1 and row >= numRows - numShaded):
            col = 0
            row += 1

    # join plaintext
    return ''.join(plaintext)

# if run directly 
if __name__ == '__main__':
    main()