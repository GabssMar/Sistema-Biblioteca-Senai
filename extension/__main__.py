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
        self.historico = ListaHistorico()
    
    # region Cadastros

    def cadastrar_livro(self):
        titulo = input("\nDigite o título do livro: ").strip().upper()
        if (titulo == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Titulo não pode ser nulo.")
            return
        
        autor = input("\nDigite o autor do livro: ").strip().upper()
        if (autor == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Autor não pode ser nulo.")
            return
        
        isbn = input("\nDigite o ISBN do livro: ").strip()
        if (isbn == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("ISBN não pode ser nulo.")
            return
        
        categoria = input("\nDigite a categoria do livro: ").strip().upper()
        if (categoria == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Categoria não pode ser nulo.")
            return
        
        ano_publicacao = input("\nDigite o ano de publicação do livro: ").strip()
        if (ano_publicacao == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Ano de publicação não pode ser nulo.")
            return
        
        if not ano_publicacao.isdigit():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ano de publicação deve conter apenas números.")
            return

        ano_publicacao = int(ano_publicacao)

        if ano_publicacao > 2025:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ano de publicação inválido, digite corretamente.")
            return
        
        quantidade_str = input("\nDigite a quantidade de cópias do livro: ").strip()
        if not quantidade_str.isdigit() or int(quantidade_str) <= 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Quantidade deve ser um número inteiro válido.")
            return

        quantidade = int(quantidade_str)

        data_cadastro = date.today().strftime("%d/%m/%Y")

        livro = Livro(titulo, autor, isbn, categoria, ano_publicacao, data_cadastro)
        self.livros[livro.titulo] = livro
        self.categorias.add(livro.categoria)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nLivro '{livro.titulo}' cadastrado com sucesso!")

        self.pilhas_copias[livro.titulo] = []
        for i in range(quantidade):
            self.pilhas_copias[livro.titulo].append(f"Cópia {i+1}")
        
    def cadastrar_usuario(self):
        nome = input("\nDigite o nome do usuário: ").strip().upper()
        if (nome == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Nome não pode ser nulo.")
            return

        cpf = input("\nDigite o CPF do usuário: ").strip()
        if (cpf == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("CPF não pode ser nulo.")
            return
        
        if not (cpf.isdigit() and len(cpf) == 11):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("CPF inválido! Digite apenas os números, sem pontos ou traços.")
            return


        telefone = input("\nDigite o telefone do usuário: ").strip()
        if (telefone == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Telefone não pode ser nulo.")
            return
        
        if not (len(telefone) == 11):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Telefone inválido! Foi digitado corretamente?")
            return
        
        data_nascimento = input("\nDigite a data de nascimento do usuário (DD/MM/AAAA): ").strip()
        if (data_nascimento == ""):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Data de nascimento não pode ser nulo.")
            return

        data_cadastro = date.today().strftime("%d/%m/%Y")
                
        usuario = Usuario(nome, cpf, telefone, data_nascimento, data_cadastro)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nUsuário '{usuario.nome}' cadastrado com sucesso!")
        self.usuarios[usuario.cpf] = usuario

    # endregion

    # region Logica Emprestimos
        
    def verificar_disponibilidade_livro(self, titulo_livro):
        return (
            titulo_livro in self.livros and
            titulo_livro in self.pilhas_copias and
            len(self.pilhas_copias[titulo_livro]) > 0
        )

    def adicionar_fila_espera(self, titulo_livro, cpf_usuario):
        if titulo_livro not in self.filas_espera:
            self.filas_espera[titulo_livro] = deque()
        fila = self.filas_espera[titulo_livro]

        if cpf_usuario in fila:
            print(f"Usuário {cpf_usuario} já está na fila de espera para o livro '{titulo_livro}'.")
            return
        
        fila.append(cpf_usuario)
        print(f"Usuário {cpf_usuario} adicionado à fila de espera para o livro '{titulo_livro}'.")
        
    def realizar_emprestimo(self, cpf_usuario, titulo_livro):
        if titulo_livro not in self.livros or cpf_usuario not in self.usuarios:
            os.system('cls' if os.name == 'nt' else 'clear')
            if titulo_livro not in self.livros and cpf_usuario not in self.usuarios:
                print("Livro e Usuário não encontrado no sistema.")
            elif titulo_livro not in self.livros:
                print("Livro não encontrado no sistema.")
            else:
                print("Usuário não encontrado no sistema.")
            return
        
        emprestimos_usuario = [key for key in self.emprestimos if key[0] == cpf_usuario]
        if len(emprestimos_usuario) >= 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Limite de 2 empréstimos ativos por usuário atingido.")
            return

        if (cpf_usuario, titulo_livro) in self.emprestimos:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("O usuário já possue este livro emprestado.")
            return

        livro_disponivel = self.verificar_disponibilidade_livro(titulo_livro)
    
        if livro_disponivel:
            copia = self.pilhas_copias[titulo_livro].pop()
            novo_emprestimo = Emprestimo(self.usuarios[cpf_usuario], self.livros[titulo_livro], copia)
            self.emprestimos[(cpf_usuario, titulo_livro)] = novo_emprestimo
            self.historico.adicionar_emprestimo(novo_emprestimo)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Empréstimo realizado com sucesso!")
        else:
            self.adicionar_fila_espera(titulo_livro, cpf_usuario)
            posicao = len(self.filas_espera[titulo_livro])
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Livro indisponível no momento.")
            print(f"Você foi adicionado à fila de espera na posição {posicao}")

    def verificar_fila_espera(self, titulo_livro):
        if titulo_livro in self.filas_espera and self.filas_espera[titulo_livro]:
            return self.filas_espera[titulo_livro][0]  # Retorna o primeiro da fila
        return None
    
    def realizar_devolucao(self, cpf_usuario, titulo_livro):
        if (cpf_usuario, titulo_livro) not in self.emprestimos:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Este livro não está emprestado.")
            return

        emprestimo = self.emprestimos.get((cpf_usuario, titulo_livro))
        if not emprestimo:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Este livro não está emprestado por este usuário.")
            return

        emprestimo.devolver()
        self.pilhas_copias[titulo_livro].append(emprestimo.copia)
        del self.emprestimos[(cpf_usuario, titulo_livro)]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Devolução realizada com sucesso!")

        while titulo_livro in self.filas_espera and self.filas_espera[titulo_livro]:
            proximo_cpf = self.filas_espera[titulo_livro][0]

            if proximo_cpf not in self.usuarios:
                print(f"Usuário {proximo_cpf} da fila de espera não encontrado. Removendo da fila.")
                self.filas_espera[titulo_livro].popleft()
                continue 

            livro_disponivel = self.verificar_disponibilidade_livro(titulo_livro)
            if livro_disponivel:
                self.filas_espera[titulo_livro].popleft()
                self.realizar_emprestimo(proximo_cpf, titulo_livro)
            else:
                break

    # endregion

    # region Classes

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
    def __init__(self, usuario, livro, copia):
        self.usuario = usuario
        self.livro = livro
        self.copia = copia
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
        
    def devolver(self):
        self.data_devolucao = datetime.now()
        
    def to_tuple(self):
        return (self.usuario.cpf, self.livro.titulo, self.data_emprestimo, self.data_devolucao)
    
    # region Historico
    
class NoHistorico:
    def __init__(self, emprestimo: Emprestimo):
        self.emprestimo = emprestimo
        self.proximo = None

class ListaHistorico:
    def __init__(self):
        self.inicio = None

    def adicionar_emprestimo(self, emprestimo: Emprestimo):
        novo_no = NoHistorico(emprestimo)
        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def exibir_historico(self):
        atual = self.inicio
        if atual is None:
            print("Nenhum empréstimo no histórico.")
        while atual:
            e = atual.emprestimo
            print(f"- Livro: {e.livro.titulo}")
            print(f"  Usuário: {e.usuario.nome}")
            print(f"  Data de Empréstimo: {e.data_emprestimo}")
            print(f"  Data de Devolução: {e.data_devolucao}")
            print("")
            atual = atual.proximo

    def exibir_ultimos_emprestimos(self, limite=10):
        historico = []
        atual = self.inicio
        while atual:
            historico.append(atual.emprestimo)
            atual = atual.proximo

        if not historico:
            print("\nNenhum empréstimo realizado!")
            return

        print(f"\nÚltimos {min(limite, len(historico))} empréstimos:")
        for emprestimo in reversed(historico[-limite:]):
            print(f"- Livro: {emprestimo.livro.titulo}")
            print(f"  Usuário: {emprestimo.usuario.nome}")
            print(f"  Data de Empréstimo: {emprestimo.data_emprestimo}")
            print(f"  Data de Devolução: {emprestimo.data_devolucao}\n")

    def exibir_emprestimo_por_livro(self, titulo_livro):
        atual = self.inicio
        encontrados = False

        while atual:
            e = atual.emprestimo
            if e.livro.titulo.lower() == titulo_livro.lower():
                if not encontrados:
                    print(f"\nHistórico de Empréstimos para o livro: {titulo_livro}\n")
                    encontrados = True
                print(f"- Usuário: {e.usuario.nome}")
                print(f"  Data de Empréstimo: {e.data_emprestimo}")
                print(f"  Data de Devolução: {e.data_devolucao}\n")
            atual = atual.proximo

        if not encontrados:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nNenhum empréstimo encontrado para o livro: {titulo_livro}")

    def exibir_emprestimo_por_usuario(self, cpf_usuario):
        atual = self.inicio
        encontrados = False

        while atual:
            e = atual.emprestimo
            if e.usuario.cpf == cpf_usuario:
                if not encontrados:
                    print(f"\nHistórico de Empréstimos para o usuário: {e.usuario.nome} (CPF: {cpf_usuario})\n")
                    encontrados = True
                print(f"- Livro: {e.livro.titulo}")
                print(f"  Data de Empréstimo: {e.data_emprestimo}")
                print(f"  Data de Devolução: {e.data_devolucao}\n")
            atual = atual.proximo

        if not encontrados:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nNenhum empréstimo encontrado para o usuário com CPF: {cpf_usuario}")

    # endregion

    # region Sistema

class SistemaBiblioteca(Biblioteca):
    def __init__(self):
        super().__init__()

    def menu_principal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("\n--- Olá! Seja bem-vindo ao sistema da Biblioteca Senai! ---")
            print("1 - Consultas")
            print("2 - Cadastros")
            print("3 - Empréstimos")
            print("# - Sair")
            escolha = input("Digite a opção desejada: ")
            self.escolha_busca_ou_cadastro(escolha)

    def escolha_busca_ou_cadastro(self, escolha):
        match escolha:
            case '1':
                print("\n--- CONSULTAS ---")
                print("1 - Histórico de Empréstimos mais recentes")
                print("2 - Histórico de Empréstimos por Livro")
                print("3 - Histórico de Empréstimos por Usuário")
                print("4 - Categorias de Livros")
                print("# - Voltar")
                sub_escolha = input("Escolha sua opção: ")
                self.escolha_tipo_busca(sub_escolha)

            case '2':
                print("\n--- CADASTROS ---")
                print("1 - Cadastrar Usuário")
                print("2 - Cadastrar Livro")
                print("# - Voltar")
                sub_escolha = input("Escolha sua opção: ")
                self.escolha_tipo_cadastro(sub_escolha)

            case '3':
                print("\n--- EMPRÉSTIMOS ---")
                print("1 - Realizar Empréstimo")
                print("2 - Registrar Devolução")
                print("# - Voltar")
                sub_escolha = input("Escolha sua opção: ")
                self.escolha_emprestimo(sub_escolha)

            case '#':
                print("Obrigado por usar o sistema da Biblioteca Senai!\n")
                sys.exit()

            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção inválida. Tente novamente.")

    def escolha_tipo_busca(self, escolha):
        match escolha:
            case '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nVocê escolheu ver a lista de Empréstimos mais recentes:")
                self.historico.exibir_ultimos_emprestimos(10)

            case '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nVocê escolheu ver o Histórico de Empréstimos por Livro!")
                titulo = input("Digite o título do livro: ")

                self.historico.exibir_emprestimo_por_livro(titulo)

            case '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nVocê escolheu ver o Histórico de Empréstimos por Usuário!")
                cpf = input("Digite o CPF do usuário: ")

                self.historico.exibir_emprestimo_por_usuario(cpf)

            case '4':
                print("\n Você escolheu ver as Categorias de Livros!")

                if self.categorias:
                    print("\nCategorias de Livros:")
                    for categoria in sorted(self.categorias):
                        print(f"- {categoria}")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nNenhuma categoria de livro cadastrada!")

            case '#':
                os.system('cls' if os.name == 'nt' else 'clear')
                return

            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção inválida.")

    def escolha_tipo_cadastro(self, escolha):
        match escolha:
            case '1':
                print("\nVocê escolheu Cadastrar um Usuário!")
                self.cadastrar_usuario()

            case '2':
                print("\n Você escolheu Cadastrar um Livro!")
                self.cadastrar_livro()

            case '#':
                os.system('cls' if os.name == 'nt' else 'clear')
                return

            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção inválida.")

    def escolha_emprestimo(self, escolha):
        match escolha:
            case '1':
                print("\nVocê escolheu efetuar um Empréstimo de Livro!")
                cpf = input("\nDigite o CPF do usuário: ")
                titulo = input("\nDigite o título do livro: ").upper()
                self.realizar_emprestimo(cpf, titulo)

            case '2':
                print("\nVocê escolheu efetuar uma Devolução de Livro!")
                cpf = input("\nDigite o CPF do Usuário: ")
                titulo = input("\nDigite o título do livro: ").upper()
                self.realizar_devolucao(cpf, titulo)

            case '#':
                os.system('cls' if os.name == 'nt' else 'clear')
                return

            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção inválida.")

    # endregion
    # endregion

    # region Program

def main():
    sistema = SistemaBiblioteca()
    sistema.menu_principal()

if __name__ == "__main__":
    main()

    # endregion