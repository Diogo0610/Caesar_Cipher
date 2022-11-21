from tkinter import *

#variáveis 
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetSize = range(len(alphabet))

#Atribuição de chaves e valores entre as variáveis
letterIndex = dict(zip(alphabet, alphabetSize))
positionIndex = dict(zip(alphabetSize, alphabet))

def caesarCipher():
  plaintext = originalText.get().lower()
  plaintext.lower()
  lshift = int(shift.get())
  cipher = ""
  if len(originalText.get()) <= 128:
    for letter in plaintext:
      if letter in alphabet:
        index = ((letterIndex[letter] + lshift) % len(alphabet))
        letterCipher = positionIndex[index]
        cipher += letterCipher
      else:
        cipher += letter
    else:
      result["text"] = "This text is too long. Fit to 128 characters."
  result["text"] = cipher

def caesarDecipher():
  plaintext = originalText.get().lower()
  plaintext.lower()
  lshift = int(shift.get())
  cipher = ""
  if len(originalText.get()) <= 128:
    for letter in plaintext:
      if letter in alphabet:
        index = ((letterIndex[letter] - lshift) % len(alphabet))
        letterCipher = positionIndex[index]
        cipher += letterCipher
      else:
        cipher += letter
    else:
      result["text"] = "This text is too long. Fit to 128 characters."
  result["text"] = cipher

#Interface
#Criação da janela
window = Tk()
window.title("Caesar's Cipher")

#Textos de orientação
htuText0 = Label(window, text = "Read some warnings before using:")
htuText0.grid(column=0, row=0, padx=10, pady=10)
htuText1 = Label(window, text = "* All uppercase characters will be converted in lowercase;")
htuText1.grid(column=0, row=1, padx=10)
htuText2 = Label(window, text = "* All symbols or numbers will remain in the final cipher;")
htuText2.grid(column=0, row=2, padx=10)
htuText3 = Label(window, text = "* Character limit is set to in 128;")
htuText3.grid(column=0, row=3, padx=10)
htuText4 = Label(window, text = "* Shift must be a natural number;")
htuText4.grid(column=0, row=4, padx=10)
htuText5 = Label(window, text = "* All text fields must be filled.")
htuText5.grid(column=0, row=5, padx=10)

#Coleta do texto inserido no campo
textPhrase = Label(window, text="Enter the text:")
textPhrase.grid(column=0, row=6, padx=10, pady=10)
originalText = Entry(window, width=60)
originalText.grid(column=0, row=7, padx=10, pady=5)

#Coleta do número inserido no campo
textShift = Label(window, text="Enter the number of shifts:")
textShift.grid(column=0, row=8, padx=10, pady=10)
shift = Entry(window, width=10)
shift.grid(column=0, row=9, padx=10, pady=3)

#Criação de um frame para armazenar os dois botões
buttonFrame = Frame(window)
buttonFrame.grid(column=0, row=10, padx=10, pady=10)

buttonCipher = Button(buttonFrame, text="Cipher text", width=10, command=caesarCipher)
buttonCipher.pack(side="left")

buttonDecipher = Button(buttonFrame, text="Decipher text", width=10, command=caesarDecipher)
buttonDecipher.pack(side="right")

#Exibe o resultado do programa
resultText = Label(window, text="Cipher's result:")
resultText.grid(column=0, row=11, padx=10)
result = Label(window, text="Waiting...")
result.grid(column=0, row=12, padx=10)

emptySpace = Label(window, text="")
emptySpace.grid(column=0, row=13, padx=10, pady=10)

#Exibe a janela na tela
window.mainloop()
