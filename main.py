""""#https://realpython.com/python-gui-tkinter/
import tkinter as tk
window = tk.Tk()
greeting = tk.Label(
  text="Programa de Criptografia",
  width=40,
  height=3
)
greeting.pack()
mensagem = tk.Label(text="Insira a mensagem")
entry = tk.Entry()
mensagem.pack()
entry.pack()
Cript_btn = tk.Button(
    text="Criptografar",
    width=10,
    height=2,
    bg="blue",
    fg="yellow",)
Dcript_btn = tk.Button(
    text="Descriptografar",
    width=10,
    height=2,
    bg="blue",
    fg="yellow",)
Cript_btn.pack(), Dcript_btn.pack()
window.mainloop()"""

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