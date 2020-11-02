# ===========================
# Detect A Readable Plaintext
# ===========================

# Through a brute force method, if we have every possible key 
# and plaintext combination: 
# This program will detect the sensible/readable plaintext
# which is most likely, for that reason, 
# the correct decrypted message

# METHOD OVERVIEW:
# ^^^^^^^^^^^^^^^
# split decrypted string into individual substrings
# check if each substring exists as a word in the dictionary.txt
# if a certain % of words are English:
# we classify that plaintext as English

# TO USE THIS CODE:
# ^^^^^^^^^^^^^^^^
# import detectEnglish
# call detectEnglish.isEnglish(your_string) => returns True or False

# TODO: check if LETTERS_AND_SPACE needs to have lower case letters added to it

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # for convenience
# setup a variable to contain upper & lower case letters, space, tab and new line
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n' 

# loads dictionary words from file and returns as dictionary
def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    # iterate over every line in the file as a word
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()
WRDPCT, LTRPCT = 20, 85

# return ratio of recognized english words to total words
# output: [0.0,...,1.0]
def getEnglishCount(message):
    message = message.upper() # convert text to all uppercase
    message = removeNonLetters(message) # remove numbers & punctuation
    possibleWords = message.split() # split based on whitespace into a list

    # if possibleWords list after non-letter removal and otherwise is empty
    if possibleWords == []:
        return 0.0 # no possible words
    
    matches = 0
    # check each word for a match
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches +=1
    
    return float(matches)/len(possibleWords) # return float value of ratio

# helper function that removes numbers & punctuation from string
def removeNonLetters(message):
    lettersOnly = [] # empty list holder for wanted symbols 
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)
 
# This function should be called to detect if the message is in english
# return True if words and letters match above required threshhold for each
def isEnglish(message, wordPercentage=WRDPCT, letterPercentage=LTRPCT):
    # by default 20% words in message must be English and
    # 85% of all the characters in the message must be letters or spaces
    # punctuation or numbers not allowed in count
    
    #check if words match above the threshold
    wordMatch = getEnglishCount(message) * 100 >= wordPercentage
    
    numLetters = len(removeNonLetters(message))
    # check if letters matches above the threshold
    letterMatch = float(numLetters) / len(message) * 100 >= letterPercentage
    # return True or False
    return wordMatch and letterMatch

def main():
    a = isEnglish('This is english.') # T
    b = isEnglish('This is also english') # T
    c = isEnglish('18937 3838 andhi 0 not english. a a a') # F

    print(a)
    print(b)
    print(c)

if __name__ == '__main__':
    main()