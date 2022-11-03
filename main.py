alfabeto = "abcçdefghijklmnopqrstuvwxyz"
tamanhoAlfabeto = range(len(alfabeto))
continuarCripto = "s"

#Cria um dicionário juntando a chave "alfabeto" e o valor "tamanhoAlfabeto"
letraIndex = dict(zip(alfabeto, tamanhoAlfabeto))

#Cria um dicionário juntando a chave "tamanhoAlfabeto" e o valor "alfabeto"
posicaoIndex = dict(zip(tamanhoAlfabeto, alfabeto))

def cesarCripto(plaintext, troca):
    cifra = ''
    for letra in plaintext:
      if letra in alfabeto:
        index = ((letraIndex[letra] + troca) % len(alfabeto))
        letraCifra = posicaoIndex[index]
        cifra += letraCifra
      else:
        cifra += letra   
    return cifra 

def coletaDados():
  resposta = input("Você deseja Criptografar ou Descriptografar uma mensagem? c/d ")
  respostaFormat = resposta.lower()
  if respostaFormat != "d" and respostaFormat != "c":
    print("Entrada inválida! Tente novamente!")
  else:
      mensagem = input("Insira a mensagem: ")
      if len(mensagem) <= 128:
        mensagemFormat = mensagem.lower()
        rotacao = int(input("Insira a chave: "))
        if "d" in respostaFormat:
          print("Descriptografia: " + cesarCripto(mensagemFormat, -rotacao))
        else:  
          print("Criptografia: " + cesarCripto(mensagemFormat, rotacao))
      else:
        print("A mensagem ultrapassa 128 caractéres, tente novamente!")

while continuarCripto == "s":
  coletaDados()
  continuarCripto = input("Digite a letra 's' para continuar ou qualquer outra tecla para encerrar a execução: ")
print("Programa finalizado!")