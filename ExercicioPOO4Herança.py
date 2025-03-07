# Classe Livro (classe papaithon)
class Livro: #criando a classe
    def __init__(self, titulo, autor, ano_publicacao): #atributos do papai
        self.titulo = titulo
        self.__autor = autor  # Atributo privado
        self.ano_publicacao = ano_publicacao

    @property #facilitando os getters and setters - salvando demais o código
    def autor(self):
        return self.__autor  # Retorna o autor

    @autor.setter
    def autor(self, novo_autor):
        self.__autor = novo_autor  # Altera o autor

    def exibir_informacoes(self):
        # mostra as informações do livro
        print(f"O Livro: {self.titulo}, autor: {self.autor}, Ano: {self.ano_publicacao}")


# Classe Ebook (herdando de papai)
class Ebook(Livro):
    def __init__(self, titulo, autor, ano_publicacao, formato_arquivo):
        # Chama o construtor da classe pai (Livro)
        super().__init__(titulo, autor, ano_publicacao)
        self.formato_arquivo = formato_arquivo  # Atributo específico para Ebook

    def exibir_informacoes(self):
        # Chama o método da classe papai pra não duplicar o código
        super().exibir_informacoes()
        print(f"Formato do arquivo: {self.formato_arquivo}")  # Exibe o formato do arquivo


# Criando um Livro
livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro.exibir_informacoes()

# Criando um Ebook
ebook = Ebook("O Hobbit", "J.R.R. Tolkien", 1937, "PDF")
ebook.exibir_informacoes()
