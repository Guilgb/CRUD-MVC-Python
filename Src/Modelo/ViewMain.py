from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from viewAluno import ViewAluno
from viewMatricula import ViewMatricula
from viewTurma import ViewTurma
from viewInstrutor import ViewInstrutor

# -------------------CORES -----------------
backgroundcolor = "#171c28"
textcolor = "#7589aa"
backgroudbox = "#1f2e47"
backgroundaux = "#4362a8"
foreground = "#ffffff"


def mainApp():
    # _______INICIANDO O APP_______________

    janela = Tk(screenName="CRUD")

    janela.title("CRUD Aluno")
    janela.geometry("700x300")
    janela.configure(background="#12192b")
    janela.resizable(width=False, height=False)

    # ______________DIVIDINDO AS JANELAS ___________

    frameBaixo = Frame(janela, width=700, height=300,
                       background=backgroundcolor, relief='flat')
    frameBaixo.grid(row=0, column=0)

    # ___________LABEL____________

    label = Label(frameBaixo, anchor='center', text='CRUD', font=(
        'rainyhearts 70'), bg=backgroundcolor, fg=textcolor)
    label.place(x=235, y=30)

    # ______ALUNO__________
    bInserir = Button(frameBaixo, command=ViewAluno.crudALuno, width=12, height=1, text='ALUNO', anchor='center', font=(
        'rainyhearts 15'), bg=foreground, fg=textcolor, relief='raised')
    bInserir.place(x=15, y=160)

    # ______INSTRUTOR__________
    bInserir = Button(frameBaixo, command=ViewInstrutor.crudInstrutor, width=15, height=1, text='INSTRUTOR', anchor='center', font=(
        'rainyhearts 15'), bg=foreground, fg=textcolor, relief='raised')
    bInserir.place(x=165, y=160)

    # ______TURMA__________
    bInserir = Button(frameBaixo, command=ViewTurma.crudTurma, width=15, height=1, text='TURMA', anchor='center', font=(
        'rainyhearts 15'), bg=foreground, fg=textcolor, relief='raised')
    bInserir.place(x=345, y=160)

    # ______MATRICILA__________
    bInserir = Button(frameBaixo, command=ViewMatricula.crudMatricula, width=15, height=1, text='MATRICULA', anchor='center', font=(
        'rainyhearts 15'), bg=foreground, fg=textcolor, relief='raised')
    bInserir.place(x=525, y=160)

    janela.mainloop()


mainApp()
