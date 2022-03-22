from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from alunoDao import DAOAluno


# -------------------CORES -----------------
backgroundcolor = "#171c28"
textcolor = "#7589aa"
backgroudbox = "#1f2e47"
backgroundaux = "#4362a8"
foreground = "#ffffff"

# _______INICIANDO O APP_______________

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
    nome = eNome.get()
    telefone = eTelefone.get()
    cidade = eCidade.get()
    estado = eEstado.get()
    escolaridae = eEscolaridade.get()

    lista = [nome, telefone, cidade, estado, escolaridae]
    if nome == '':
        messagebox.showerror('Campo Nulo')
    else:
        DAOAluno.insertAluno(lista)
        eNome.delete(0, 'end')
        eTelefone.delete(0, 'end')
        eCidade.delete(0, 'end')
        eEstado.delete(0, 'end')
        eEscolaridade.delete(0, 'end')

    for widget in frameDireita.winfo_children():
        widget.destroy()
    mostrar()


def atualizar():
    pass


def deletar():
    nome = eNome.get()
    DAOAluno.deleteAluno(nome)
    mostrar()


# __________________LABEL CIMA _____________
appName = Label(frameCima, text='CRUD', anchor=NW, font=(
    'rainyhearts 30'), bg=backgroundaux, fg=textcolor, relief='flat')
appName.place(x=100, y=5)

# __________________LABEL CIMA _____________

lNome = Label(frameBaixo, text='Nome:', anchor=NW, font=(
    'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
lNome.place(x=15, y=10)

eNome = Entry(frameBaixo, justify='left',
              relief='solid', width=45, bg=backgroudbox, fg=foreground)
eNome.place(x=15, y=40)


# ______________TELEFONE__________
lTelefone = Label(frameBaixo, text='Telefone:', anchor=NW, font=(
    'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
lTelefone.place(x=15, y=70)

eTelefone = Entry(frameBaixo, justify='left',
                  relief='solid', width=45, bg=backgroudbox, fg=foreground)
eTelefone.place(x=15, y=100)


# ______________ESTADO__________
lEstado = Label(frameBaixo, text='Estado:', anchor=NW, font=(
    'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
lEstado.place(x=15, y=130)

eEstado = Entry(frameBaixo, justify='left',
                relief='solid', width=45, bg=backgroudbox, fg=foreground)
eEstado.place(x=15, y=160)

# ______________CIDADE__________
lCidade = Label(frameBaixo, text='Cidade:', anchor=NW, font=(
    'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
lCidade.place(x=15, y=190)

eCidade = Entry(frameBaixo, justify='left',
                relief='solid', width=45, bg=backgroudbox, fg=foreground)
eCidade.place(x=15, y=210)


# ______________ESCOLARIDADE__________
lEscolaridade = Label(frameBaixo, text='Escolaridade:', anchor=NW, font=(
    'rainyhearts 15'), bg=backgroundcolor, fg=textcolor, relief='flat')
lEscolaridade.place(x=15, y=240)

eEscolaridade = Entry(frameBaixo, justify='left',
                      relief='solid', width=45, bg=backgroudbox, fg=foreground)
eEscolaridade.place(x=15, y=270)


# ______BOTAO INSERIR__________

bInserir = Button(frameBaixo, command=inserir, text='Inserir', anchor=NW, font=(
    'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
bInserir.place(x=30, y=300)

# ______BOTAO UPDATE__________

bAtualizar = Button(frameBaixo, text='Atualizar', anchor=NW, font=(
    'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
bAtualizar.place(x=100, y=300)


# ______BOTAO DELETE__________

bDelete = Button(frameBaixo, command=deletar, text='Delete', anchor=NW, font=(
    'rainyhearts 12'), bg=backgroudbox, fg=foreground, relief='raised')
bDelete.place(x=190, y=300)


# _____________TABELA _____________


def mostrar():
    lista = DAOAluno.listarAlunos('')
    tabela_head = ['ID', 'Nome',  'Telefone', 'Cidade', 'Escolaridade']

    # criando a tabela
    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center"]
    h = [50, 200, 160, 135, 170]
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
