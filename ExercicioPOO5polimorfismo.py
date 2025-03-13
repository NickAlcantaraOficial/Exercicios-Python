    class Livro:
        def __init__(self, titulo, autor):
            self.titulo = titulo
            self.autor = autor

        def exibir_informacoes(self):
            print(f"📖 Livro: {self.titulo}, Autor: {self.autor}")


    class Ebook(Livro):
        def __init__(self, titulo, autor, formato_arquivo):
            super().__init__(titulo, autor)
            self.formato_arquivo = formato_arquivo

        def exibir_informacoes(self):
            print(f"📱 Ebook: {self.titulo}, Autor: {self.autor}, Formato: {self.formato_arquivo}")


    class Revista:
        def __init__(self, titulo, editora, edicao):
            self.titulo = titulo
            self.editora = editora
            self.edicao = edicao

        def exibir_informacoes(self):
            print(f"📰 Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}")


    # 🔥 Função que usa polimorfismo
    def exibir_item_biblioteca(item):
        item.exibir_informacoes()  # Chama o método correspondente à classe do objeto


    # Criando objetos diferentes
    livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
    ebook = Ebook("O Hobbit", "J.R.R. Tolkien", "PDF")
    revista = Revista("National Geographic", "NatGeo", 2024)

    # Usando polimorfismo: mesma função para diferentes classes!
    exibir_item_biblioteca(livro)
    exibir_item_biblioteca(ebook)
    exibir_item_biblioteca(revista)
