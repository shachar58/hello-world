#Shachar Frank and  Eran Haim
<<<<<<< HEAD
def translate (message, key, mode):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
=======

def translate (message, key, mode,cypher):  #the main function for encrypting and decrypting
>>>>>>> shachar_change
    key = key.upper()
    key_index = 0
    translated = []
    for char in message:
<<<<<<< HEAD
        num = letters.find(char.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += letters.find(key[key_index]) # add if encrypting
            elif mode == 'decrypt':
                num -= letters.find(key[key_index]) # subtract if decrypting

            num %= len(letters) # handle the potential wrap-around
             # add the encrypted/decrypted symbol to the end of translated.
            if char.isupper():
                translated.append(letters[num])
            elif char.islower():
                translated.append(letters[num].lower())
            key_index += 1 # move to the next letter in the key
            if key_index == len(key):
                key_index = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
=======
        num = cypher.find(char.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += cypher.find(key[key_index]) # add if encrypting
            elif mode == 'decrypt':
                num -= cypher.find(key[key_index]) # subtract if decrypting

            num %= len(cypher) # handle the potential wrap-around

            if char.isupper():      # add the encrypted/decrypted symbol to the end of translated
                translated.append(cypher[num])
            elif char.islower():
                translated.append(cypher[num].lower())
            key_index += 1 # move to the next letter in the key
            if key_index == len(key):   #the index is reset if it reach the final letter
                key_index = 0
        else:
            # The symbol was not in "char", so add it to translated as is.
>>>>>>> shachar_change
            translated.append(char)
    return ''.join(translated)
