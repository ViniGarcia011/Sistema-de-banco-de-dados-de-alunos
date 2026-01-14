alunos = []

def adicionar_aluno():
    nome = input('Digite o Nome do Aluno:')
    idade = int(input('Digite a idade do Aluno:'))
    while True:
        nota = float(input('Digite a nota do Aluno:'))
        if nota >= 0 and nota <= 10:
            break
        else:
            print("Nota inválida, a nota deve ser de 0 a 10.")

    dados = {
        'nome' : nome, 
        'idade' : idade,
        'nota' : nota
    }
    alunos.append(dados)

def listar_alunos():
    if len(alunos) == 0:
        print(f"Sem alunos cadastrados\n{'='* 50}.")
        return
    for aluno in alunos:
        print(f'Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota:{aluno['nota']}\n{'='*30}')



def buscar_aluno(nome_do_aluno):
    if len(alunos) == 0:
        print('Sem alunos encontrados.')
    for aluno in alunos:
        if aluno['nome'].lower() == nome_do_aluno.lower():
            print(f'{aluno['nome']}\n{aluno['idade']}\n{aluno['nota']}')
            break
    else:
        print('Esse aluno não foi encontrado.')

def deletar_aluno(nome_do_aluno):
    if len(alunos) == 0:
        print('Sem alunos encontrados.')
    for aluno in alunos:
        if aluno['nome'].lower() == nome_do_aluno.lower():
            alunos.remove(aluno)
            break
    else:
        print('Esse aluno não foi encontrado.')

def media_de_notas():
    if len(alunos) == 0:
        print("Sem alunos cadastrados")       
        return
    soma = 0
    for aluno in alunos:
        soma += aluno['nota']
    media = soma / len(alunos)
    print(f'A média das notas do alunos são {media:.2f}\n{'='*50}')
        
while True:
    opcao = int(input('\nOque deseja fazaer?\n1.Adicionar Aluno\n2.Listar Todos Alunos\n3.Buscar Aluno Pelo Nome\n4.Remover Aluno\n5.Mostrar Média Geral das Notas\n6.Sair\n:'))
    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            nome_aluno = input('Qual aluno deseja buscar?:')
            buscar_aluno(nome_aluno)
        case 4:
            nome_aluno = input('Qual aluno deseja remover?:')
            deletar_aluno(nome_aluno)
            print(f'Aluno {nome_aluno} removido')
        case 5:
            media_de_notas()
        case 6:
            break

