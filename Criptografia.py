alfabeto = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuWwXxYyZz"
tamanhoAlfabeto = range(len(alfabeto))

letterIndex = dict(zip(alfabeto, tamanhoAlfabeto))
indexLetter = dict(zip(tamanhoAlfabeto, alfabeto))

resultado = ""

def cesarEncrypt(plaintext, shift=3):
    cipher = ''

    for letter in plaintext:
        index = ((letterIndex[letter] + shift) % len(alfabeto))
        cipherLetter = indexLetter[index]
        cipher += cipherLetter  
    resultado = cipher    
    return resultado 

def cesarDecrypt(ciphertext, shift=-3):
    global encryptStatus
    encryptStatus = 3
    uncipher = ''
    for letter in ciphertext:
        index = ((letterIndex[letter] + shift) % len(alfabeto))
        cipherLetter = indexLetter[index]
        uncipher += cipherLetter  
    resultado = uncipher
    return resultado 

print("Criptografia: " + cesarEncrypt("Python", 8))
print("Descriptogragia: " + cesarDecrypt(cesarEncrypt("Python", 8), -8))