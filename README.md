# Biblioteca Senai

### Descrição do projeto

Esse projeto é um sistema de gestão de biblioteca com interface de linha de comando (Sistema CLI), desenvolvido como projeto de entrega da P2 da disciplina de Estrutura de Dados.
O sistema foi pensado para facilitar a gestão dos cadastros, empréstimos e visualização do histórico da biblioteca.

### Funcionalidades

- Cadastro de usuário
- Cadastro de livro
- Cadastro de empréstimo de livros
- Visualizar empréstimos de livros
- Visualizar empréstimos de livros por usuário
- Visualizar categorias dos livros

### Recursos técnicos utilizados

- Listas - Pilhas
- Listas - Filas
- Tuplas
- Sets
- Dicionários
- Listas Encadeadas - Simplesmente Encadeadas

### Organização do código

docs/  
  ├─ system_flowchart.md  
extension/  
  ├─ __pycache__/  
    ├─ __init__.py  
    ├─ __main__.py  


### Como executar

**Requisitos**

- Instalar a versão mais recente do Python
- Baixar o arquivo zip do repositório

Após realizar as requisições acima, extraia os arquivos do projeto e acesse a pasta adquirida pelo CMD. Com essa pasta selecionada, rode o comando: python -m extension

### Exemplo de uso
--Menu Principal--  
--- Olá! Seja bem-vindo ao sistema da Biblioteca Senai! ---
 1 - Consultas
 2 - Cadastros
 3 - Empréstimos
 # - Sair
 Digite a opção desejada:
  
### Fluxograma
Para visualizar o fluxograma, [clique aqui!](docs/system_flowchart.md).  

### Decisões do Projeto
- **Lista - Pilhas:** Como um livro pode ter mais de uma cópia, tanto faz a ordem com qual os exemplares são emprestados. Como as pilhas seguem o padrão LIFO, achamos mais interessante usarmos para a liberação de livros para empréstimo.
- **Lista - Filas:** Utilizadas para organizar o empréstimo de livros, pois eles devem ser liberados por ordem de solicitação de empréstimo.
- **Tuplas:** Utilizadas para representar dados imutáveis de livros, usuários e empréstimos, facilitando a manter a integridade dos dados.
- **Sets:** Foram utilizados para guardar categorias únicas de livros, permitindo consultas mais rápidas.
- **Dicionarios:** Escolhidos para armazenar livros, usuários, empréstimos e filas de espera, para deixar as informações de forma visível e clara.
- **Listas encadeadas:** Utilizadas para armazenar os usuários cadastrados, permitindo inserções dinâmicas sem a necessidade de realocar posições na memória. Essa estrutura foi escolhida para representar melhor o crescimento contínuo da lista de usuários e facilitar operações de inserção e remoção.
