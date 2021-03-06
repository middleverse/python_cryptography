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

# maps letters in candidate to respective index in cipherWord, 
# adds that letter to letterMapping if not already there
# EX: if PUPPY is the candidate to HGHHU, map P to H, U to G & Y to U
def addLettersToMapping(letterMapping, cipherWord, candidate):
    for i in range(len(cipherWord)):
        if candidate[i] not in letterMapping[cipherWord[i]]:
            letterMapping[cipherWord[i]].append(candidate[i])

# returns intersection of two maps
def intersectMappings(mapA, mapB):
    intersectedMapping = getBlankCipherletterMapping()
    for symbol in SYMBOLS:
        # if a symbol has no mappings in one  of the maps
        # copy the other map entirely into intersectedMapping
        if mapA[symbol] == []:
            intersectedMapping[symbol] = copy.deepcopy(mapB[symbol])
        elif mapB[symbol] == []:
            intersectedMapping[symbol] = copy.deepcopy(mapA[symbol])
        # if a symbol appears in both maps, add that symbol to the mapping
        else:
            for mappedLetter in mapA[symbol]:
                if mappedLetter in mapB[symbol]:
                    intersectedMapping[symbol].append(mappedLetter)
    return intersectedMapping
        
def removeSolvedLettersFromMapping(letterMapping):
    loopAgain = True
    while loopAgain:
        # assume we won't loop again
        loopAgain = False
        # make a list of solved letters
        solvedLetters = []
        for cipherletter in SYMBOLS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])
        # delete solved letters from all cipherletters where the maps is greater than 1
        for cipherletter in SYMBOLS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1: # another solved letter, hence loop again
                        loopAgain = True # TODO: can't this line just be 'append to solved' 
    return letterMapping

def hackSubstitutionCipher(ciphertext):
    intersectedMap = getBlankCipherletterMapping()
    # remove non letters or space from 
    nonSpacedCipherWordList = ciphertext.upper().split()
    cipherwordList = nonLettersOrSpaces.sub('', ciphertext.upper()).split()
    
    for cipherword in cipherwordList:
        # get cipher letter mapping
        candidateMap = getBlankCipherletterMapping()
        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue # do nothing if word in not in our dictionary
        # add the letters of each cipherword to the mapping
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)
        # intersect mappings so far with current candidate mapping
        intersectedMap = intersectMappings(intersectedMap, candidateMap)
        # remove all solved letters
    return removeSolvedLettersFromMapping(intersectedMap)

def decryptWithMapping(ciphertext, letterMapping):
    # return the decrypted ciphertext string
    # with any ambiguous decrypted letters replaced with an underscore

    # create a key from the letterMapping
    key = ['x'] * len(SYMBOLS) 
    for cipherletter in SYMBOLS:
        if len(letterMapping[cipherletter]) == 1:
            # if there's only one letter, add it to key
            keyIndex = SYMBOLS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)
    print(key)

    return substitutionCipher.decrypt(key, ciphertext)

def main():
    ciphertext = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    print('Hacking...')
    letterMapping = hackSubstitutionCipher(ciphertext)

    # Diplay results 
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original Ciphertext:')
    print(ciphertext)
    print()
    hackedPlaintext = decryptWithMapping(ciphertext, letterMapping)
    print(hackedPlaintext)

if __name__ == '__main__':
    main()