from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from src.dao.matriculaDAO import DAOMatricula


class ViewMatricula:
    def __init__(self) -> None:
        pass
    # -------------------CORES -----------------

    def crudMatricula():
        # _______INICIANDO O APP_______________
        backgroundcolor = "#171c28"
        textcolor = "#7589aa"
        backgroudbox = "#1f2e47"
        backgroundaux = "#4362a8"
        foreground = "#ffffff"

        janela = Tk(screenName="CRUD")

        janela.title("CRUD Aluno")
        janela.geometry("1043x453")
        janela.configure(background="#12192b")
        janela.resizable(width=False, height=False)

        # ______________DIVIDINDO AS JANELAS ___________

        frameCima = Frame(janela, width=310, height=50,
                          background=backgroundaux, relief='flat')
        frameCima.grid(row=0, column=0)

        frameBaixo = Frame(janela, width=310, height=400,
                           background=backgroundcolor, relief='flat')
        frameBaixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

        frameDireita = Frame(janela, width=388, height=400,
                             background=backgroundcolor, relief='flat')
        frameDireita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

        # ___FUNCAO INSERIR __________________

        def inserir():
            aluno = eAluno.get()
            turma = eTurma.get()

            lista = [aluno, turma]
            if aluno == '':
                messagebox.showerror('Campo Nulo')
            else:
                DAOMatricula.inserirMatricula(lista)
                eAluno.delete(0, 'end')
                eTurma.delete(0, 'end')

            for widget in frameDireita.winfo_children():
                widget.destroy()
            mostrar()

        def atualizar():
            try:
                treev_dados = tree.focus()
                treev_dicionario = tree.item(treev_dados)
                tree_lista = treev_dicionario['values']

                valor = tree_lista[0]

                eAluno.delete(0, 'end')
                eTurma.delete(0, 'end')

                eAluno.insert(0, tree_lista[1])
                eTurma.insert(0, tree_lista[2])

                def update():
                    aluno = eAluno.get()
                    turma = eTurma.get()

                    lista = [valor, aluno, turma]
                    if aluno == '':
                        messagebox.showerror('Campo Nulo')
                    else:
                        DAOMatricula.updateMatricula(lista)
                        eAluno.delete(0, 'end')
                        eTurma.delete(0, 'end')

                    for widget in frameDireita.winfo_children():
                        widget.destroy()

                    mostrar()

                    # CONFIRMAR
                bConfirma = Button(frameBaixo, command=update, text='CONFIRMAR', anchor=NW, font=(
                    'rainyhearts 10'), bg=backgroudbox, fg=foreground, relief='raised')
                bConfirma.place(x=100, y=340)

            except TypeError as error:
                print("Failed", error)

        def deletar():
            nome = eAluno.get()
            DAOMatricula.deletMatricula(nome)
            mostrar()

        # __________________NOME CRUD_____________
        appName = Label(frameCima, text='CRUD MATRICULA', anchor=NW, font=(
            'rainyhearts 30'), bg=backgroundaux, fg=textcolor, relief='flat')
        appName.place(x=5, y=5)

        # _________________ ALUNO _____________

        lAuno = Label(frameBaixo, text='Aluno:', anchor=NW, font=(
            'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
        lAuno.place(x=15, y=10)

        eAluno = Entry(frameBaixo, justify='left',
                       relief='solid', width=45, bg=backgroudbox, fg=foreground)
        eAluno.place(x=15, y=40)

        # ______________Turma__________
        lTurma = Label(frameBaixo, text='Turma:', anchor=NW, font=(
            'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
        lTurma.place(x=15, y=70)

        eTurma = Entry(frameBaixo, justify='left',
                       relief='solid', width=45, bg=backgroudbox, fg=foreground)
        eTurma.place(x=15, y=100)

        # ______BOTAO INSERIR__________

        bInserir = Button(frameBaixo, command=inserir, text='Inserir', anchor=NW, font=(
            'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
        bInserir.place(x=30, y=300)

        # ______BOTAO UPDATE__________

        bAtualizar = Button(frameBaixo, command=atualizar, text='Atualizar', anchor=NW, font=(
            'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
        bAtualizar.place(x=100, y=300)

        # ______BOTAO DELETE__________

        bDelete = Button(frameBaixo, command=deletar, text='Delete', anchor=NW, font=(
            'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
        bDelete.place(x=190, y=300)

        # _____________TABELA _____________

        def mostrar():
            global tree
            lista = DAOMatricula.listarMatricula('')
            tabela_head = ['ID', 'Nome do Aluno',  'Nome da Turma']

            # criando a tabela
            tree = ttk.Treeview(frameDireita, selectmode="extended",
                                columns=tabela_head, show="headings")

            # vertical scrollbar
            vsb = ttk.Scrollbar(
                frameDireita, orient="vertical", command=tree.yview)

            # horizontal scrollbar
            hsb = ttk.Scrollbar(
                frameDireita, orient="horizontal", command=tree.xview)

            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            tree.grid(column=0, row=0, sticky='nsew')
            vsb.grid(column=1, row=0, sticky='ns')
            hsb.grid(column=0, row=1, sticky='ew')

            frameDireita.grid_rowconfigure(0, weight=12)

            hd = ["nw", "center", "center"]
            h = [110, 305, 305]
            n = 0

            for col in tabela_head:
                tree.heading(col, text=col.title(), anchor=CENTER)
                # adjust the column's width to the header string
                tree.column(col, width=h[n], anchor=hd[n])

                n += 1

            for item in lista:
                tree.insert('', 'end', values=item)

        mostrar()
        janela.mainloop()
