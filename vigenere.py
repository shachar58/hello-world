#Shachar Frank and  Eran Haim
import random
currentSession=0
import Letters

LettersDir={}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translate (message, key, mode,sessionIndex):
    if sessionIndex in LettersDir.keys():
        letters = LettersDir[sessionIndex]
    else:
        print("changed letters !")
        defineLetters(sessionIndex)
        letters=LettersDir[sessionIndex]
    print(sessionIndex,", ",LettersDir[sessionIndex])
    key = key.upper()
    key_index = 0
    translated = []
    message=''.join(message)
    for char in message:
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
            translated.append(char)
    return ''.join(translated)


def defineLetters (sessionIndex):
    LettersDir[sessionIndex]=shuffle_string(letters)

def shuffle_string(string):
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)