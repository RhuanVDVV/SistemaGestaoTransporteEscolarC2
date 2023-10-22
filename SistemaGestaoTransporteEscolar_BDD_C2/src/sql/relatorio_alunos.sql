select a.CODIGO_ALUNO,
        a.NOME,
        a.HORARIO_AULA,
        a.TURMA,
        a.MATRICULA,      
        a.CPF AS CPF_RESPONSAVEL,
        r.NOME as NOME_RESPONSAVEL,
        r.LOGRADOURO,
        r.BAIRRO,
        r.CIDADE,
        e.CODIGO_ESCOLA,
        e.nome AS NOME_ESCOLA

from LABDATABASE.ALUNOS a
inner join LABDATABASE.RESPONSAVEIS r
on a.cpf = r.cpf
inner join LABDATABASE.ESCOLAS e
on a.codigo_escola = e.codigo_escola
order by a.nome