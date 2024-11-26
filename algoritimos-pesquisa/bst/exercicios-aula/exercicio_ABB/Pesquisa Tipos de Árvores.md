# Pesquisa Outros Tipos de Árvores:

FONTE:  Algoritmos - Teoria e Prática - Thomas Cormen

## Red–Black Tree (Árvore rubro-negra) 

- ### O que é? 
	- Uma árvore vermelho-preto é uma árvore de busca binária com um bit extra de armazenamento por nó: sua cor — ela pode ser VERMELHA ou PRETA.
	- Cada nó da árvore contém agora os atributos cor, chave, esquerda, direita e p.
	- Uma árvore vermelho-preto é uma árvore de busca binária que satisfaz as seguintes propriedades vermelho-preto: 
		 1. Todo nó é vermelho ou preto. 
		 2. A raiz é preta. 
		 3. Toda folha é preta. 
		 4. Se um nó é vermelho, então os seus filhos são pretos. 
		 5. Para cada nó, todos os caminhos simples do nó até folhas descendentes contêm o mesmo número de nós pretos.
	- Exemplo:
		- Uma árvore vermelho-preto com nós pretos em negro e nós vermelhos em cinzento. Todo nó em uma árvore vermelho-preto é vermelho ou preto, os filhos de um nó vermelho são pretos, e todo caminho simples de um nó até uma folha descendente contém o mesmo número de nós pretos:
			1.  Toda folha, mostrada como um NIL, é preta. Cada nó não NIL é marcado com sua altura preta: nós NILs têm altura preta igual a 0:
				![[Pasted image 20241126110306.png]]
			2. A mesma árvore vermelho-preto, mas com folhas e o pai da raiz omitidos completamente:
				![[Pasted image 20241126110434.png]]
- ### Para que serve?  
	- Uma árvore de busca binária de altura h pode suportar qualquer das operações básicas de conjuntos dinâmicos no tempo O(h). 
	- Assim, as operações de conjuntos são rápidas se a altura da árvore de busca é pequena. 
	- Todavia, se a altura da árvore é grande, a execução dessas operações poderá ser mais lenta do que com uma lista ligada. 
	- Árvores vermelho-preto são um dos muitos esquemas de árvores de busca que são “balanceadas” de modo a garantir que operações básicas de conjuntos dinâmicos demorem o tempo O(lg n) no pior caso.
