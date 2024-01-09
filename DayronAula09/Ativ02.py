from tkinter import *

janela = Tk()
janela.title("Media das Notas")
janela.geometry("400x500")

def media():
    valor1 = float(valor1_input.get())
    valor2 = float(valor2_input.get())
    valor3 = float(valor3_input.get())
    
    soma = float(valor1+valor2+valor3)
    media = float(soma/3)
 if media >= 7 and media < 10:
        resultado.configure(text=f"Você foi aprovado com a média {media:.2f}")
    elif media < 7 and media >= 0:
        resultado.configure(text=f"Você foi reprovado com a média {media:.2f}")
    elif media == 10:
        resultado.configure(text=f"Você foi aprovado com distinção com a média {media:.2f}")
    else:
        resultado.configure(text=f"Média {media:.2f} é inválida")


valor1_label = Label(text = "Digite o Primeiro Valor: ", bg="red", fg="white").pack()

valor1_input = Entry()
valor1_input.pack()

valor2_label = Label(text = "Digite o Segundo Valor: ", bg="red", fg="white").pack()

valor2_input = Entry()
valor2_input.pack()

valor3_label = Label(text = "Digite o Terceiro Valor: ", bg="red", fg="white").pack()

valor3_input = Entry()
valor3_input.pack()

botao_enviar = Button(janela, text="Calcular", command=media)
botao_enviar.pack()

resultado = Label(text="").pack()

janela.mainloop()