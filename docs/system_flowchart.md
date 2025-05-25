```mermaid
flowchart TD
    A[Start] --> B[Display Main Menu]
    B --> C{Choose Option}
    
    C -->|1| D[Cadastrar Usuário]
    D -->|Input| D1[Nome]
    D1 --> D2[CPF]
    D2 --> D3[Telefone]
    D3 --> D4[Data Nascimento]
    D4 --> D5[Salvar Usuário]
    D5 --> B
    
    C -->|2| E[Cadastrar Livro]
    E -->|Input| E1[Título]
    E1 --> E2[Autor]
    E2 --> E3[ISBN]
    E3 --> E4[Categoria]
    E4 --> E5[Ano Publicação]
    E5 --> E6[Salvar Livro]
    E6 --> B
    
    C -->|3| F[Cadastrar Empréstimo]
    F --> B
    
    C -->|4| G[Ver Histórico por Livro]
    G --> B
    
    C -->|5| H[Ver Histórico por Usuário]
    H --> B
    
    C -->|6| I[Ver Categorias]
    I -->|Display| I1[Listar Categorias]
    I1 --> B
    
    C -->|7| J[Sair]
    J --> K[End]
    
    C -->|Invalid| L[Mostrar Erro]
    L --> B
```

# Sistema Biblioteca SENAI - Fluxograma do Sistema

Este fluxograma representa o funcionamento básico do Sistema de Biblioteca SENAI, mostrando as principais operações e fluxos de dados disponíveis no menu principal.

## Descrição do Fluxo

1. O sistema inicia mostrando o menu principal
2. O usuário pode escolher entre 7 opções diferentes:
   - Cadastrar um Usuário
   - Cadastrar um Livro
   - Cadastrar um Empréstimo
   - Ver Histórico de Empréstimos por Livro
   - Ver Histórico de Empréstimo por Usuário
   - Ver Categorias de Livros
   - Sair do Sistema

3. Cada opção leva a um fluxo específico que, após completado, retorna ao menu principal
4. O sistema continua em execução até que a opção de sair seja selecionada 