class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_dados(self):
        print(f"O Livro {self.titulo}, foi inscrita por {self.autor} e publicada no ano de {self.ano_publicacao}")

livro1 = Livro("Bíblia NVI", "Thomas Nelson Brasil", 1973)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)


livro1.exibir_dados()
livro2.exibir_dados()