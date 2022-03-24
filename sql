create database crud;

use crud;

create table Telefones(
	idTelefone int auto_increment primary key,
    numeroTelefone char(11) not null
);

create table Estado(
	idEstado int auto_increment primary key,
    nomeEstado varchar(40) not null
);

create table Cidades(
	idCidade int auto_increment primary key,
    nomeCidade varchar(40) not null,
    idEstado int not null,
    constraint fk_Cidade_estado foreign key(idEstado) references Estado(idEstado) on delete cascade
);

create table Escolaridade(
	idEscolaridade int auto_increment primary key,
    nomeEscolaridade varchar(40) not null
);

create table Aluno(
	idAluno int auto_increment primary key,
    nomeAluno varchar(40) not null,
    idTelefone int not null,
    idCidade int not null,
    idEscolaridade int not null,
    constraint fk_telefone_aluno foreign key(idTelefone) references Telefones(idTelefone) on delete cascade,
    constraint fk_cidade_aluno foreign key(idCidade) references Cidades(idCidade) on delete cascade,
    constraint fk_escolaridade_aluno foreign key(idEscolaridade) references Escolaridade(idEscolaridade) on delete cascade
);

create table Instrutor(
	idInstrutor int auto_increment primary key,
    nomeInstrutor varchar(40) not null,
    formacao varchar(40) not null,
	idTelefone int not null,
    idCidade int not null,
    constraint fk_telefone_instrutor foreign key(idTelefone) references Telefones(idTelefone) on delete cascade,
    constraint fk_cidade_instrutor foreign key(idCidade) references Cidades(idCidade) on delete cascade
);

create table Area(
	idArea int auto_increment primary key,
    nomeArea varchar(40) not null
);

create table Curso(
	idCurso int auto_increment primary key,
	nomeCurso varchar(40) not null,
    chCurso varchar(40) not null,
    idArea int not null,
    constraint fk_area_curso foreign key(idArea) references Area(idArea) on delete cascade
);

create table Filial(
	idFilial int auto_increment primary key,
    nomeFilial varchar(40) not null,
    localidadeFilial varchar(40) not null
);

create table Turma(
	idTurma int auto_increment primary key,
    nomeTurma varchar(40) not null,
    horaInicio time not null,
    horaFim time not null,
    diaInicio date not null,
    diaFim date not null,
    idCurso int not null,
    idFilial int not null,
    idInstrutor int not null,
    constraint fk_curso_turma foreign key(idCurso) references Curso(idCurso) on delete cascade,
    constraint fk_filial_turma foreign key(idFilial) references Filial(idFilial) on delete cascade,
    constraint fk_insrutor_turma foreign key(idInstrutor) references Instrutor(idInstrutor) on delete cascade
);

create table Matricula(
	idMatricula int auto_increment primary key,
    idAluno int not null,
    idTurma int not null,
    constraint fk_aluno_matricula foreign key (idAluno) references Aluno(idAluno) on delete cascade,
    constraint fk_turma_matricula foreign key (idTurma) references Turma(idTurma) on delete cascade
);
insert into Area(nomeArea) value('tecnologia');
insert into Curso(nomeCurso, chCurso, idArea) values('Engenharia de Software', 'não sei o que é isso', 1);
insert into Filial(nomeFilial, localidadeFilial) values('IFCE', 'Iguatu');
insert into Turma(nomeTurma, horaInicio, horaFim, diaInicio, diaFim, idCurso, idFilial, idInstrutor) values('S1', '17:00:001', '22:20:00', 27/01/2020, 27/04/2020, 1, 1, 1);
select t.idTurma, t.nomeTurma, t.horaInicio, t.horaFim, t.diaInicio, t.diaFim, c.nomeCurso, c.chCurso, f.nomeFilial, f.localidadeFilial, i.nomeInstrutor from Turma t inner join Curso c on(t.idCurso = c.idCurso) inner join Filial f on(t.idFilial = f.idFilial) inner join Instrutor i on(t.idInstrutor = i.idInstrutor);
select i.idInstrutor, i.nomeInstrutor, i.formacao, t.numeroTelefone, c.nomeCidade from Instrutor i inner join Telefones t on(i.idTelefone = t.idTelefone) inner join Cidades c on(i.idCidade = c.idCidade);