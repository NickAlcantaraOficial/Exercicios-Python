from abc import ABC, abstractmethod


# 1. Criando a classe abstrata ItemBiblioteca
class ItemBiblioteca(ABC):

    @abstractmethod
    def exibir_informacoes(self):
        pass


# 2. Classe Livro herda de ItemBiblioteca
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_informacoes(self):
        print(f"📖 Livro: {self.titulo}, Autor: {self.autor}")


# 2. Classe Ebook herda de ItemBiblioteca
class Ebook(ItemBiblioteca):
    def __init__(self, titulo, autor, formato_arquivo):
        self.titulo = titulo
        self.autor = autor
        self.formato_arquivo = formato_arquivo

    def exibir_informacoes(self):
        print(f"📱 Ebook: {self.titulo}, Autor: {self.autor}, Formato: {self.formato_arquivo}")


# 2. Classe Revista herda de ItemBiblioteca
class Revista(ItemBiblioteca):
    def __init__(self, titulo, editora, edicao):
        self.titulo = titulo
        self.editora = editora
        self.edicao = edicao

    def exibir_informacoes(self):
        print(f"📰 Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}")


# 3. Testando as classes
# Instanciando os objetos das classes concretas
livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
ebook = Ebook("O Hobbit", "J.R.R. Tolkien", "PDF")
revista = Revista("National Geographic", "NatGeo", 2024)

# Chamando o método exibir_informacoes() para cada objeto
livro.exibir_informacoes()
ebook.exibir_informacoes()
revista.exibir_informacoes()

# Tentando instanciar a classe abstrata ItemBiblioteca (isso gerará um erro)
# item = ItemBiblioteca()  # Isso gera um erro, pois ItemBiblioteca é uma classe abstrata.
