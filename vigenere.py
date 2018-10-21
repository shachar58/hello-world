#Shachar Frank and  Eran Haim
def translate (message, key, mode,cypher):
    key = key.upper()
    key_index = 0
    translated = []
    for char in message:
        num = cypher.find(char.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += cypher.find(key[key_index]) # add if encrypting
            elif mode == 'decrypt':
                num -= cypher.find(key[key_index]) # subtract if decrypting

            num %= len(cypher) # handle the potential wrap-around
             # add the encrypted/decrypted symbol to the end of translated.
            if char.isupper():
                translated.append(cypher[num])
            elif char.islower():
                translated.append(cypher[num].lower())
            key_index += 1 # move to the next letter in the key
            if key_index == len(key):
                key_index = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(char)
    return ''.join(translated)
