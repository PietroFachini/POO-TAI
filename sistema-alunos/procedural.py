def apresentar(nome, idade):
    return f"Olá, meu nome é {nome} e tenho {idade} anos."

def maior_de_idade(idade):
    return idade >= 18 #retorna um valor booleano

alunos = [
    {"nome": "João", "idade": 17},
    {"nome": "Maria", "idade": 16},
    {"nome": "Carlos", "idade": 18},
]

for aluno in alunos:
    print(apresentar(aluno["nome"], aluno["idade"]))

    if maior_de_idade(aluno["idade"]): # se true com os valores inseridos, retorna conforme
     print(f"{aluno['nome']} é maior de idade.")