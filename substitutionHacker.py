# ==========================
# Substitution Cipher Hacker
# ==========================

import os, copy, re, substitutionCipher, wordPatterns, makeWordPatterns

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpaces = re.compile('[^A-Z\s]')

def getBlankCipherletterMapping():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 
    'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
    'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
    'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

# maps letters in candidate to respectice index in cipherWord, 
# adds that letter to letterMapping if not already there
# EX: if PUPPY is the candidate to HGHHU, map P to H, U to G & Y to U
def addLettersToMappings(letterMapping, cipherWord, candidate):
    for i in range(len(cipherWord)):
        if candidate[i] not in letterMapping[cipherWord[i]]:
            letterMapping[cipherWord[i]].append(candidate[i])

def intersectMappings(mapA, mapB):
    return -1

def hackSubstitutionCipher(ciphertext):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpaces.sub('', ciphertext.upper()).split()

def main():
    ciphertext = ''
    print('Hacking...')
    letterMapping = hackSubstitutionCipher(ciphertext)

    # Diplay results 
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original Ciphertext:')
    print(ciphertext)
    print()

if __name__ == '__main__':
    main()