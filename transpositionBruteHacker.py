# ======================================
# Brute Hacking The Transposition Cipher
# ======================================
import decryptTranspositionCipher
import detectEnglish

# returns plaintext if a readable decryption is found, None otherwise
def hackTransposition(ciphertext):
    print("Decrypting..")
    print("This may take a while, press Ctrl-D to stop at any time.")

    # Brute-force: Loop through every possible key
    # keys for transposition cipher range from 1 to length of message
    for key in range(1, len(ciphertext)):
        print("Trying Key #%s...", (key))

        plaintext = decryptTranspositionCipher.decryptMessage(key, ciphertext)

        # if plaintext is readable, ask user if we should stop hacking
        if detectEnglish.isEnglish(plaintext):
            print()
            print('Possible plaintext:')
            print('Key: %s, Message: %s', (key, plaintext[:100]))
            print()
            print('Enter Y if done, anything else to continue hacking:')
            response = input('> ')
            # return PT if user satisfied with match
            if response.strip().upper() == 'Y':
                return plaintext

    # if we loop through all keys and none matched a potential plaintext, return None
    return None

def main():
    ciphertext = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""
    plaintext = hackTransposition(ciphertext)

    if plaintext == None:
        print()
        print('Unable to decrypt.')
    else:
        print()
        print('Original Plaintext:')
        print('===================')
        print(plaintext)

if __name__ == '__main__':
    main()
