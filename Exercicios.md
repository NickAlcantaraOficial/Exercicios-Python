EXERCÍCIOS OO

Visão Geral dos Conceitos de POO
Antes de começar, segue um breve panorama dos conceitos que serão avaliados:
1.	Classe: Modelo ou “molde” que define a estrutura e o comportamento de um conjunto de objetos.
2.	Objeto: Instância de uma classe; representa concretamente um “elemento” baseado no modelo definido pela classe.
3.	Atributos: Variáveis que guardam estado ou características de uma classe/objeto.
4.	Métodos: Funções associadas a uma classe, que definem comportamentos dos objetos.
5.	Encapsulamento: Forma de proteger o acesso direto a atributos e métodos, geralmente usando modificadores de visibilidade (em Python, convenções de uso de underscore).
6.	Herança: Capacidade de criar novas classes a partir de classes existentes, aproveitando e especializando comportamentos.
7.	Polimorfismo: Possibilidade de objetos de diferentes classes responderem de forma diferente a uma mesma chamada de método.
8.	Abstração: Habilidade de representar conceitos do mundo real em classes, focando no que é essencial e escondendo detalhes internos.
9.	Composição: Relação “tem-um” (ex.: um Carro “tem-um” Motor). Quando o objeto-contêiner é destruído, os objetos componentes também devem deixar de existir.
10.	Agregação: Relação “tem-um” mais fraca (ex.: um Time “tem” vários Jogadores, mas os Jogadores podem existir independentemente do Time).
11.	Métodos Mágicos (ou Especiais): Métodos que começam e terminam com __ (underscores duplos), como __init__, __str__, __len__, etc.
12.	Exceções Personalizadas: Classes que herdam de Exception para tratar erros específicos da aplicação.
13.	Métodos de Classe e Métodos Estáticos: Métodos declarados com @classmethod e @staticmethod que não requerem instância para serem chamados.
14.	Propriedades (getter/setter): Uso de @property, @nome.setter, etc., para gerenciar acesso a atributos de forma encapsulada.
________________________________________
Cenário Proposto
Para tornar os exercícios mais integrados, vamos supor que estamos desenvolvendo um mini-sistema de gerenciamento de uma Biblioteca. Cada exercício será um passo para construir ou melhorar esse sistema, sempre focando em um ou mais conceitos de POO.
________________________________________
Exercício 1: Criação de Classes e Objetos
Conceito trabalhado: Classe e Objeto
Enunciado:
1.	Crie uma classe chamada Livro (representando um livro da biblioteca) com os atributos: 
o	titulo (string)
o	autor (string)
o	ano_publicacao (int)
2.	No método __init__, inicialize esses atributos.
3.	Instancie dois objetos da classe Livro com dados fictícios e imprima os dados de cada objeto na tela.
Dicas:
•	Use o construtor __init__ para definir os atributos.
•	Teste imprimindo o titulo, autor e ano_publicacao de cada livro.
________________________________________
Exercício 2: Atributos e Métodos de Instância
Conceito trabalhado: Atributos e Métodos
Enunciado:
1.	Ainda na classe Livro, crie dois métodos: 
o	exibir_informacoes(): que imprime na tela todos os dados do livro em um formato amigável.
o	get_idade_do_livro(): que retorna quantos anos se passaram desde a publicação do livro até o ano atual (assuma que o ano atual é 2025, caso queira simplificar).
2.	Mostre o uso dos métodos instanciando novamente os livros e chamando esses métodos para cada objeto.
Dicas:
•	Você pode usar uma variável ano_atual = 2025 para calcular a idade do livro se não quiser importar datas dinâmicas.
•	Não se esqueça de return no método que informa a idade do livro.
________________________________________
Exercício 3: Encapsulamento (Getters e Setters)
Conceito trabalhado: Encapsulamento
Enunciado:
1.	Torne o atributo autor privado (ou semi-privado, seguindo a convenção Python) na classe Livro, nomeando-o como self.__autor.
2.	Implemente métodos de acesso (get e set) para manipular e obter o autor. 
o	get_autor()
o	set_autor(novo_autor)
3.	Ajuste o método exibir_informacoes() para usar o get_autor() em vez de acessar diretamente o atributo.
4.	Demonstre o uso desses métodos ao instanciar e modificar o autor de um livro.
Dicas:
•	Em Python, não há “encapsulamento” estrito como em outras linguagens, mas usamos a convenção de __atributo para indicar que ele não deve ser acessado diretamente.
•	Pense em como a mudança de autor reflete ao exibir as informações.
________________________________________
Exercício 4: Herança
Conceito trabalhado: Herança
Enunciado:
1.	Crie uma classe Ebook que herde de Livro.
2.	Adicione o atributo formato_arquivo (por exemplo, "PDF", "EPUB") no construtor.
3.	Reescreva o método exibir_informacoes() para incluir o tipo de arquivo.
4.	Crie instâncias de Ebook e Livro, e mostre na tela que a classe Ebook herda e utiliza métodos/atributos da classe Livro, mas com sua especialização.
Dicas:
•	No construtor (__init__), chame o construtor da classe-pai (super().__init__(...)) para aproveitar a inicialização de Livro.
•	A sobrescrita do método exibir_informacoes() deve chamar a versão original para não duplicar código.
________________________________________
Exercício 5: Polimorfismo
Conceito trabalhado: Polimorfismo
Enunciado:
1.	Crie outra classe chamada Revista que também possua atributos como titulo, editora e edicao (número da edição).
2.	Crie um método exibir_informacoes() em Revista para exibir seus dados.
3.	Crie uma função fora das classes chamada exibir_item_biblioteca(item), que chama o método exibir_informacoes() do objeto recebido.
4.	Demonstre que, passando um objeto Livro, Ebook ou Revista para exibir_item_biblioteca(item), a chamada ao método exibir_informacoes() se comporta de maneiras diferentes.
Dicas:
•	O polimorfismo aparece quando chamamos o método exibir_informacoes() para cada tipo de objeto, mas cada classe implementa esse método de forma diferente.
•	As assinaturas podem ser iguais, mas a implementação interna difere.
________________________________________
Exercício 6: Abstração (Classes Abstratas)
Conceito trabalhado: Abstração
Enunciado:
1.	Crie uma classe abstrata ItemBiblioteca que declare, pelo menos, um método abstrato exibir_informacoes(). 
o	Para isso, importe e use from abc import ABC, abstractmethod.
2.	Faça com que as classes Livro, Ebook e Revista herdem de ItemBiblioteca.
3.	Certifique-se de que cada classe concreta implemente o método exibir_informacoes().
Dicas:
•	Em Python, para criar uma classe abstrata, sua classe deve herdar de ABC e qualquer método abstrato deve ser decorado com @abstractmethod.
•	Tentar instanciar ItemBiblioteca diretamente deve gerar um erro.
________________________________________
Exercício 7: Composição
Conceito trabalhado: Composição (“tem-um” forte)
Enunciado:
1.	Crie uma classe chamada Autor. Ela terá atributos como nome e nacionalidade.
2.	Modifique a classe Livro para obrigatoriamente receber um objeto Autor em seu construtor.
3.	Dentro de Livro, guarde este objeto em um atributo privado __autor.
4.	No método exibir_informacoes() de Livro, exiba também as informações do Autor.
Dicas:
•	Essa relação é de composição: sem o Livro, o Autor não faz sentido dentro daquele contexto (ou seja, o autor está fortemente vinculado ao livro, neste exemplo).
•	Quando criar o livro, você deverá primeiro instanciar um Autor, depois passar esse Autor como parâmetro para o construtor de Livro.
________________________________________
Exercício 8: Agregação
Conceito trabalhado: Agregação (“tem-um” fraco)
Enunciado:
1.	Crie uma classe Biblioteca que possua o atributo nome (string) e uma lista de itens (lista_itens) do tipo ItemBiblioteca.
2.	A classe Biblioteca deve ter métodos como: 
o	adicionar_item(item: ItemBiblioteca)
o	remover_item(item: ItemBiblioteca)
o	listar_acervo(): que exibe as informações de todos os itens.
3.	Crie pelo menos dois objetos de classes diferentes (Livro, Revista ou Ebook) e agregue-os a uma instância de Biblioteca.
4.	Mostre que, ao destruir a instância de Biblioteca, os itens ainda podem existir independentemente (por exemplo, você pode imprimir as informações dos itens depois de remover a biblioteca).
Dicas:
•	A ideia de agregação é que os objetos contidos podem existir fora do contexto da “agregadora”.
________________________________________
Exercício 9: Métodos Mágicos (ou Especiais)
Conceito trabalhado: __str__, __len__, etc.
Enunciado:
1.	Na classe Biblioteca, sobrescreva o método __str__ para retornar uma representação em string que inclua o nome da biblioteca e a quantidade de itens.
2.	(Opcional) Você pode sobrescrever o método __len__ para que len(biblioteca) retorne o número de itens agregados.
Dicas:
•	O método __str__(self) deve retornar uma string.
•	Você pode usar len(self.lista_itens) dentro de __len__.
________________________________________
Exercício 10: Exceções Personalizadas
Conceito trabalhado: Exceções
Enunciado:
1.	Crie uma exceção personalizada, por exemplo, ExcecaoItemNaoEncontrado, que herde de Exception.
2.	Modifique o método remover_item(item) na classe Biblioteca para lançar ExcecaoItemNaoEncontrado caso o item não esteja na lista de itens.
3.	Trate essa exceção em um bloco try/except ao tentar remover um item que não exista na biblioteca.
Dicas:
•	Em Python, personalizamos exceções estendendo Exception ou suas subclasses.
•	Exemplo de classe de exceção: 
•	class ExcecaoItemNaoEncontrado(Exception):
•	    pass
________________________________________
Exercício 11: Métodos de Classe e Métodos Estáticos
Conceito trabalhado: @classmethod e @staticmethod
Enunciado:
1.	Adicione um atributo de classe total_itens em ItemBiblioteca para contar quantos itens (de qualquer tipo) já foram criados.
2.	Use um método de classe (@classmethod) para incrementar esse contador sempre que um novo objeto (Livro, Ebook ou Revista) for instanciado.
3.	Implemente um método estático (@staticmethod) em ItemBiblioteca que retorne, por exemplo, o ano atual (ou alguma informação genérica) e demonstre seu uso.
Dicas:
•	O método de classe recebe cls como primeiro parâmetro.
•	O método estático não recebe self nem cls.
________________________________________
Exercício 12: Revisão e Integração de Todos os Conceitos
Conceito trabalhado: Integração geral
Enunciado:
1.	Faça um script final (main.py, por exemplo) onde você crie: 
o	Uma instância de Biblioteca.
o	Diversos objetos de Livro, Ebook e Revista, todos herdando de ItemBiblioteca.
o	Agrupe todos eles na Biblioteca.
2.	Teste todos os métodos criados (exibir informações, remoção com tratamento de exceção, polimorfismo, etc.).
3.	Exiba o resultado do print(biblioteca) (que usa __str__) e len(biblioteca) (se implementado).
4.	Mostre que está sendo usado o contador de itens (método de classe) e o método estático.
Dicas:
•	Este é o momento de validar todo o código produzido, garantindo que cada conceito foi corretamente aplicado.
________________________________________
Conclusão
Seguindo essa sequência de exercícios, o candidato terá a oportunidade de demonstrar conhecimento de todos os pilares da Programação Orientada a Objetos (classes, objetos, herança, polimorfismo, encapsulamento, abstração), bem como aspectos mais avançados (composição, agregação, métodos mágicos, exceções personalizadas, métodos de classe/estáticos). Ao final, você terá um mini-sistema de gerenciamento de biblioteca completamente funcional, embora simples, cobrindo os principais tópicos de POO em Python.

