def cesar(text, key, isEncripted):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encriptedText = ''
    for letter in text:
        index = alphabet.find(letter)
        if index == -1:
            encriptedText += letter
        else:
            newIndex = index + key if isEncripted == True else index - key
            newIndex = newIndex % len(alphabet)
            encriptedText += alphabet[newIndex:newIndex+1]
    return encriptedText


def bruteForce(encriptedText):
    for key in range(26):
        key = int(key)
        print('Key:', key, 'Result:', cesar(encriptedText, key, False))

text, key = input("Input your text and key (separed by ,): ").strip().split(",")

key = int(key)

encriptedText = cesar(text.lower(), key, True)
print('Encripted', encriptedText)
bruteForce(encriptedText)