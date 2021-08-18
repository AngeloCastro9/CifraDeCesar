def cesar(text, key, isDecripted):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encriptedText = ''
    for later in text:
        index = alphabet.find(later)
        if index == -1:
            encriptedText += later
        else:
            newIndex = index + key if isDecripted == True else index - key
            newIndex = newIndex % len(alphabet)
            encriptedText += alphabet[newIndex:newIndex+1]
    return encriptedText


def bruteForce(encriptedText):
    for key in range(26):
        key = int(key)
        print('Key:', key, 'Result:', cesar(encriptedText, key, False))

text, key = input("Input your text and key (separed by ,): ").strip().split(",")

key = int(key)

encripted = cesar(text.lower(), key, True)
print('Encripted', encripted)
bruteForce(encripted)