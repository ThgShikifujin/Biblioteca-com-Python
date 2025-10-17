# classe livro, serve para guardar os atributos ou quase todos que um livro real teria.
class Livros:

    def __init__(self, titulo, autor, ano, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade
        self.disponivel = True


# esta classe fica responsável por adiministrar os Livros, bem próximo ao que uma biblioteca de verdade faria.
class Biblioteca:

    # Aqui estou criando a lista de livros.
    def __init__(self):
        self.livros = []

    # função para adicionar livros na lista de livros, o append() adiciona um item a lista de livros.
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    # Função para listar todos os livros em self.livros.
    def listar_livros(self):
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(
                f"{livro.titulo} - {livro.autor} ({livro.ano}) | {livro.quantidade} ({status})")

    # Função para emprestar os livros disponível da lista de livros, diminuir a quantidade e verificar se pode ou não emprestar verificando se o titulo existe na lista e se a quantidade esta > 0.
    def empresta_livro(self, titulo_livro):
        for livro in self.livros:
            if livro.titulo.lower() == titulo_livro.lower():
                if livro.quantidade > 0:
                    livro.quantidade -= 1
                    if livro.quantidade == 0:
                        livro.disponivel = False
                    print(f"O livro '{livro.titulo}' foi emprestado.")
                else:
                    print(f"Desculpe, já não há mais cópias do livro '{livro.titulo}' disponíveis.")
                return
        print(f"O livro '{titulo_livro}' não foi encontrado.")

    # Função para devolver um livro emprestado, conferirndo se o livros existe na lista e adicionando na quantidade.
    def devolve_livro(self, titulo_livro):
        for livro in self.livros:
            if livro.titulo.lower() == titulo_livro.lower():
                livro.quantidade += 1
                livro.disponivel = True
                print(f"O livro '{livro.titulo}' foi devolvido com sucesso!")
                return
        print(f"O livro '{titulo_livro}' não foi encontrado.")

    # Função que faz uma busca na lista de livros e mostra as informações do livro, verificando se ele existe ou não na lista.
    def buscar_livro(self, titulo_livro):
        for livro in self.livros:
            if livro.titulo.lower() == titulo_livro.lower():
                print(f"""Livro encontrado: 
Titulo: {livro.titulo}
Autor: {livro.autor}
Ano: {livro.ano}
Disponíveis {livro.quantidade}""")
                return
        print("Livro não encontrado!")


# Essa é a parte de interação com o usuário, aqui vou utilizar as funções acima.
biblioteca = Biblioteca()


while True:
    print("\n=== MENU DA BIBLIOTECA ===")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro")
    print("4. Emprestar livro")
    print("5. Devolver livro")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Informe o Título: ")
        autor = input("Informe o Autor: ")
        ano = int(input("Informe o ano de publicação: "))
        quantidade = int(input("Informe a quantidade: "))

        novo_livro = Livros(titulo, autor, ano, quantidade)

        biblioteca.adicionar_livro(novo_livro)

        print(f"\n Livro '{titulo}' foi cadastrado com sucesso!")
    elif opcao == "2":
        biblioteca.listar_livros()
    elif opcao == "3":
        titulo = input("Digite o nome do livro desejado: ")

        biblioteca.buscar_livro(titulo)
    elif opcao == "4":
        titulo = input("Informe o titulo do livro a ser emprestado: ")

        biblioteca.empresta_livro(titulo)
    elif opcao == "5": 
        titulo = input("Informe o livro a ser devolvido: ")

        biblioteca.devolve_livro(titulo)
    elif opcao == "6":
        print("Encerrando o sistema...")
        break