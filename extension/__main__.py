import sys
from datetime import date

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.categorias = set()
        self.usuarios = {}
        self.emprestimos = {}
        self.filas_espera = {}
        self.pilhas_copias = {}
        self.historico = None
    
    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro
        self.categorias.add(livro.categoria)
        
    def cadastrar_usuario(self, usuario):
        self.usuarios[usuario.cpf] = usuario

class Livro:
    def __init__(self, titulo, autor, isbn, categoria, ano_publicacao, data_cadastro):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.categoria = categoria
        self.ano_publicacao = ano_publicacao
        self.data_cadastro = data_cadastro
        
    def to_tuple(self):
        return (self.titulo, self.autor, int(self.ano_publicacao))

class Usuario:
    def __init__(self, nome, cpf, telefone, data_nascimento, data_cadastro):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.data_cadastro = data_cadastro
        
    def to_tuple(self):
        return (self.nome, self.cpf, self.telefone, self.data_nascimento, self.data_cadastro)


def main():
    biblioteca_senai = Biblioteca()

    while True:
        print("\n Olá! Seja bem-vindo ao sistema da Biblioteca Senai!")
        print("\n Digite 1 para Cadastrar um Usuário \n Digite 2 para Cadastrar um Livro \n Digite 3 para Cadastrar um Empréstimo de Livro \n Digite 4 para ver o Histórico de Empréstimos por Livro \n Digite 5 para ver o Histórico de Empréstimo por Usuário \n Digite 6 para ver as Categorias de Livros \n Digite 7 para sair")
        opcao = input("\n Digite a opção desejada: ")

        match opcao:
            case '1':
                print("\nVocê escolheu Cadastrar um Usuário!")
                nome = input("\nDigite o nome do usuário: ")
                cpf = input("\nDigite o CPF do usuário (XXX.XXX.XXX-XX): ")
                telefone = input("\nDigite o telefone do usuário ((XX) XXXXX-XXXX): ")
                data_nascimento = input("\nDigite a data de nascimento do usuário (DD/MM/AAAA): ")
                data_cadastro = date.today().strftime("%d/%m/%Y")
                
                usuario = Usuario(nome, cpf, telefone, data_nascimento, data_cadastro)
                biblioteca_senai.cadastrar_usuario(usuario)
                
                print(f"\nUsuário '{usuario.nome}' cadastrado com sucesso!")

            case '2':
                print("\n Você escolheu Cadastrar um Livro!")
                titulo = input("\nDigite o título do livro: ")
                autor = input("\nDigite o autor do livro: ")
                isbn = input("\nDigite o ISBN do livro: ")
                categoria = input("\nDigite a categoria do livro: ")
                ano_publicacao = input("\nDigite o ano de publicação do livro: ")
                data_cadastro = date.today().strftime("%d/%m/%Y")

                livro = Livro(titulo, autor, isbn, categoria, ano_publicacao, data_cadastro)
                biblioteca_senai.adicionar_livro(livro)

                print(f"\nLivro '{livro.titulo}' cadastrado com sucesso!")

            # case '3':
            
            # case '4':
            
            # case ''

            case '6':
                print("\n Você escolheu ver as Categorias de Livros!")

                if biblioteca_senai.categorias:
                    print("\nCategorias de Livros:")
                    for categoria in sorted(biblioteca_senai.categorias):
                        print(f"- {categoria}")
                else:
                    print("\nNenhuma categoria de livro cadastrada!")

            case '7':
                print("Obrigado por usar o sistema da Biblioteca Senai!")
                print("Até logo!")
                sys.exit()

            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()