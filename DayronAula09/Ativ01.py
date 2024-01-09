from tkinter import *

caixinha = Tk()
caixinha.title("Atividade 1 Tk")
caixinha.geometry("300x300")

def soma():
    nota1 = int(nota1_input.get())
    nota2 = int(nota2_input.get())
    nome = usuario_input.get()

    resultado.configure(text=f"{nome} a soma das suas notas é: {nota1+nota2}")

usuario_label = Label(text = "Digite seu nome: ").pack()

usuario_input = Entry()
usuario_input.pack()

nota1_label = Label(text = "Digite a Primeira Nota", bg="red", fg="white").pack()

nota1_input = Entry()
nota1_input.pack()

nota2_label = Label(text = "Digite a Segunda Nota", bg="red", fg="white").pack()

nota2_input = Entry()
nota2_input.pack()

botao_enviar = Button(caixinha, text="Enviar", command=soma)
botao_enviar.pack()

resultado = Label(text = "").pack()

caixinha.mainloop()
