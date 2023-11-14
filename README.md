# Automação-em-Python

Esse código utiliza a biblioteca `pyautogui` do Python para automatizar um processo de cadastro de produtos em algum sistema ou programa. Vou explicar passo a passo o que cada parte do código está fazendo:

1. **Login:**
   - O código clica na posição `(955, 539)` na tela (em coordenadas específicas) e digita o nome de usuário 'diogo'.
   - Em seguida, clica na posição `(954, 563)` e digita a senha '123456'.
   - Depois, clica na posição `(868, 598)` para fazer login, com um tempo de duração de 1 segundo para cada clique (`duration = 1`).

2. **Cadastro de Produtos:**
   - Abre o arquivo de texto chamado 'produtos.txt' no modo de leitura (`'r'`).
   - Itera pelas linhas do arquivo, onde cada linha deve conter dados do produto separados por vírgulas (produto, quantidade, preço).
   - Para cada linha do arquivo:
     - Extrai o nome do produto, a quantidade e o preço usando `linha.split(',')`.
     - Simula cliques e digitações nas coordenadas específicas na tela para preencher o formulário do sistema:
       - Clica na posição `(673, 525)` e digita o nome do produto.
       - Clica na posição `(667, 553)` e digita a quantidade.
       - Clica na posição `(671, 583)` e digita o preço.
       - Clica na posição `(593, 737)` para registrar o produto no sistema, com um tempo de duração de 0.5 segundos para cada ação (`duration = 0.5`).

3. **Finalização:**
   - Após completar o cadastro de todos os produtos do arquivo, o código aguarda por 1 segundo (`sleep(1)`), possivelmente para garantir que todos os processos tenham sido concluídos antes de finalizar.

Esse código é uma forma de automação, simulando cliques e digitações em locais específicos da tela para inserir dados de produtos em algum sistema. As coordenadas utilizadas (`(x, y)`) podem variar dependendo do tamanho e posição da janela do programa ou site que está sendo automatizado.
