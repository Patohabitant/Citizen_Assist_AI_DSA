# Evidências de testes

Cada caso iniciou uma nova execução de `main.py`. A sequência de entradas inclui o encerramento. A saída observada contém os trechos conferidos, na ordem em que apareceram, sem as repetições do menu.

## 1. Lista vazia

**Entradas**

~~~text
6
7
8
0
~~~

**Resultado esperado**

- Nenhum serviço encontrado.
- Nenhum serviço encontrado.
- Total de serviços: 0

**Saída observada**

~~~text
Nenhum serviço encontrado.
Nenhum serviço encontrado.
Total de serviços: 0
Sistema encerrado.
~~~

## 2. Opção, IDs e campo inválidos

**Entradas**

~~~text
9
1
abc
0
-2
30
(Enter sem texto)
Título eleitoral
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
0
~~~

**Resultado esperado**

- Opção inválida.
- Digite um inteiro positivo.
- Digite um inteiro positivo.
- Digite um inteiro positivo.
- Campo obrigatório.
- Serviço cadastrado.

**Saída observada**

~~~text
Opção inválida.
Digite um inteiro positivo.
Digite um inteiro positivo.
Digite um inteiro positivo.
Campo obrigatório.
Serviço cadastrado.
Sistema encerrado.
~~~

## 3. Cadastro e duplicidade

**Entradas**

~~~text
1
30
Título eleitoral
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
1
10
Certidão de nascimento
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
1
10
8
0
~~~

**Resultado esperado**

- Serviço cadastrado.
- Serviço cadastrado.
- ID já cadastrado.
- Total de serviços: 2

**Saída observada**

~~~text
Serviço cadastrado.
Serviço cadastrado.
ID já cadastrado.
Total de serviços: 2
Sistema encerrado.
~~~

## 4. Consulta válida e inexistente

**Entradas**

~~~text
1
10
Certidão de nascimento
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
2
10
2
99
0
~~~

**Resultado esperado**

- ID 10 | Certidão de nascimento | Documentação
- ID não encontrado.

**Saída observada**

~~~text
ID 10 | Certidão de nascimento | Documentação
ID não encontrado.
Sistema encerrado.
~~~

## 5. Pesquisa por categoria, título e sem retorno

**Entradas**

~~~text
1
10
Certidão de nascimento
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
1
20
Carteira de Identidade
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
3
2
DOCUMENTAÇÃO
3
1
carteira
3
1
passaporte
0
~~~

**Resultado esperado**

- ID 10 | Certidão de nascimento | Documentação
- ID 20 | Carteira de Identidade | Documentação
- Resultados: 2
- ID 20 | Carteira de Identidade | Documentação
- Resultados: 1
- Nenhum serviço encontrado.

**Saída observada**

~~~text
ID 10 | Certidão de nascimento | Documentação
ID 20 | Carteira de Identidade | Documentação
Resultados: 2
ID 20 | Carteira de Identidade | Documentação
Resultados: 1
Nenhum serviço encontrado.
Sistema encerrado.
~~~

## 6. Atualização e consulta

**Entradas**

~~~text
1
20
Carteira de Identidade
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
4
20
5
Posto B
2
20
0
~~~

**Resultado esperado**

- Serviço atualizado.
- Local: Posto B

**Saída observada**

~~~text
Serviço atualizado.
Local: Posto B
Sistema encerrado.
~~~

## 7. Ordenação pelo título

**Entradas**

~~~text
1
30
Título eleitoral
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
1
10
Certidão de nascimento
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
1
20
Carteira de Identidade
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
6
7
0
~~~

**Resultado esperado**

- ID 30 | Título eleitoral
- ID 10 | Certidão de nascimento
- ID 20 | Carteira de Identidade
- Resultados: 3
- ID 20 | Carteira de Identidade
- ID 10 | Certidão de nascimento
- ID 30 | Título eleitoral
- Resultados: 3

**Saída observada**

~~~text
ID 30 | Título eleitoral | Documentação
ID 10 | Certidão de nascimento | Documentação
ID 20 | Carteira de Identidade | Documentação
Resultados: 3
ID 20 | Carteira de Identidade | Documentação
ID 10 | Certidão de nascimento | Documentação
ID 30 | Título eleitoral | Documentação
Resultados: 3
Sistema encerrado.
~~~

## 8. Exclusão do primeiro, último e único nó, seguida de novo cadastro

**Entradas**

~~~text
1
30
Título eleitoral
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
1
10
Certidão de nascimento
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
1
20
Carteira de Identidade
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
5
30
5
20
5
10
5
99
8
1
20
Carteira de Identidade
Documentação
Descrição fictícia
Requisitos fictícios
Local fictício
6
0
~~~

**Resultado esperado**

- Serviço excluído.
- Serviço excluído.
- Serviço excluído.
- ID não encontrado.
- Total de serviços: 0
- Serviço cadastrado.
- ID 20 | Carteira de Identidade

**Saída observada**

~~~text
Serviço excluído.
Serviço excluído.
Serviço excluído.
ID não encontrado.
Total de serviços: 0
Serviço cadastrado.
ID 20 | Carteira de Identidade | Documentação
Sistema encerrado.
~~~

## Verificação da estrutura

Foram exercitadas as 720 permutações de seis registros, incluindo títulos equivalentes na comparação sem distinção de maiúsculas e minúsculas. Para cada permutação, a ordem foi comparada com uma ordenação estável de referência. Também foram verificadas a referência do último nó, a contagem após exclusões e a reinserção no fim.

**Resultado observado:** todas as 720 permutações passaram, assim como os oito cenários do menu.
