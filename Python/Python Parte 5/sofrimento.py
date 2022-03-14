"""Tem q fazer a parada de achar a palavra no arquivo .TXT 
e arrumar a janela que esta vindo mto pequena"""


from tkinter import *
from tkinter import scrolledtext

tela = Tk()
tela.title('Buscador de palavras')
tela.geometry('1280x720')


def quantidade():

    frequenciaEpica.delete(0, END)
    txt.delete(END, END)
    frequencia = 0

    palavra = escrever.get()

    Mongi = []
    arquivo = open('chat.txt', 'r')
    for i in arquivo.readlines():
        Mongi.append(i.strip().split())
    arquivo.close()

    for i in range(len(Mongi)):

        for k in range(len(Mongi[i])):
            if palavra.lower() in Mongi[i][k].lower():
                Mongi[i][-1] = Mongi[i][-1]+'\n\n'
                
                txt.insert(1.0, ' '.join(Mongi[i]))
                frequencia += 1

    frequenciaEpica.insert(0, frequencia)


dor = Label(tela, text='Palavra Suspeita:', font=('Arial', 14))
dor.place(relx=0.01, rely=0.05, anchor=NW)

# Lugar pra escrever :)

escrever = Entry(tela, width=15, font=('Arial', 14))

escrever.place(relx=0.13, rely=0.05, anchor=NW)

# Botão brabo
btn = Button(tela, text='Clique para pesquisar!', command=quantidade)

btn.place(relx=0.27, rely=0.08, anchor=NW)


label1 = Label(tela, text='Frequência:', font=('Arial', 14))

label1.place(relx=0.020, rely=0.1, anchor=NW)

# Caixa de entrada parte 2 :o

frequenciaEpica = Entry(tela, width=15, font=('Arial', 14))
frequenciaEpica.place(relx=0.13, rely=0.1, anchor=NW)


# Ocorrências

label1 = Label(tela, text='Ocorrências:', font=('Arial', 14))

label1.place(relx=0.020, rely=0.2, anchor=NW)


txt = scrolledtext.ScrolledText(tela, width=150, height=31)


txt.place(relx=0.5, rely=0.62, anchor=CENTER)

tela.mainloop()
