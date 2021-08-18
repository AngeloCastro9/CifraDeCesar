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
    keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    for key in keys:
        key = int(key)
        print('Key:', key, 'Result:', cesar(encriptedText, key, False))

text, key = input("Digite o texto seguido da chave (separe por ,): ").strip().split(",")

key = int(key)

encripted = cesar(text.lower(), key, True)
print('Encripted', encripted)
bruteForce(encripted)