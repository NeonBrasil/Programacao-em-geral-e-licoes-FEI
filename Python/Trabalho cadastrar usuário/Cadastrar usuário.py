import os
from tkinter import *
from tkinter import messagebox
from datetime import date

from random import randrange

window = Tk()
window.title("Criar conta")
window.geometry("600x500")


def Criar():
    id = []
    for i in range(5):
        id.append(str(randrange(9)))
    print(id)
    cpf = entrarCpf.get()

    nome = entrarNome.get()
    dataNascimento = entrarDataNascimento.get().replace('-', '/').split('/')
    endereco = entrarEndereco.get()
    
    profissao = entrarProfissao.get()

    idade = date.today().year - int(dataNascimento[-1])

    if os.path.isfile("./database/"+cpf+".txt"):

        messagebox.showinfo("Aviso", "Usuário ja cadastrado!")

    else:

        user = open("./database/"+cpf+".txt", "w")
        user.write(f'ID: {"".join(id)}\n')
        user.write(f"Nome: {nome}\n")
        user.write(f"Data de Nascimento: {dataNascimento}\n")
        user.write(f"Idade: {idade}\n")
        user.write(f"Endereço: {endereco}\n")
        user.write(f"Profissão: {profissao}\n")
        messagebox.showinfo(
            "Aviso", "Parábens, usuário cadastrado com sucesso!!!")
        user.close()


cpf = Label(window, text="CPF:", font=("Arial", 14))
cpf.place(relx=0.25, rely=0.15, anchor=CENTER)

name = Label(window, text="Nome:", font=("Arial", 14))
name.place(relx=0.25, rely=0.25, anchor=CENTER)

dataNascimento = Label(
    window, text="Data de Nascimento:\ndd/mm/aaaa", font=("Arial", 14))
dataNascimento.place(relx=0.25, rely=0.35, anchor=CENTER)

endereco = Label(window, text="Endereço:", font=("Arial", 14))
endereco.place(relx=0.25, rely=0.5, anchor=CENTER)

profissao = Label(window, text="Profissão:", font=("Arial", 14))
profissao.place(relx=0.25, rely=0.65, anchor=CENTER)


entrarCpf = Entry(window, width=15, font=("Arial", 14))
entrarCpf.place(relx=0.7, rely=0.15, anchor=CENTER)

entrarNome = Entry(window, width=15, font=("Arial", 14))
entrarNome.place(relx=0.7, rely=0.25, anchor=CENTER)

entrarDataNascimento = Entry(window, width=15, font=("Arial", 14))
entrarDataNascimento.place(relx=0.7, rely=0.35, anchor=CENTER)

entrarEndereco = Entry(window, width=15, font=("Arial", 14))
entrarEndereco.place(relx=0.7, rely=0.5, anchor=CENTER)

entrarProfissao = Entry(window, width=15, font=("Arial", 14))
entrarProfissao.place(relx=0.7, rely=0.65, anchor=CENTER)

btn = Button(window, text="Clique aqui para Cadastrar", command=Criar)

btn.place(relx=0.48, rely=0.8, anchor=CENTER)

window.mainloop()
