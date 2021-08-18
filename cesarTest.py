def cesar(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encriptedText = ''
    for later in text:
        index = alphabet.find(later)
        if index == -1:
            encriptedText += later
        else:
            newIndex = index + key
            newIndex = newIndex % len(alphabet)
            encriptedText += alphabet[newIndex:newIndex+1]
    return encriptedText


text, key = input("Digite o texto seguido da chave (separe por ,): ").strip().split(",")

key = int(key)

print(cesar(text.lower(), key))