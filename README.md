# Citizen_Assist_AI_DSA
Citizen Assist AI | Documentação e cidadania
FIAP · Global Solution 2026.2 · Data Structures and Algorithms · 1CC-FEV
Integrante	RM
Paulo Henrique Lira Bilac de Araujo	569496
Olavo Dadario Vianna Barreto	569272
Pedro Soares de Souza	571285


Objetivo e execução
O protótipo organiza informações sobre serviços de documentação e cidadania. Cada registro contém ID inteiro positivo e único, título, categoria, descrição, requisitos e local de atendimento. Os dados informados pelo usuário ficam em memória durante a execução. Para a demonstração, use registros fictícios.

Abra esta pasta no terminal e execute python main.py ou, no Windows, py main.py. O projeto usa Python 3.8 ou superior e apenas a biblioteca padrão.
Opção	Operação
1	Cadastrar serviço
2	Consultar por ID
3	Pesquisar por trecho do título ou da categoria, ignorando maiúsculas e minúsculas
4	Atualizar um campo textual de um serviço
5	Excluir por ID
6	Listar todos os serviços na ordem atual
7	Ordenar por título e exibir a ordem resultante
8	Mostrar total geral e quantidade por categoria
0	Encerrar


Implementação
main.py trata o menu e valida entradas. catalogo.py contém o modelo e as operações sobre a lista encadeada. Cada No aponta para um objeto Servico e para o próximo nó. O catálogo mantém referências para o primeiro e o último nó, além de um contador. O percurso começa no primeiro nó e segue as referências até encontrar o resultado ou chegar ao fim. A pesquisa por atributo percorre a lista inteira para mostrar todas as correspondências.

O cadastro anexa o nó ao fim após verificar o ID. Na exclusão, o nó anterior passa a apontar para o sucessor do removido. Se o removido era o primeiro, o início avança para seu sucessor. Se era o último, o fim passa a apontar para o anterior. Quando o único nó é removido, início e fim voltam a ser vazios.

O Insertion Sort retira um nó por vez da sequência original e o insere na posição correta da sequência ordenada. Quando o título já pertence ao fim da sequência ordenada, a referência para o último nó permite inseri-lo diretamente no fim. Títulos iguais preservam a ordem relativa, considerando a comparação sem distinção entre maiúsculas e minúsculas.
Complexidade
Considere n registros e k categorias distintas. Para comparar a quantidade de operações em função de n, considere o custo de manipulação de cada campo textual fixo.
Operação	Tempo	Justificativa
Cadastro completo	O(n) no pior caso	Verifica duplicidade por busca sequencial. Encadear o nó no fim custa O(1).
Consulta e atualização por ID	O(n) no pior caso	Podem percorrer até o último nó. Alterar o campo encontrado custa O(1).
Pesquisa por título ou categoria	O(n)	Examina cada nó para encontrar todas as correspondências.
Exclusão	O(n) no pior caso	Busca o ID enquanto acompanha o nó anterior. A alteração das referências custa O(1).
Listagem	O(n)	Visita todos os nós.
Insertion Sort	O(n) no melhor caso e O(n²) no pior	Uma entrada crescente é anexada em tempo constante por nó. A busca repetida de posições no meio da sequência ordenada pode exigir um número quadrático de comparações.
Indicadores	O(n + k) em média	Conta categorias em um percurso e exibe cada uma. O contador geral já está disponível em O(1).


A ordenação reutiliza os nós e usa O(1) de espaço auxiliar em função de n. Os indicadores usam O(k) de espaço auxiliar para a contagem por categoria.
Demonstração prática
1. Com a lista vazia, escolha 6. O sistema deve informar que nenhum serviço foi encontrado.
2. Cadastre, nesta ordem, ID 30 — Título eleitoral, ID 10 — Certidão de nascimento e ID 20 — Carteira de Identidade. Use a categoria Documentação nos dois últimos e Cidadania no primeiro. Preencha os demais campos com exemplos fictícios.
3. Tente cadastrar novamente o ID 10 e mostre a rejeição. Consulte o ID 20 e, depois, o ID 99.
4. Pesquise documentação por categoria. Atualize o local do ID 20 e consulte novamente para confirmar a alteração.
5. Liste e depois ordene por título. Compare a ordem original 30, 10, 20 com a ordem resultante 20, 10, 30. Explique como os nós são reposicionados um a um.
6. Exclua o ID 20 e mostre os indicadores com os dois serviços restantes. Exclua os registros restantes e mostre o total zero.
As entradas, expectativas e saídas verificadas na execução estão em Evidencias_Testes.md.
