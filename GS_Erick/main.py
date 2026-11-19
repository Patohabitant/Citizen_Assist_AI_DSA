from catalogo import Catalogo, Servico


CAMPOS = {
    "1": ("titulo", "Título"),
    "2": ("categoria", "Categoria"),
    "3": ("descricao", "Descrição"),
    "4": ("requisitos", "Requisitos"),
    "5": ("local", "Local de atendimento"),
}


def ler_texto(rotulo):
    while True:
        valor = input(f"{rotulo}: ").strip()
        if valor:
            return valor
        print("Campo obrigatório.")


def ler_id():
    while True:
        try:
            identificador = int(input("ID: "))
            if identificador > 0:
                return identificador
        except ValueError:
            pass
        print("Digite um inteiro positivo.")


def exibir(servico):
    print(f"ID {servico.identificador} | {servico.titulo} | {servico.categoria}")
    print(f"  Descrição: {servico.descricao}")
    print(f"  Requisitos: {servico.requisitos}")
    print(f"  Local: {servico.local}")


def listar(servicos):
    total = 0
    for servico in servicos:
        exibir(servico)
        total += 1
    if total:
        print(f"Resultados: {total}")
    else:
        print("Nenhum serviço encontrado.")


def cadastrar(catalogo):
    identificador = ler_id()
    if catalogo.consultar(identificador) is not None:
        print("ID já cadastrado.")
        return
    dados = {campo: ler_texto(rotulo) for campo, rotulo in CAMPOS.values()}
    catalogo.cadastrar(Servico(identificador, **dados))
    print("Serviço cadastrado.")


def consultar(catalogo):
    servico = catalogo.consultar(ler_id())
    if servico is None:
        print("ID não encontrado.")
    else:
        exibir(servico)


def pesquisar(catalogo):
    opcao = input("Pesquisar por [1] título ou [2] categoria: ").strip()
    if opcao not in ("1", "2"):
        print("Opção inválida.")
        return
    campo, _ = CAMPOS[opcao]
    listar(catalogo.pesquisar(campo, ler_texto("Termo")))


def atualizar(catalogo):
    identificador = ler_id()
    if catalogo.consultar(identificador) is None:
        print("ID não encontrado.")
        return
    for numero, (_, rotulo) in CAMPOS.items():
        print(f"{numero}. {rotulo}")
    opcao = input("Campo a atualizar: ").strip()
    if opcao not in CAMPOS:
        print("Opção inválida.")
        return
    campo, rotulo = CAMPOS[opcao]
    catalogo.atualizar(identificador, campo, ler_texto(rotulo))
    print("Serviço atualizado.")


def excluir(catalogo):
    if catalogo.excluir(ler_id()):
        print("Serviço excluído.")
    else:
        print("ID não encontrado.")


def ordenar(catalogo):
    catalogo.ordenar_por_titulo()
    listar(catalogo)


def analisar(catalogo):
    print(f"Total de serviços: {catalogo.total}")
    for categoria, quantidade in catalogo.indicadores().items():
        print(f"{categoria}: {quantidade}")


def executar():
    catalogo = Catalogo()
    acoes = {
        "1": ("Cadastrar", cadastrar),
        "2": ("Consultar por ID", consultar),
        "3": ("Pesquisar", pesquisar),
        "4": ("Atualizar", atualizar),
        "5": ("Excluir", excluir),
        "6": ("Listar", listar),
        "7": ("Ordenar por título", ordenar),
        "8": ("Ver indicadores", analisar),
    }
    print("Citizen Assist AI | Documentação e cidadania")
    while True:
        print()
        for numero, (rotulo, _) in acoes.items():
            print(f"{numero}. {rotulo}")
        print("0. Encerrar")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            print("Sistema encerrado.")
            return
        if opcao in acoes:
            acoes[opcao][1](catalogo)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    try:
        executar()
    except (EOFError, KeyboardInterrupt):
        print("\nSistema encerrado.")
