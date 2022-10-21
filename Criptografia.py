#alfabeto = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz "
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

tamanhoAlfabeto = range(len(alfabeto))

#dict = dicionário -> dict(zip()) = percorre todo o dicionário e atribui ao alfabeto 
# o número da string (print(letraIndex)) e (print(IndexLetra)) para melhor entendimento.

#Cria um índice amarrando um caracter da variável "alfabeto" na sua posiç ão da string, pela variável "tamanhoAlfabeto"
letraIndex = dict(zip(alfabeto, tamanhoAlfabeto))

#Cria um índice amarrando um número da variável "tamanhoAlfabeto" com o caracter na variável "alfabeto"
indexLetra = dict(zip(tamanhoAlfabeto, alfabeto))

resultado = ""

def cesarCripto(plaintext, troca):
    cifra = ''

    for letra in plaintext:
        index = ((letraIndex[letra] + troca) % len(alfabeto))
        letraCifra = indexLetra[index]
        cifra += letraCifra  
    resultado = cifra    
    return resultado 

def cesarDescripto(ciphertext, troca):
    uncipher = ''
    for letra in ciphertext:
        index = ((letraIndex[letra] + troca) % len(alfabeto))
        cipherLetter = indexLetra[index]
        uncipher += cipherLetter  
    resultado = uncipher
    return resultado 

resposta = input("Você deseja Criptografar ou Descriptografar uma mensagem? c/d ")
resposta.lower()

if "d" in resposta:
  descriptografar = input("Insira o texto que quer Descriptografar: ")
  rotacao = int(input("Insira o número de rotações: "))
  print("Descriptogragia: " + cesarDescripto(descriptografar, -rotacao))
else:  
  criptografar = input("Insira o texto que quer Criptografar: ")
  rotacao = int(input("Insira o número de rotações: "))
  print("Criptografia: " + cesarCripto(criptografar, rotacao))