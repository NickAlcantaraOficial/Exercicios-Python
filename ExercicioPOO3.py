class Livro:  # Criando a classe Livro
    def __init__(self, titulo, autor, ano_publicacao):  # Criando os atributos da classe
        self.titulo = titulo
        self.__autor = autor  # Usando o "dois underscore" torna-se o atributo privado
        self.ano_publicacao = ano_publicacao

    def get_autor(self):  # Usado para acessar o método privado
        return self.__autor  # Retorna o autor

    def set_autor(self, novo_autor):  # Setando e modificando o autor
        self.__autor = novo_autor  # Altera o autor

    def exibir_informacoes(self):  # Criando a função exibir informações
        print(f"O Livro: {self.titulo}, autor: {self.get_autor()}, Ano: {self.ano_publicacao}")

# Criando o livro
livro = Livro("O Senhor dos Anéis", "J.R.R Tolkien", 1954)
livro.exibir_informacoes()

# Mudando o autor
livro.set_autor("João da Silva")
livro.exibir_informacoes()
