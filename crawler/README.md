Passos para a utilização do programa

1. Entre no diretorio do crawler
    - No terminal
        cd bs_amazon

2. Ative o ambiente virtual
    - No terminal
        .env/scripts/activate

3. Amarmazenar Catalogos:
    -> Esse processo irá gerar um arquivo denominado 'catalgos.csv', onde ficara a lista de links de catalogos onde estão os produtos desejados para analise.

    - Acesse o arquivo 'armazenarCatalos.py' na sua IDE;
    - Localize a função def main();
    - Altere a variavel url para a url da pagina catalogo da amazon desejada (pode não suportar do tipo de pagina de catalogo inserida);
    - No segundo parâmetro da função 'leitorPaginaCategoria()' coloque a quantidade de paginas de catalogos você deseja armazenar sequencialmente
    - Rode o algoritimo: 'python armazenarCatalogos.py' no Terminal.

4. Execute o arquivo 'armazenarProdutos.py'
    -> Esse processo irá gerar um arquivo denominado 'produtos.csv', onde ficara a lista de links dos produtos que vão ter seus dados armazenados.

    - No terminal:
        python armazenarProdutos.py

5. Execute o arquivo 'armazenarDados.py'
    -> Esse processo irá gerar um arquivo denominado 'dados.csv' no diretorio 'memoriaExterna', que simula uma memoria externa. Neste arquivo ficara todos os dados dos produtos, dados esses que serão posteriormente ordenados pelo merge sort externo.

    - No terminal:
        python armazenarDados.py

6. Aplicando o Merge Sort Externo

    - Vá para o diretorio memoria interna:
        no terminal: cd../memoriaInterna
    - Acesse o arquivo mergeSortExterno.py
    - Localize a função def main()
    - Atualize os campos de endereço de memoria e os paramentros da função conforme necessario
    - Execute o programa