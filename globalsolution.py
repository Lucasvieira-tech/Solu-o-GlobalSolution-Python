# AgroRecover – Plataforma de Recuperação Agrícola
# Enchentes do RS (2024)

usuarios = [
    {"nome": "Alberto Vieira", "email": "alberto@email.com", "senha": "senha123"}
]
especialistas = [
    {"login": "agronomo1", "senha": "esp123"},
    {"login": "analista1", "senha": "esp456"},
]

areas = []
proximo_id = 1

#Utilitários

def menu(titulo, opcoes):
    print(f"\n{'='*40}\n  {titulo}\n{'='*40}")
    for op in opcoes:
        print(f"  {op}")

def ler_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Digite um número inteiro.")

def ler_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Digite um número válido.")

def recomendar(degradacao):
    if degradacao <= 3:
        return "Policultivo"
    elif degradacao <= 6:
        return "Irrigação inteligente + Biofertilizantes"
    else:
        return "Hidroponia emergencial"

def buscar_area(id_area):
    for a in areas:
        if a["id"] == id_area:
            return a
    return None

#Autenticação

def cadastrar_usuario():
    print("\n=== CADASTRO ===")
    nome  = input("  Nome  : ").strip()
    email = input("  Email : ").strip()
    senha = input("  Senha : ").strip()

    if not nome or not email or not senha:
        print("  Preencha todos os campos.")
        return
    if any(u["email"] == email for u in usuarios):
        print("  Email já cadastrado.")
        return

    usuarios.append({"nome": nome, "email": email, "senha": senha})
    print(f"  Usuário '{nome}' cadastrado!")

def login_usuario():
    print("\n=== LOGIN ===")
    email = input("  Email : ").strip()
    senha = input("  Senha : ").strip()
    for u in usuarios:
        if u["email"] == email and u["senha"] == senha:
            print(f"  Bem-vindo(a), {u['nome']}!")
            return u
    print("  Email ou senha incorretos.")
    return None

def login_especialista():
    print("\n=== LOGIN ESPECIALISTA ===")
    login = input("  Login : ").strip()
    senha = input("  Senha : ").strip()
    for e in especialistas:
        if e["login"] == login and e["senha"] == senha:
            print(f"  Bem-vindo(a), {login}!")
            return e
    print("  Login ou senha incorretos.")
    return None

#Áreas

def cadastrar_area(dono):
    global proximo_id
    print("\n=== CADASTRAR ÁREA ===")
    nome      = input("  Nome da área  : ").strip()
    latitude  = ler_float("  Latitude      : ")
    longitude = ler_float("  Longitude     : ")
    extensao  = ler_float("  Extensão (ha) : ")
    degradacao = ler_int("  Degradação 1-10: ")

    if not 1 <= degradacao <= 10:
        print("  Valor deve ser entre 1 e 10.")
        return

    areas.append({
        "id": proximo_id,
        "nome": nome,
        "latitude": latitude,
        "longitude": longitude,
        "extensao": extensao,
        "dono": dono,
        "degradacao": degradacao,
    })
    print(f"  Área '{nome}' cadastrada (ID {proximo_id}).")
    print(f"  Recomendação: {recomendar(degradacao)}")
    proximo_id += 1

def listar_areas(dono=None):
    print("\n=== ÁREAS ===")
    lista = [a for a in areas if dono is None or a["dono"] == dono]
    if not lista:
        print("  Nenhuma área encontrada.")
        return
    for a in lista:
        print(f"  [{a['id']}] {a['nome']} | Degradação: {a['degradacao']}/10 | {a['extensao']} ha")

def ver_detalhes():
    id_area = ler_int("  ID da área : ")
    a = buscar_area(id_area)
    if not a:
        print("  Área não encontrada.")
        return
    print(f"\n  ID        : {a['id']}")
    print(f"  Nome      : {a['nome']}")
    print(f"  Lat/Long  : {a['latitude']} / {a['longitude']}")
    print(f"  Extensão  : {a['extensao']} ha")
    print(f"  Degradação: {a['degradacao']}/10")
    print(f"  Dono      : {a['dono']}")
    print(f"  Técnica   : {recomendar(a['degradacao'])}")

