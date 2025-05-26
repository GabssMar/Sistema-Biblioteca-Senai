import sys
from datetime import date, datetime
from collections import deque
import os

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.categorias = set()
        self.usuarios = {}
        self.emprestimos = {}
        self.filas_espera = {}
        self.pilhas_copias = {}
        self.historico = None
    
    def cadastrar_livro(self, livro):
        self.livros[livro.titulo] = livro
        self.categorias.add(livro.categoria)
        
    def cadastrar_usuario(self, usuario):
        self.usuarios[usuario.cpf] = usuario
        
    def verificar_disponibilidade_livro(self, titulo_livro):
        if titulo_livro not in self.livros:
            return False
        if titulo_livro in self.emprestimos:
            return False
        return True
        
    def adicionar_fila_espera(self, titulo_livro, cpf_usuario):
        if titulo_livro not in self.filas_espera:
            self.filas_espera[titulo_livro] = deque()
        self.filas_espera[titulo_livro].append(cpf_usuario)
        
    def realizar_emprestimo(self, cpf_usuario, titulo_livro):
        if titulo_livro not in self.livros:
            print("Livro não encontrado no sistema.")
            return
            
        if cpf_usuario not in self.usuarios:
            print("Usuário não encontrado no sistema.")
            return
            
        livro_disponivel = self.verificar_disponibilidade_livro(titulo_livro)
        
        if livro_disponivel:
            novo_emprestimo = Emprestimo(self.usuarios[cpf_usuario], self.livros[titulo_livro])
            self.emprestimos[titulo_livro] = novo_emprestimo
            print("Empréstimo realizado com sucesso!")
        else:
            self.adicionar_fila_espera(titulo_livro, cpf_usuario)
            posicao = len(self.filas_espera[titulo_livro])
            print("Livro indisponível no momento.")
            print(f"Você foi adicionado à fila de espera na posição {posicao}")

    def verificar_fila_espera(self, titulo_livro):
        if titulo_livro in self.filas_espera and self.filas_espera[titulo_livro]:
            return self.filas_espera[titulo_livro][0]  # Retorna o primeiro da fila
        return None
    
    def realizar_devolucao(self, cpf_usuario, titulo_livro):
        if titulo_livro not in self.emprestimos:
            print("Este livro não está emprestado.")
            return

        emprestimo = self.emprestimos[titulo_livro]
        
        if emprestimo.usuario.cpf != cpf_usuario:
            print("Este usuário não realizou o empréstimo deste livro.")
            return

        emprestimo.devolver()
        del self.emprestimos[titulo_livro]
        print("Devolução realizada com sucesso!")

        if titulo_livro in self.filas_espera and self.filas_espera[titulo_livro]:
            proximo_cpf = self.filas_espera[titulo_livro].popleft()
            self.realizar_emprestimo(proximo_cpf, titulo_livro)

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

class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
        
    def devolver(self):
        self.data_devolucao = datetime.now()
        
    def to_tuple(self):
        return (self.usuario.cpf, self.livro.titulo, self.data_emprestimo, self.data_devolucao)

def main():
    biblioteca_senai = Biblioteca()

    while True:
        print("\n Olá! Seja bem-vindo ao sistema da Biblioteca Senai!")
        print("\n Digite 1 para Cadastrar um Usuário \n Digite 2 para Cadastrar um Livro \n Digite 3 para Cadastrar um Empréstimo de Livro \n Digite 4 para Cadastrar uma Devolução de Livro \n Digite 5 para ver o Histórico de Empréstimos por Livro \n Digite 6 para ver o Histórico de Empréstimo por Usuário \n Digite 7 para ver as Categorias de Livros \n Digite 8 para sair")
        opcao = input("\n Digite a opção desejada: ")

        match opcao:
            case '1':
                print("\nVocê escolheu Cadastrar um Usuário!")
                nome = input("\nDigite o nome do usuário: ").upper()
                cpf = input("\nDigite o CPF do usuário: ")
                telefone = input("\nDigite o telefone do usuário: ")
                data_nascimento = input("\nDigite a data de nascimento do usuário (DD/MM/AAAA): ")
                data_cadastro = date.today().strftime("%d/%m/%Y")
                
                usuario = Usuario(nome, cpf, telefone, data_nascimento, data_cadastro)
                biblioteca_senai.cadastrar_usuario(usuario)
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\nUsuário '{usuario.nome}' cadastrado com sucesso!")

            case '2':
                print("\n Você escolheu Cadastrar um Livro!")
                titulo = input("\nDigite o título do livro: ").upper()
                autor = input("\nDigite o autor do livro: ").upper()
                isbn = input("\nDigite o ISBN do livro: ")
                categoria = input("\nDigite a categoria do livro: ").upper()
                ano_publicacao = input("\nDigite o ano de publicação do livro: ")
                data_cadastro = date.today().strftime("%d/%m/%Y")

                livro = Livro(titulo, autor, isbn, categoria, ano_publicacao, data_cadastro)
                biblioteca_senai.adicionar_livro(livro)

                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\nLivro '{livro.titulo}' cadastrado com sucesso!")

            case '3':
                print("\nVocê escolheu Cadastrar um Empréstimo de Livro!")
                cpf = input("\nDigite o CPF do usuário: ")
                titulo = input("\nDigite o título do livro: ").upper()
                biblioteca_senai.realizar_emprestimo(cpf, titulo)
            
            case '4':
                print("\nVocê escolheu Cadastrar uma Devolução de Livro!")
                cpf = input("\nDigite o CPF do Usuário: ")
                titulo = input("\nDigite o título do livro: ").upper()
                biblioteca_senai.realizar_devolucao(cpf, titulo)
                

                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\nDevolução de '{titulo}' realizada com sucesso!")

            case '5':
                print("\n Você escolheu ver o Histórico de Empréstimos por Livro!")

                if biblioteca_senai.emprestimos:
                    print("\nHistórico de Empréstimos:")
                    for titulo_livro, emprestimo in biblioteca_senai.emprestimos.items():
                        print(f"- Livro: {titulo_livro}")
                        print(f"  Usuário: {emprestimo.usuario.nome}")
                        print(f"  Data de Empréstimo: {emprestimo.data_emprestimo}")
                        print(f"  Data de Devolução: {emprestimo.data_devolucao}")
                else:
                    print("\nNenhum empréstimo realizado!")

            case '6':
                print("\n Você escolheu ver o Histórico de Empréstimo por Usuário!")

                if biblioteca_senai.emprestimos:
                    print("\nHistórico de Empréstimos por Usuário:")
                    for cpf_usuario, emprestimo in biblioteca_senai.emprestimos.items():
                        print(f"- Usuário: {cpf_usuario}")
                        print(f"  Livro: {emprestimo.livro.titulo}")
                        print(f"  Data de Empréstimo: {emprestimo.data_emprestimo}")
                        print(f"  Data de Devolução: {emprestimo.data_devolucao}")
                else:
                    print("\nNenhum empréstimo realizado!")

            case '7':
                print("\n Você escolheu ver as Categorias de Livros!")

                if biblioteca_senai.categorias:
                    print("\nCategorias de Livros:")
                    for categoria in sorted(biblioteca_senai.categorias):
                        print(f"- {categoria}")
                else:
                    print("\nNenhuma categoria de livro cadastrada!")

            case '8':
                print("Obrigado por usar o sistema da Biblioteca Senai!")
                print("Até logo!")
                sys.exit()

            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()