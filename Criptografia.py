from tkinter import *

alfabeto = "abcdefghijklmnopqrstuvwxyz"
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
<<<<<<< HEAD
          print("A chave precisa ser um número natural!")
=======
          print("A chave precisa ser um número real!")
>>>>>>> 7f85d693d5e60a6d5e444db0d1f5df2b9a24b286
      else:
          print("A mensagem ultrapassa 128 caractéres, tente novamente!")

'''while continuarCripto == "s":
  coletaDados()
  continuarCripto = input("Digite a letra 's' para continuar ou qualquer outra tecla para encerrar a execução: ")
print("Programa finalizado!")'''

window = Tk()
window.title("Caesar's Cipher")

textPhrase = Label(window, text = "Enter the text: ")
textPhrase.grid(column=0, row=0, padx=10, pady=10)
plaintext = Entry(window, width=50)
plaintext.grid(column=0, row=1, padx=10, pady=3)

textShift = Label(window, text="Enter the number of shifts: ")
textShift.grid(column=0, row=2, padx=10, pady=10)
shift = Entry(window, width=10)
shift.grid(column=0, row=3, padx=10, pady=3)

buttonFrame = Frame(window)
buttonFrame.grid(column=0, row=4, padx=10, pady=10)

buttonCipher = Button(buttonFrame, text="Cipher text", width=10)
buttonCipher.pack(side="left")

buttonDecipher = Button(buttonFrame, text="Decipher text", width=10)
buttonDecipher.pack(side="right")

Result = Label(window, text="Result here!")
Result.grid(column=0, row=5, padx=10, pady=10)

window.mainloop()