- ### Como funciona?
	- Inserção 
		- Para inserir um nó, usamos uma versão ligeiramente modificada do procedimento TREE-INSERT da BST para inserir o nó z na árvore T como se ela fosse uma árvore de busca binária comum e depois "colorimos" z de vermelho.
		- A chamada RB-INSERT(T, z) insere o nó z — cuja chave considera-se já ter sido inserida — na árvore vermelho-preto T:
			![[Pasted image 20241126111720.png]]
			- Há quatro diferenças entre os procedimentos TREE-INSERT e RB-INSERT:  
				1. Todas as instâncias de NIL em TREEINSERT são substituídas por T.nil; 
				2. Definimos z.esquerda e z.direita como T.nil nas linhas 14 e 15 de RB-INSERT, a fim de manter a estrutura de árvore adequada; 
				3. Colorimos z de vermelho na linha 16; 
				4. Visto que colorir z de vermelho pode causar uma violação de uma das propriedades vermelho-preto, chamamos RB-INSERT-FIXUP(T, z) na linha 17 de RB-INSERT para restaurar as propriedades vermelho-preto.
		- Para garantir que as propriedades vermelho-preto serão preservadas, chamamos um procedimento auxiliar RB-INSERT-FIXUP para colorir novamente os nós e executar rotações.
			![[Pasted image 20241126112103.png]]
			- Casos:
				1. Caso 1:
					![[Pasted image 20241126112703.png]]
					 - Um nó z depois da inserção. Como z e seu pai z.p são vermelhos, ocorre uma violação da propriedade 4. Visto que o tio y de z é vermelho, o caso 1 no código se aplica. Colorimos novamente os nós e movimentamos o ponteiro z para cima na árvore
				2. Caso 2:
					![[Pasted image 20241126113305.png]]
					- Mais uma vez, z e seu pai são vermelhos, mas o tio y de z é preto. Como z é o filho à direita de z.p, o caso 2 se aplica. Executamos uma rotação para a esquerda.
				3. Caso 3:
					![[Pasted image 20241126113412.png]]
					 - Agora, z é o filho à esquerda de seu pai, e o caso 3 se aplica. Colorindo novamente e executando uma rotação para a direita, é produzida a árvore vermelho-preto válida:
				1. Árvore vermelho-preto válida:
					![[Pasted image 20241126113620.png]]
	- Eliminação
		- Eliminar um nó de uma árvore vermelho-preto é um pouco mais complicado que inserir um nó. 
		- O procedimento para eliminar um nó de uma árvore vermelho-preto é baseado no procedimento RB-DELETE.
		- RB-DELETE
			- O procedimento RB-DELETE é como o procedimento TREE-DELETE, porém com linhas adicionais de pseudocódigo. 
			- Algumas dessas linhas adicionais rastreiam um nó y que poderia causar violações das propriedades vermelho-preto. 
			- Quando queremos eliminar o nó z e z tem menos do que dois filhos, z é removido da árvore e queremos que y seja z. 
			- Quando z tem dois filhos, y deve ser o sucessor de z , e y passa para a posição de z na árvore. 
			- Também lembramos a cor de y antes de ele ser eliminado da árvore ou passar para dentro dela, e rastreamos o nó x que passa para a posição original de y na árvore porque o nó x também poderia causar violações das propriedades vermelho-preto
			- ![[Pasted image 20241126115244.png]]
			- RB-TRANSPLANT:
				 ![[Pasted image 20241126114349.png]]
				- Há duas diferenças entre o procedimento RB-TRANSPLANT e o procedimento TRANSPLANT. 
						1. A linha 1 referencia a sentinela T.nil em vez de NIL;
						2. A atribuição a .p na linha 6 ocorre incondicionalmente: podemos atribuir a v.p mesmo que  aponte para a sentinela.
			- RB-DELETE-FIXUP:
				-  Após eliminar o nó z, RB-DELETE chama um procedimento auxiliar RB-DELETE-FIXUP, que muda as cores e executa rotações para restaurar as propriedades vermelho-preto.
				- ![[Pasted image 20241126115536.png]]
				- explicação
	- Rotação
		- As operações de árvores de busca TREE-INSERT e TREE-DELETE, quando executadas em uma árvore vermelho-preto com n chaves, demoram o tempo O(lg n). 
		- Como elas modificam a árvore, o resultado pode violar as propriedades vermelho-preto. 
		- Para restabelecer essas propriedades, devemos mudar as cores de alguns nós na árvore e também mudar a estrutura de ponteiros. 
		- Mudamos a estrutura de ponteiros por meio de rotação, uma operação local em uma árvore de busca que preserva a propriedade de árvore de busca binária. 
		- Quando fazemos uma rotação para a esquerda em um nó x, supomos que seu filho à direita y não é T.nil; x pode ser qualquer nó na árvore cujo filho à direita não é T.nil. A rotação para a esquerda “pivota” ao redor da ligação de x para y. 
		- Transforma y na nova raiz da subárvore, com x como filho à esquerda de y e o filho à esquerda de y como filho à direita de x.
		- ![[Pasted image 20241126130026.png]]
