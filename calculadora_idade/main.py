from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date


def calcular():
    inicio = cal1.get()
    fim = cal2.get()
    dia1, mes1, ano1 = [ int(f) for f in inicio.split("/")]
    data_inicio = date(ano1, mes1, dia1)
    dia2, mes2, ano2 = [ int(f) for f in fim.split("/")]
    data_nascimento = date(ano2, mes2, dia2)
    anos = relativedelta(data_inicio, data_nascimento).years
    meses = relativedelta(data_inicio, data_nascimento).months
    dias = relativedelta(data_inicio, data_nascimento).days
    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias


janela = Tk()
janela.title("Calculadora de idade")
janela.geometry("310x400")

cinza = "#3b3b3b"
preto = "#333333"
branco = "#ffffff"
laranja = "#fcc058"

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=preto)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=cinza)
frame_baixo.grid(row=1, column=0)

l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief=FLAT, anchor=CENTER, font=("Ivy 15 bold"), bg=preto, fg=branco)
l_calculadora.place(x=0, y=30)
l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief=FLAT, anchor=CENTER, font=("Arial 35 bold"), bg=preto, fg=laranja)
l_idade.place(x=0, y=70)

l_data_inicial = Label(frame_baixo, text="Data inicial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=("Ivy 11"), bg=cinza, fg=branco)
l_data_inicial.place(x=40, y=30)
cal1 = DateEntry(frame_baixo, Widget=13, bg="darkblue", fg=branco, borderwidth=2, date_pattern="dd/mm/y", y=2022)
cal1.place(x=180, y=30)

l_data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=("Ivy 11"), bg=cinza, fg=branco)
l_data_nascimento.place(x=40, y=70)
cal2 = DateEntry(frame_baixo, Widget=13, bg="darkblue", fg=branco, borderwidth=2, date_pattern="dd/mm/y", y=2022)
cal2.place(x=180, y=70)

l_app_anos = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivy 25 bold"), bg=cinza, fg=branco)
l_app_anos.place(x=60, y=135)
l_app_nome = Label(frame_baixo, text="Anos", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivy 11 bold"), bg=cinza, fg=branco)
l_app_nome.place(x=58, y=175)


l_app_meses = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivy 25 bold"), bg=cinza, fg=branco)
l_app_meses.place(x=140, y=135)
l_appmeses = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivy 11 bold"), bg=cinza, fg=branco)
l_appmeses.place(x=135, y=175)

l_app_dias = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivy 25 bold"), bg=cinza, fg=branco)
l_app_dias.place(x=220, y=135)
l_appdias = Label(frame_baixo, text="Dias", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=("Ivy 11 bold"), bg=cinza, fg=branco)
l_appdias.place(x=220, y=175)

l_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=20, height=1, relief=RAISED, overrelief=RIDGE, font=("Ivy 10 bold"), bg=cinza, fg=branco)
l_calcular.place(x=70, y=225)

janela.mainloop()
