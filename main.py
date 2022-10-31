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

letraIndex = dict(zip(alfabeto, tamanhoAlfabeto))
indexLetra = dict(zip(tamanhoAlfabeto, alfabeto))

def cesarCripto(plaintext, troca):
    cifra = ''
    for letra in plaintext:
      if letra in alfabeto:
        index = ((letraIndex[letra] + troca) % len(alfabeto))
        letraCifra = indexLetra[index]
        cifra += letraCifra
      else:
        cifra += letra   
    return cifra 

resposta = input("Você deseja Criptografar ou Descriptografar uma mensagem? c/d ")
respostaFormat = resposta.lower()
mensagem = input("Insira a mensagem: ")
mensagemFormat = mensagem.lower()
rotacao = int(input("Insira o número de rotações: "))
if "d" in respostaFormat:
  print("Descriptografia: " + cesarCripto(mensagemFormat, -rotacao))
elif "c" in respostaFormat:  
  print("Criptografia: " + cesarCripto(mensagemFormat, rotacao))
else:
  print("Entrada inválida! Tente novamente:")