from classes import Professor, Disciplina, Atividade

def criar_disciplina():
    nome = input("Nome da disciplina: ")
    professor_nome = input("Nome do professor: ")
    professor = Professor(professor_nome)
    disciplina = Disciplina(nome, professor)
    disciplinas.append(disciplina)
    print(f"Disciplina '{nome}' criada com sucesso!")

def adicionar_atividade():
    nome_disciplina = input("Nome da disciplina: ")
    data = input("Data da atividade: ")
    nome_atividade = input("Nome da atividade: ")

    for disciplina in disciplinas:
        if disciplina.nome == nome_disciplina:
            atividade = Atividade(nome_atividade, data)
            disciplina.adicionar_atividade(atividade)
            print(f"Atividade '{nome_atividade}' adicionada em {data} para a disciplina '{nome_disciplina}'.")
            return
    print(f"Disciplina '{nome_disciplina}' não encontrada.")

def listar_atividades():
    nome_disciplina = input("Nome da disciplina: ")

    for disciplina in disciplinas:
        if disciplina.nome == nome_disciplina:
            print(f"Atividades da disciplina '{nome_disciplina}':")
            disciplina.listar_atividades()
            return
    print(f"Disciplina '{nome_disciplina}' não encontrada.")

disciplinas = []

while True:
    print("\nMENU:")
    print("1. Criar Disciplina")
    print("2. Adicionar Atividade")
    print("3. Listar Atividades de Disciplina")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_disciplina()
    elif opcao == "2":
        adicionar_atividade()
    elif opcao == "3":
        listar_atividades()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
