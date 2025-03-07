class Livro:  # Criando a classe Livro
    def __init__(self, titulo, autor, ano_publicacao):  # Criando os atributos da classe
        self.titulo = titulo
        self.__autor = autor  # Usando o "dois underscore" torna-se o atributo privado
        self.ano_publicacao = ano_publicacao

    @property
    def autor(self):  # Acessa o autor de forma "simples", sem precisar do método get
        return self.__autor  # Retorna o autor

    @autor.setter
    def autor(self, novo_autor):  # Permite que o autor seja modificado
        self.__autor = novo_autor  # Altera o autor

    def exibir_informacoes(self):  # Criando a função exibir informações
        print(f"O Livro: {self.titulo}, autor: {self.autor}, Ano: {self.ano_publicacao}")

# Criando o livro
livro = Livro("O Senhor dos Anéis", "J.R.R Tolkien", 1954)
livro.exibir_informacoes()

# Mudando o autor
livro.autor = "João da Silva"  # Agora, podemos acessar e modificar o autor diretamente
livro.exibir_informacoes()
