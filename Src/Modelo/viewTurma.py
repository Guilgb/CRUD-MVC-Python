from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from turmaDAO import DAOTurma


# -------------------CORES -----------------
backgroundcolor = "#171c28"
textcolor = "#7589aa"
backgroudbox = "#1f2e47"
backgroundaux = "#4362a8"
foreground = "#ffffff"


def crudTurma():
    # _______INICIANDO O APP_______________

    janela = Tk(screenName="CRUD")

    janela.title("CRUD TURMA")
    janela.geometry("1185x475")
    janela.configure(background="#12192b")
    janela.resizable(width=False, height=False)

    # ______________DIVIDINDO AS JANELAS ___________

    frameCima = Frame(janela, width=310, height=50,
                      background=backgroundaux, relief='flat')
    frameCima.grid(row=0, column=0)

    frameBaixo = Frame(janela, width=310, height=420,
                       background=backgroundcolor, relief='flat')
    frameBaixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

    frameDireita = Frame(janela, width=588, height=420,
                         background=backgroundcolor, relief='flat')
    frameDireita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

    # ___FUNCAO INSERIR __________________

    def inserir():
        nome = eNome.get()
        horai = eHoraInicio.get()
        horaf = eHoraFim.get()
        diai = eDiaaInicio.get()
        diaf = eDiaFim.get()
        area = eArea.get()
        curso = eCurso.get()
        ch = eCursoCh.get()
        filial = eFilial.get()
        localidade = eLocalidade.get()
        instrutor = eInstrutor.get()

        lista = [nome, horai, horaf, diai, diaf,
                 area, curso, ch, filial, localidade, instrutor]
        if nome == '':
            messagebox.showerror('Campo Nulo')
        else:
            DAOTurma.inserirTurma(lista)
            eNome.delete(0, 'end')
            eHoraInicio.delete(0, 'end')
            eHoraFim.delete(0, 'end')
            eDiaaInicio.delete(0, 'end')
            eDiaFim.delete(0, 'end')
            eArea.delete(0, 'end')
            eCurso.delete(0, 'end')
            eCursoCh.delete(0, 'end')
            eFilial.delete(0, 'end')
            eLocalidade.delete(0, 'end')
            eInstrutor.delete(0, 'end')

        for widget in frameDireita.winfo_children():
            widget.destroy()
        mostrar()

    def atualizar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor = tree_lista[0]

            eNome.delete(0, 'end')
            eHoraInicio.delete(0, 'end')
            eHoraFim.delete(0, 'end')
            eDiaaInicio.delete(0, 'end')
            eDiaFim.delete(0, 'end')
            # eArea.delete(0, 'end')
            eCurso.delete(0, 'end')
            eCursoCh.delete(0, 'end')
            eFilial.delete(0, 'end')
            eLocalidade.delete(0, 'end')
            eInstrutor.delete(0, 'end')

            eNome.insert(0, tree_lista[1])
            eHoraInicio.insert(0, tree_lista[2])
            eHoraFim.insert(0, tree_lista[3])
            eDiaaInicio.insert(0, tree_lista[4])
            eDiaFim.insert(0, tree_lista[5])
            # eArea.insert(0, tree_lista[6])
            eCurso.insert(0, tree_lista[6])
            eCursoCh.insert(0, tree_lista[7])
            eFilial.insert(0, tree_lista[8])
            eLocalidade.insert(0, tree_lista[9])
            eInstrutor.insert(0, tree_lista[10])

            def update():
                nome = eNome.get()
                horai = eHoraInicio.get()
                horaf = eHoraFim.get()
                diai = eDiaaInicio.get()
                diaf = eDiaFim.get()
                # area = eArea.get()
                curso = eCurso.get()
                ch = eCursoCh.get()
                filial = eFilial.get()
                localidade = eLocalidade.get()
                instrutor = eInstrutor.get()

                lista = [valor, nome, horai, horaf, diai, diaf,
                         curso, ch, filial, localidade, instrutor]
                if nome == '':
                    messagebox.showerror('Campo Nulo')
                else:
                    DAOTurma.updateTurma(lista)
                    eNome.delete(0, 'end')
                    eHoraInicio.delete(0, 'end')
                    eHoraFim.delete(0, 'end')
                    eDiaaInicio.delete(0, 'end')
                    eDiaFim.delete(0, 'end')
                    # eArea.delete(0, 'end')
                    eCurso.delete(0, 'end')
                    eCursoCh.delete(0, 'end')
                    eFilial.delete(0, 'end')
                    eLocalidade.delete(0, 'end')
                    eInstrutor.delete(0, 'end')

                for widget in frameDireita.winfo_children():
                    widget.destroy()

                mostrar()

                # CONFIRMAR
            bConfirma = Button(frameBaixo, command=update, text='CONFIRMAR', anchor=NW, font=(
                'rainyhearts 10'), bg=backgroudbox, fg=foreground, relief='raised')
            bConfirma.place(x=230, y=397)

        except TypeError as error:
            print("Failed", error)

    def deletar():
        nome = eNome.get()
        DAOTurma.deleteTurma(nome)
        mostrar()

    # __________________LABEL CIMA _____________
    appName = Label(frameCima, text='CRUD TURMA', anchor=NW, font=(
        'rainyhearts 30'), bg=backgroundaux, fg=textcolor, relief='flat')
    appName.place(x=35, y=5)

    # __________________LABEL CIMA _____________

    lNome = Label(frameBaixo, text='Nome da turma:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lNome.place(x=15, y=10)

    eNome = Entry(frameBaixo, justify='left',
                  relief='solid', width=45, bg=backgroudbox, fg=foreground)
    eNome.place(x=15, y=40)

    # ______________HORA INCIO__________
    lHoraInicio = Label(frameBaixo, text='Hora Incio:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lHoraInicio.place(x=15, y=70)

    eHoraInicio = Entry(frameBaixo, justify='left',
                        relief='solid', width=15, bg=backgroudbox, fg=foreground)
    eHoraInicio.place(x=15, y=100)

    # ______________HORA FIM__________
    lHoraFim = Label(frameBaixo, text='Hora Fim:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lHoraFim.place(x=150, y=70)

    eHoraFim = Entry(frameBaixo, justify='left',
                     relief='solid', width=15, bg=backgroudbox, fg=foreground)
    eHoraFim.place(x=150, y=100)

    # ______________DIA INCIO__________
    lDiaInicio = Label(frameBaixo, text='Dia Incio:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lDiaInicio.place(x=15, y=130)

    eDiaaInicio = Entry(frameBaixo, justify='left',
                        relief='solid', width=15, bg=backgroudbox, fg=foreground)
    eDiaaInicio.place(x=15, y=160)

    # ______________DIA FIM__________
    lDiaFim = Label(frameBaixo, text='Dia Fim:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lDiaFim.place(x=150, y=130)

    eDiaFim = Entry(frameBaixo, justify='left',
                    relief='solid', width=15, bg=backgroudbox, fg=foreground)
    eDiaFim.place(x=150, y=160)

    # ______________AREA__________
    lArea = Label(frameBaixo, text='Area:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lArea.place(x=15, y=190)

    eArea = Entry(frameBaixo, justify='left',
                  relief='solid', width=37, bg=backgroudbox, fg=foreground)
    eArea.place(x=60, y=193)

    # ______________CURSO__________
    lCurso = Label(frameBaixo, text='Curso:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lCurso.place(x=15, y=220)

    eCurso = Entry(frameBaixo, justify='left',
                   relief='solid', width=15, bg=backgroudbox, fg=foreground)
    eCurso.place(x=15, y=250)

    # ______________CH__________
    lCursoCh = Label(frameBaixo, text='CH:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lCursoCh.place(x=150, y=220)

    eCursoCh = Entry(frameBaixo, justify='left',
                     relief='solid', width=15, bg=backgroudbox, fg=foreground)
    eCursoCh.place(x=150, y=250)

    # ______________Filail__________
    lFilial = Label(frameBaixo, text='Filial:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lFilial.place(x=15, y=280)

    eFilial = Entry(frameBaixo, justify='left',
                    relief='solid', width=15, bg=backgroudbox, fg=foreground)
    eFilial.place(x=15, y=310)

    # ______________CH__________
    lLocalidade = Label(frameBaixo, text='Localidade:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lLocalidade.place(x=150, y=280)

    eLocalidade = Entry(frameBaixo, justify='left',
                        relief='solid', width=15, bg=backgroudbox, fg=foreground)
    eLocalidade.place(x=150, y=310)

    # ______________INSTRUTOR__________
    lInstrutor = Label(frameBaixo, text='Instrutor:', anchor=NW, font=(
        'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
    lInstrutor.place(x=15, y=340)

    eInstrutor = Entry(frameBaixo, justify='left',
                       relief='solid', width=45, bg=backgroudbox, fg=foreground)
    eInstrutor.place(x=15, y=370)

    # ______BOTAO INSERIR__________

    bInserir = Button(frameBaixo, command=inserir, text='Inserir', anchor=NW, font=(
        'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
    bInserir.place(x=10, y=395)

    # ______BOTAO UPDATE__________

    bAtualizar = Button(frameBaixo, command=atualizar, text='Atualizar', anchor=NW, font=(
        'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
    bAtualizar.place(x=80, y=395)

    # ______BOTAO DELETE__________

    bDelete = Button(frameBaixo, command=deletar, text='Delete', anchor=NW, font=(
        'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
    bDelete.place(x=170, y=395)

    # _____________TABELA _____________

    def mostrar():
        global tree
        lista = DAOTurma.listarTurma('')
        tabela_head = ['ID', 'Turma',  'Hora Incio', 'Hora Fim',
                       'Dia Inicio', 'Dia Fim', 'Curso', 'CH', 'Filial',
                       'Localidade', 'Instrutor']

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

        hd = ["nw", "nw", "nw", "center",
              "center", "center", "nw", "nw", 'nw', 'nw', 'nw']
        h = [30, 50, 70, 70, 70, 70, 180, 70, 105, 70, 70]
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


crudTurma()
