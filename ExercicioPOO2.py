class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_dados(self):
        print(f"O Livro '{self.titulo}', foi escrito por {self.autor} e publicado no ano de {self.ano_publicacao}")

    def exibir_informacoes(self):
        print(f"Informações do Livro:\nTítulo: {self.titulo}\nAutor: {self.autor}\nAno de Publicação: {self.ano_publicacao}")

    def get_idade_do_livro(self):
        ano_atual = 2025
        idade = ano_atual - self.ano_publicacao
        return idade

# Criando os livros
livro1 = Livro("Bíblia NVI", "Thomas Nelson Brasil", 1973)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Exibindo informações dos livros
print("Livro 1:")
livro1.exibir_informacoes()
print(f"Idade do Livro: {livro1.get_idade_do_livro()} anos\n")

print("Livro 2:")
livro2.exibir_informacoes()
print(f"Idade do Livro: {livro2.get_idade_do_livro()} anos\n")
