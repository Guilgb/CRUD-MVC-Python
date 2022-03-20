class DAOMatricula:
    def __init__(self) -> None:
        pass

    def inserirMatricula(self):
        aluno = input('Digite o nome do aluno a cadastrar: ')
        turma = input('Digite o id da turma na qual deseja cadastrar: ')

        cadastroMatricula = input(
            'Deseja realmente cadastrar sua matricula (y/n): ')
        if(cadastroMatricula == 'y'):
            novaMatricula = Matricula(aluno, turma)

        # CONEXÃO COM O BANCO
        con = Conection.getConection("")
        cursor = con.cursor()

        # SQL BUSCA ALUNO
        def idAluno():
            sqlAluno = "SELECT idAluno FROM Aluno where nomeAluno=%s"
            valueAluno = (novaMatricula.aluno)
            cursor.execute(sqlAluno, valueAluno)

            resultAluno = cursor.fetchone()
            for reAluno in resultAluno:
                return reAluno

        # SQL BUSCA TURMA
        def idTurma():
            sqlTurma = "SELECT idTurma FROM Aluno where idTurma=%s"
            valueTurma = (novaMatricula.turma)
            cursor.execute(sqlTurma, valueTurma)

            resultTurma = cursor.fetchone()
            for reTurma in resultTurma:
                return reTurma

        # CRIA MATRICULA
        sqlMatricula = "INSERT INTO Matricula(idAluno, idTurma) values(%s, %s)"
        valueMatricula = (idAluno, idTurma)
        cursor.execute(sqlMatricula, valueMatricula)
