import random

contas = []

alertas_agricolas = [
    "Risco de erosão identificado na propriedade. - 30/05/2026",
    "Nível de umidade acima do ideal. - 29/05/2026",
    "Possível contaminação da água detectada. - 27/05/2026"
]

monitoramento_propriedade = [
    "Umidade do solo: 68%",
    "Risco de erosão: Baixo",
    "Saúde do solo: Em recuperação",
    "Cobertura vegetal: 72%"
]

recomendacoes_agricolas = [
    "Aplicar biofertilizantes para recuperação do solo.",
    "Utilizar irrigação inteligente para otimizar o consumo de água.",
    "Implementar policultivo para aumentar a resistência da produção.",
    "Utilizar hidroponia emergencial em áreas mais degradadas."
]

historico_monitoramento = []

def cadastrar(conta):
    contas.append(conta)
    print("Conta cadastrada com sucesso!")

def mostrar_lista(lista):
    if len(lista) == 0:
        print("Nenhuma informação disponível.")
    else:
        for item in lista:
            print(item)

def analisar_propriedade():
    resultado = random.randint(1, 5)

    if resultado == 1:
        return "Área em boas condições."
    elif resultado == 2:
        return "Necessita recuperação do solo."
    elif resultado == 3:
        return "Risco moderado de erosão."
    elif resultado == 4:
        return "Excesso de umidade detectado."
    else:
        return "Área afetada por enchente recente."

def adicionar_historico(registro):
    historico_monitoramento.append(registro)

opcao = -1

while opcao != 0:

    print("\n===== Plataforma Geo Rocket Agro =====")
    print("1 - Sobre a plataforma")
    print("2 - Cadastrar conta")
    print("3 - Ver alertas agrícolas")
    print("4 - Monitoramento da propriedade")
    print("5 - Recomendações agrícolas")
    print("6 - Analisar propriedade")
    print("7 - Histórico de análises")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:

        case 1:
            print("A plataforma Geo Rocket Agro auxilia produtores rurais na recuperação de áreas afetadas por enchentes através do uso de satélites, sensores agrícolas e inteligência artificial.")

        case 2:
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            conta = {
                "nome": nome,
                "email": email,
                "senha": senha
            }

            cadastrar(conta)

        case 3:
            print("\n=== Alertas Agrícolas ===")
            mostrar_lista(alertas_agricolas)

        case 4:
            print("\n=== Monitoramento da Propriedade ===")
            mostrar_lista(monitoramento_propriedade)

        case 5:
            print("\n=== Recomendações Agrícolas ===")
            mostrar_lista(recomendacoes_agricolas)

        case 6:
            propriedade = input("Digite o nome da propriedade: ")

            resultado = analisar_propriedade()

            print("\nResultado da análise:")
            print(propriedade, "-", resultado)

            registro = {
                "propriedade": propriedade,
                "resultado": resultado
            }

            adicionar_historico(registro)

        case 7:
            print("\n=== Histórico ===")

            if len(historico_monitoramento) == 0:
                print("Nenhuma análise realizada.")
            else:
                for item in historico_monitoramento:
                    print(item["propriedade"], "-", item["resultado"])

        case 0:
            print("Encerrando sistema...")

        case _:
            print("Opção inválida.")