## B Tree, B+ tree  
- ### O que é? 
	- As B-árvores são diferentes das árvores vermelho-preto no sentido de que os nós de B-árvores podem ter muitos filhos, de alguns até milhares. Isto é, o “fator de ramificação” de uma B-árvore pode ser bastante grande, embora normalmente, dependa de características da unidade de disco utilizada. 
	- As B-árvores são semelhantes às árvores vermelho-preto no sentido de que toda B-árvore de n nós tem altura O(lg n). Todavia, a altura exata de uma B-árvore pode ser consideravelmente menor que a altura de uma árvore vermelho-preto porque seu fator de ramificação e, por consequência, a base do logaritmo que expressa sua altura pode ser muito maior. 
	- Portanto, também podemos usar Bárvores para implementar muitas operações de conjuntos dinâmicos no tempo O(lg n).
- ### Para que serve?  
	- B-árvores são árvores de busca balanceadas projetadas para funcionar bem em discos ou outros dispositivos de armazenamento secundário de acesso direto. 
	- B-árvores são semelhantes a árvores vermelho-preto, mas são melhores para minimizar operações de E/S de disco. 
	- Muitos sistemas de bancos de dados usam B-árvores ou variantes de B-árvores para armazenar informações.
- ### Como funciona?
	- Criação
		- Para construir uma B-árvore T, primeiro utilizamos B-TREE-CREATE para criar um nó de raiz vazio e depois chamamos B-TREE-INSERT para acrescentar novas chaves. 
		- Esses dois procedimentos usam um procedimento auxiliar ALLOCATE-NODE, que aloca uma página de disco para ser usada como um novo nó no tempo O(1). 
		- Podemos considerar que um nó criado por ALLOCATE-NODE não requer nenhuma operação DISK-READ, já que ainda não existe nenhuma informação útil armazenada no disco para esse nó.
		- ![[Pasted image 20241126175400.png]]
	- Inserção 
		- Quando se trata de uma B-árvore, não podemos simplesmente criar um novo nó de folha e inseri-lo, já que a árvore resultante deixaria de ser uma B-árvore válida. Em vez disso, inserimos a nova chave em um nó de folha existente. 
		- Visto que não podemos inserir uma chave em um nó de folha que está cheio, recorremos a uma operação que reparte um nó cheio y (que tem 2t - 1 chaves) em torno de sua chave mediana chavet [y] em dois nós que têm somente t - 1 chaves cada. 
		- A chave mediana sobe para dentro do pai de y para identificar o ponto de repartição entre as duas novas árvores. Porém, se o pai de y também está cheio, temos de reparti-lo antes de podermos inserir a nova chave e, assim, podemos acabar repartindo nós cheios por toda a árvore acima. 
		- Como ocorre com uma árvore de busca binária, podemos inserir uma chave em uma B-árvore em uma única passagem descendente pela árvore da raiz até uma folha. Para tal, não esperamos para verificar se realmente precisamos repartir um nó cheio para executar a inserção. Em vez disso, à medida que descemos a árvore à procura da posição à qual pertence a nova chave, repartimos cada nó cheio que encontramos pelo caminho (inclusive a própria folha). Assim, sempre que queremos repartir um nó cheio y, temos a certeza de que seu pai não está cheio.
	- Pesquisa
		- Executar uma busca em uma B-árvore é muito semelhante a executar uma busca em uma árvore de busca binária, exceto que, em vez de tomar uma decisão de ramificação binária ou de “duas vias” em cada nó, tomamos uma decisão de ramificação de várias vias, de acordo com o número de filhos do nó. 
		- Mais exatamente, em cada nó interno x, tomamos uma decisão de ramificação de (x.n + 1) vias. 
		- Exemplo:
			- ![[Pasted image 20241126180116.png]]
			- B-TREE-SEARCH é uma generalização direta do procedimento TREE-SEARCH definido para árvores de busca binária. BTREE-SEARCH toma como entrada um ponteiro para o nó de raiz x de uma subárvore e uma chave k que deve ser procurada nessa subárvore. 
			- Assim, a chamada de nível superior é da forma B-TREE-SEARCH(T.raiz, k). Se k está na Bárvore, B-TREE-SEARCH retorna o par ordenado (y, i), que consiste em um nó y e um índice i tal que y.chavei = k. Caso contrário, o procedimento retorna NIL.