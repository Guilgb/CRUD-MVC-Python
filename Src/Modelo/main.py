from alunoDao import DAOAluno


def menu():
    while True:
        opcao = input(
            '1 - Adicionar /  2 - Remover  / 3 - Listar / 4 Sair\n')
        if (opcao == "1"):
            daoAluno = DAOAluno
            daoAluno.insertAluno('Teste Inserir')

        elif(opcao == "2"):
            daoAluno = DAOAluno
            daoAluno.deleteAluno('Teste Deletar')

        elif(opcao == "3"):
            daoAluno = DAOAluno
            daoAluno.listarAlunos('Teste Listar')

        elif(opcao == '4' or 'sair'):
            break


if __name__ == '__main__':
    menu()
1