def alterar_area():
    listar_areas()
    id_area = ler_int("  ID da área a alterar : ")
    a = buscar_area(id_area)
    if not a:
        print("  Área não encontrada.")
        return

    print("  Campos: nome, latitude, longitude, extensao, degradacao")
    campo = input("  Campo : ").strip().lower()

    if campo not in ("nome", "latitude", "longitude", "extensao", "degradacao"):
        print("  Campo inválido.")
        return

    if campo == "nome":
        a[campo] = input(f"  Novo valor: ").strip()
    elif campo == "degradacao":
        v = ler_int("  Novo valor (1-10): ")
        if 1 <= v <= 10:
            a[campo] = v
        else:
            print("  Valor inválido.")
            return
    else:
        a[campo] = ler_float("  Novo valor: ")

    print("  Campo atualizado!")

def excluir_area():
    listar_areas()
    id_area = ler_int("  ID da área a excluir : ")
    a = buscar_area(id_area)
    if not a:
        print("  Área não encontrada.")
        return
    if input(f"  Excluir '{a['nome']}'? (s/n): ").lower() == "s":
        areas.remove(a)
        print("  Área excluída.")

def relatorio(dono=None):
    print("\n=== RELATÓRIO ===")
    lista = [a for a in areas if dono is None or a["dono"] == dono]
    if not lista:
        print("  Sem dados.")
        return
    media = sum(a["degradacao"] for a in lista) / len(lista)
    print(f"  Total de áreas : {len(lista)}")
    print(f"  Degradação média: {media:.1f}/10")
    for a in lista:
        print(f"\n  {a['nome']} – Degradação: {a['degradacao']}/10")
        print(f"  Técnica: {recomendar(a['degradacao'])}")

#Menus

def menu_usuario(usuario):
    while True:
        menu(f"MENU – {usuario['nome'].upper()}", [
            "[1] Minhas áreas",
            "[2] Cadastrar área",
            "[3] Ver detalhes de área",
            "[4] Relatório",
            "[0] Sair",
        ])
        op = ler_int("  Opção: ")
        if op == 1:
            listar_areas(dono=usuario["email"])
        elif op == 2:
            cadastrar_area(dono=usuario["email"])
        elif op == 3:
            listar_areas(dono=usuario["email"])
            ver_detalhes()
        elif op == 4:
            relatorio(dono=usuario["email"])
        elif op == 0:
            print(f"  Até logo, {usuario['nome']}!")
            break
        else:
            print("  Opção inválida.")

def menu_especialista(esp):
    while True:
        menu(f"MENU ESPECIALISTA – {esp['login'].upper()}", [
            "[1] Cadastrar área",
            "[2] Alterar área",
            "[3] Excluir área",
            "[4] Listar todas as áreas",
            "[5] Ver detalhes de área",
            "[6] Relatório geral",
            "[0] Sair",
        ])
        op = ler_int("  Opção: ")
        if op == 1:
            cadastrar_area(dono=esp["login"])
        elif op == 2:
            alterar_area()
        elif op == 3:
            excluir_area()
        elif op == 4:
            listar_areas()
        elif op == 5:
            listar_areas()
            ver_detalhes()
        elif op == 6:
            relatorio()
        elif op == 0:
            print(f"  Até logo, {esp['login']}!")
            break
        else:
            print("  Opção inválida.")

#Principal

def main():
    print("\n=== AGRORECOVER – Recuperação Agrícola RS ===")
    while True:
        menu("TIPO DE ACESSO", [
            "[1] Usuário comum",
            "[2] Especialista",
            "[0] Sair",
        ])
        tipo = ler_int("  Opção: ")

        if tipo == 1:
            menu("ACESSO", ["[1] Login", "[2] Cadastrar"])
            op = ler_int("  Opção: ")
            if op == 1:
                usuario = login_usuario()
                if usuario:
                    menu_usuario(usuario)
            elif op == 2:
                cadastrar_usuario()

        elif tipo == 2:
            esp = login_especialista()
            if esp:
                menu_especialista(esp)

        elif tipo == 0:
            print("\n  Até logo! ")
            break
        else:
            print("  Opção inválida.")

if _name_ == "_main_":
    main()