import sys
from datetime import date

def main():
    print("\n Olá! Seja bem-vindo ao sistema da Biblioteca Senai!")
    print("\n Digite 1 para Cadastrar um Usuário \n Digite 2 para Cadastrar um Livro \n Digite 3 para Cadastrar um Empréstimo de Livro \n Digite 4 para ver o Histórico de Empréstimos por Livro \n Digite 5 para ver o Histórico de Empréstimo por Usuário \n Digite 6 para ver as Categorias de Livros \n Digite 7 para sair")
    opcao = input("\n Digite a opção desejada: ")

    match opcao:
        case '1':
            print("\n Você escolheu Cadastrar um Usuário!")
            print("\n Digite o nome do usuário: ")
            nome = input()
            print("\n Digite o CPF do usuário (XXX.XXX.XXX-XX): ")
            cpf = input()
            print("\n Digite o telefone do usuário ((XX) XXXXX-XXXX): ")
            telefone = input()
            print("\n Digite a data de nascimento do usuário (DD/MM/AAAA): ")
            data_nascimento = input()
            data_cadastro = date.today()
            
            # Isso aqui vai criar um dicionário com os dados do usuário (não foi o GPT que fez isso, foi eu Gabriele)
            usuario = {
                "nome": nome,
                "cpf": cpf,
                "telefone": telefone,
                "data_nascimento": data_nascimento,
                "data_cadastro": data_cadastro.strftime("%d/%m/%Y")
            }
            
            print(usuario)
            
        case '2':
            print("\n Você escolheu Cadastrar um Livro!")
            print("\n Digite o título do livro: ")
            titulo = input()
            print("\n Digite o autor do livro: ")
            autor = input()
            print("\n Digite o ISBN do livro")
            isbn = input()
            print("\n Digite a categoria do livro: ") # Nesse caso aqui, a categoria vai vir por meio de Sets
            categoria = input()
            print("\n Digite o ano de publicação do livro: ")
            ano_publicacao = input()
            data_cadastro = date.today()
            
            # Isso aqui vai criar um dicionário com os dados do livro (não foi o GPT que fez isso, foi eu Gabriele)
            livro = {
                "titulo": titulo,
                "autor": autor,
                "isbn": isbn,
                "categoria": categoria,
                "ano_publicacao": ano_publicacao,
                "data_cadastro": data_cadastro.strftime("%d/%m/%Y")
            }
            
            print(livro)
            
        # case '3':
            
        # case '4':
            
        # case '5':
            
        # case '6':
        
        case '7':
            print("Obrigado por usar o sistema da Biblioteca Senai!")
            print("Até logo!")
            sys.exit()
        