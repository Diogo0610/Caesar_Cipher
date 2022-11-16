alfabeto = "abcçdefghijklmnopqrstuvwxyz"
tamanhoAlfabeto = range(len(alfabeto))
continuarCripto = "s"

letraIndex = dict(zip(alfabeto, tamanhoAlfabeto))
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
        rotacao = input("Insira a chave numérica: ")
        numero = rotacao.isnumeric()
        if numero:
          rotacao = int(rotacao)
          if "d" in respostaFormat:
            print("Descriptografia: " + cesarCripto(mensagemFormat, -rotacao))
          else:  
            print("Criptografia: " + cesarCripto(mensagemFormat, rotacao))
        else:
          print("A chave precisa ser um número real!")
      else:
          print("A mensagem ultrapassa 128 caractéres, tente novamente!")

while continuarCripto == "s":
  coletaDados()
  continuarCripto = input("Digite a letra 's' para continuar ou qualquer outra tecla para encerrar a execução: ")
print("Programa finalizado!")