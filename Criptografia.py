alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
tamanhoAlfabeto = range(len(alfabeto))

letraIndex = dict(zip(alfabeto, tamanhoAlfabeto))
indexLetra = dict(zip(tamanhoAlfabeto, alfabeto))

def cesarCripto(plaintext, troca):
    cifra = ''
    for letra in plaintext:
        index = ((letraIndex[letra] + troca) % len(alfabeto))
        letraCifra = indexLetra[index]
        cifra += letraCifra   
    return cifra 

resposta = input("Você deseja Criptografar ou Descriptografar uma mensagem? c/d ")
resposta.lower()
mensagem = input("Insira a mensagem: ")
rotacao = int(input("Insira o número de rotações: "))
if "d" in resposta:
  print("Descriptogragia: " + cesarCripto(mensagem, -rotacao))
else:  
  print("Criptografia: " + cesarCripto(mensagem, rotacao))