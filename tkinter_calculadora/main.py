from tkinter import *
from tkinter import ttk

preto = "#1e1f1e"
branco = "#feffff"
azulEsc = "#38576b"
cinza = "#ECEFF1"
laranja = "#FFAB40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=preto)

frame_tela = Frame(janela, width=235, height=50, bg=azulEsc)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ""
valor_texto = StringVar()


def entrada_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=azulEsc, fg=branco)
app_label.place(x=0, y=0)

bt1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt1.place(x=0, y=0)
bt2 = Button(frame_corpo, command = lambda: entrada_valores("%"), text="%", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt2.place(x=118, y=0)
bt3 = Button(frame_corpo, command = lambda: entrada_valores("/"), text="/", width=5, height=2, bg=laranja, fg=branco, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt3.place(x=177, y=0)

bt4 = Button(frame_corpo, command = lambda: entrada_valores("7"), text="7", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt4.place(x=0, y=52)
bt5 = Button(frame_corpo, command = lambda: entrada_valores("8"), text="8", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt5.place(x=59, y=52)
bt6 = Button(frame_corpo, command = lambda: entrada_valores("9"), text="9", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt6.place(x=118, y=52)
bt7 = Button(frame_corpo, command = lambda: entrada_valores("*"), text="*", width=5, height=2, bg=laranja, fg=branco, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt7.place(x=177, y=52)

bt8 = Button(frame_corpo, command = lambda: entrada_valores("4"), text="4", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt8.place(x=0, y=104)
bt9 = Button(frame_corpo, command = lambda: entrada_valores("5"), text="5", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt9.place(x=59, y=104)
bt10 = Button(frame_corpo, command = lambda: entrada_valores("6"), text="6", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt10.place(x=118, y=104)
bt11 = Button(frame_corpo, command = lambda: entrada_valores("-"), text="-", width=5, height=2, bg=laranja, fg=branco, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bot11.place(x=177, y=104)

bt12 = Button(frame_corpo, command = lambda: entrada_valores("1"), text="1", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt12.place(x=0, y=156)
bt13 = Button(frame_corpo, command = lambda: entrada_valores("2"), text="2", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt13.place(x=59, y=156)
bt14 = Button(frame_corpo, command = lambda: entrada_valores("3"), text="3", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt14.place(x=118, y=156)
bt15 = Button(frame_corpo, command = lambda: entrada_valores("+"), text="+", width=5, height=2, bg=laranja, fg=branco, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt15.place(x=177, y=156)

bt16 = Button(frame_corpo, command = lambda: entrada_valores("0"), text="0", width=11, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt16.place(x=0, y=208)
bt17 = Button(frame_corpo, command = lambda: entrada_valores("."), text=".", width=5, height=2, bg=cinza, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt17.place(x=118, y=208)
bt18 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=laranja, fg=branco, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
bt18.place(x=177, y=208)

janela.mainloop()
