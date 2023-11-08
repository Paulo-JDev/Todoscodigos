import tkinter as tk
from tkinter import messagebox


def submit():
    nome = entry_nome.get()
    idade = entry_idade.get()

    if nome and idade:
        mensagem = "Nome: {}\nIdade: {}".format(nome, idade)
        messagebox.showinfo("Informações", mensagem)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


# Cria a janela principal
janela = tk.Tk()
janela.title("Formulário")

# Cria os rótulos
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()

label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()

# Cria as caixas de entrada
entry_nome = tk.Entry(janela)
entry_nome.pack()

entry_idade = tk.Entry(janela)
entry_idade.pack()

# Cria o botão de envio
botao_enviar = tk.Button(janela, text="Enviar", command=submit)
botao_enviar.pack()

# Inicia o loop da interface gráfica
janela.mainloop()
