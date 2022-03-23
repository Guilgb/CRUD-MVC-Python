from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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
    janela.geometry("600x300")
    janela.configure(background="#12192b")
    janela.resizable(width=False, height=False)

    # ______________DIVIDINDO AS JANELAS ___________

    frameBaixo = Frame(janela, width=600, height=300,
                       background=backgroundcolor, relief='flat')
    frameBaixo.grid(row=0, column=0)

    # ______ALUNO__________
    bInserir = Button(frameBaixo, width=20, height=20, text='CRUD ALUNO', anchor='center', font=(
        'rainyhearts 15'), bg=foreground, fg=textcolor, relief='raised')
    bInserir.place(x=30, y=180)

    # ______INSTRUTOR__________
    bInserir = Button(frameBaixo, width=20, height=40, text='CRUD INSTRUTOR', anchor='center', font=(
        'rainyhearts 15'), bg=foreground, fg=textcolor, relief='raised')
    bInserir.place(x=180, y=180)

    # ______TURMA__________
    bInserir = Button(frameBaixo, text='CRUD INSTRUTOR', anchor='center', font=(
        'rainyhearts 15'), bg=foreground, fg=textcolor, relief='raised')
    bInserir.place(x=380, y=180)

    janela.mainloop()


mainApp()
