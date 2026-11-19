from collections import Counter
from dataclasses import dataclass
from typing import Iterator, Optional


@dataclass
class Servico:
    identificador: int
    titulo: str
    categoria: str
    descricao: str
    requisitos: str
    local: str


@dataclass
class No:
    servico: Servico
    proximo: Optional["No"] = None


class Catalogo:
    def __init__(self):
        self.inicio: Optional[No] = None
        self.fim: Optional[No] = None
        self.total = 0

    def __iter__(self) -> Iterator[Servico]:
        atual = self.inicio
        while atual is not None:
            yield atual.servico
            atual = atual.proximo

    def consultar(self, identificador):
        for servico in self:
            if servico.identificador == identificador:
                return servico
        return None

    def cadastrar(self, servico):
        if servico.identificador <= 0:
            raise ValueError("O ID deve ser positivo.")
        if self.consultar(servico.identificador) is not None:
            return False

        novo = No(servico)
        if self.fim is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self.total += 1
        return True

    def pesquisar(self, campo, termo):
        if campo not in ("titulo", "categoria"):
            raise ValueError("Campo de pesquisa inválido.")
        termo = termo.casefold()
        for servico in self:
            if termo in getattr(servico, campo).casefold():
                yield servico

    def atualizar(self, identificador, campo, valor):
        if campo not in ("titulo", "categoria", "descricao", "requisitos", "local"):
            raise ValueError("Campo de atualização inválido.")
        servico = self.consultar(identificador)
        if servico is None:
            return False
        setattr(servico, campo, valor)
        return True

    def excluir(self, identificador):
        anterior = None
        atual = self.inicio
        while atual is not None:
            if atual.servico.identificador == identificador:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual is self.fim:
                    self.fim = anterior
                self.total -= 1
                return True
            anterior, atual = atual, atual.proximo
        return False

    def ordenar_por_titulo(self):
        # A lista ordenada é construída reutilizando os nós existentes.
        ordenado = None
        ultimo = None
        atual = self.inicio
        while atual is not None:
            restante = atual.proximo
            titulo = atual.servico.titulo.casefold()

            if ultimo is not None and ultimo.servico.titulo.casefold() <= titulo:
                ultimo.proximo = atual
                atual.proximo = None
                ultimo = atual
            elif ordenado is None or titulo < ordenado.servico.titulo.casefold():
                atual.proximo = ordenado
                ordenado = atual
                if ultimo is None:
                    ultimo = atual
            else:
                anterior = ordenado
                while anterior.proximo.servico.titulo.casefold() <= titulo:
                    anterior = anterior.proximo
                atual.proximo = anterior.proximo
                anterior.proximo = atual

            atual = restante

        self.inicio = ordenado
        self.fim = ultimo

    def indicadores(self):
        return Counter(servico.categoria.casefold() for servico in self)
