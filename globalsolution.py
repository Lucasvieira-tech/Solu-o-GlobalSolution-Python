import random

contas = []

alertas_agricolas = [
    "Risco de erosão identificado na propriedade.",
    "Nível de umidade acima do ideal.",
    "Possível contaminação da água detectada."
]

historico_monitoramento = []

tecnologias = (
    "Satélites",
    "Sensores Agrícolas",
    "Inteligência Artificial",
    "Dashboard Web",
    "Aplicativo Mobile"
)

#FUNÇÕES

def cadastrar(conta):
    contas.append(conta)
    print("Conta cadastrada com sucesso!")


def mostrar_lista(lista):

    if len(lista) == 0:
        print("Nenhuma informação disponível.")

    else:
        for item in lista:
            print(item)


def mostrar_tecnologias():

    print("\n=== Tecnologias Utilizadas ===")

    for item in tecnologias:
        print("-", item)


def sensor_agricola():

    umidade = random.randint(40, 100)
    temperatura = random.randint(15, 35)
    erosao = random.randint(0, 100)

    print("\n=== Dados dos Sensores ===")
    print("Umidade:", umidade, "%")
    print("Temperatura:", temperatura, "°C")
    print("Risco de erosão:", erosao, "%")


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


def recomendacao_personalizada(degradacao):

    if degradacao <= 3:
        return "Policultivo"

    elif degradacao <= 6:
        return "Irrigação Inteligente + Biofertilizantes"

    else:
        return "Hidroponia Emergencial"


def calcular_recuperacao(umidade, erosao, vegetacao):

    nota = (umidade + vegetacao) - erosao

    if nota >= 100:
        return "Recuperação Avançada"

    elif nota >= 60:
        return "Recuperação Moderada"

    else:
        return "Recuperação Inicial"


def adicionar_historico(registro):
    historico_monitoramento.append(registro)


def dashboard():

    print("\n=== DASHBOARD ===")

    print("Usuários cadastrados:", len(contas))
    print("Análises realizadas:", len(historico_monitoramento))
    print("Alertas registrados:", len(alertas_agricolas))


def gerar_relatorio():

    print("\n=== RELATÓRIO AGRÍCOLA ===")

    if len(historico_monitoramento) == 0:
        print("Nenhum dado disponível.")
        return

    for item in historico_monitoramento:

        print("\nPropriedade:", item["propriedade"])
        print("Resultado:", item["resultado"])


#MENU

opcao = -1

while opcao != 0:

    print("\n================================")
    print("    ReCultiva")
    print("================================")
    print("1 - Sobre a plataforma")
    print("2 - Cadastrar conta")
    print("3 - Ver alertas agrícolas")
    print("4 - Tecnologias utilizadas")
    print("5 - Consultar sensores")
    print("6 - Analisar propriedade")
    print("7 - Histórico de análises")
    print("8 - Recomendação agrícola")
    print("9 - Calcular recuperação")
    print("10 - Dashboard")
    print("11 - Relatório")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    match opcao:

        case 1:

            print("\nA ReCultiva utiliza satélites, sensores e inteligência artificial")
            print("para auxiliar agricultores na recuperação de áreas afetadas")
            print("pelas enchentes ocorridas no Rio Grande do Sul.")

        case 2:

            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")

            conta = {
                "nome": nome,
                "email": email,
                "senha": senha
            }

            cadastrar(conta)

        case 3:

            print("\n=== ALERTAS ===")
            mostrar_lista(alertas_agricolas)

        case 4:

            mostrar_tecnologias()

        case 5:

            sensor_agricola()

        case 6:

            propriedade = input("Nome da propriedade: ")

            resultado = analisar_propriedade()

            print("\nResultado da análise:")
            print(propriedade, "-", resultado)

            registro = {
                "propriedade": propriedade,
                "resultado": resultado
            }

            adicionar_historico(registro)

        case 7:

            print("\n=== HISTÓRICO ===")

            if len(historico_monitoramento) == 0:
                print("Nenhuma análise realizada.")

            else:

                for item in historico_monitoramento:

                    print(
                        item["propriedade"],
                        "-",
                        item["resultado"]
                    )

        case 8:

            degradacao = int(
                input("Informe o nível de degradação (1 a 10): ")
            )

            print(
                "Recomendação:",
                recomendacao_personalizada(degradacao)
            )

        case 9:

            umidade = int(input("Umidade (%): "))
            erosao = int(input("Erosão (%): "))
            vegetacao = int(input("Cobertura vegetal (%): "))

            print(
                "Situação:",
                calcular_recuperacao(
                    umidade,
                    erosao,
                    vegetacao
                )
            )

        case 10:

            dashboard()

        case 11:

            gerar_relatorio()

        case 0:

            print("Encerrando sistema...")

        case _:

            print("Opção inválida.")
