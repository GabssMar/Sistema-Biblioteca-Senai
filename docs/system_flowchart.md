```mermaid
flowchart TD
    A[Início] --> B[Menu Principal]
    B --> C{Escolha Opção}
    
    %% Cadastro de Usuário
    C -->|1| D[Cadastrar Usuário]
    D --> D1[Input: Nome]
    D1 --> D2[Input: CPF]
    D2 --> D3[Input: Telefone]
    D3 --> D4[Input: Data Nascimento]
    D4 --> D5[Salvar Usuário]
    D5 --> B
    
    %% Cadastro de Livro
    C -->|2| E[Cadastrar Livro]
    E --> E1[Input: Título]
    E1 --> E2[Input: Autor]
    E2 --> E3[Input: ISBN]
    E3 --> E4[Input: Categoria]
    E4 --> E5[Input: Ano Publicação]
    E5 --> E6[Salvar Livro]
    E6 --> B
    
    %% Sistema de Empréstimo
    C -->|3| F[Cadastrar Empréstimo]
    F --> F1[Input: CPF]
    F1 --> F2[Input: Título]
    F2 --> F3{Verificar Disponibilidade}
    F3 -->|Disponível| F4[Realizar Empréstimo]
    F3 -->|Indisponível| F5[Adicionar à Fila]
    F4 --> B
    F5 --> B
    
    %% Sistema de Devolução
    C -->|4| G[Cadastrar Devolução]
    G --> G1[Input: CPF]
    G1 --> G2[Input: Título]
    G2 --> G3{Verificar Empréstimo}
    G3 -->|Válido| G4[Realizar Devolução]
    G4 --> G5{Tem Fila?}
    G5 -->|Sim| G6[Notificar Próximo]
    G5 -->|Não| B
    G6 --> B
    G3 -->|Inválido| B
    
    %% Histórico por Livro
    C -->|5| H[Ver Histórico por Livro]
    H --> H1{Tem Empréstimos?}
    H1 -->|Sim| H2[Mostrar Empréstimos]
    H1 -->|Não| H3[Mostrar Mensagem]
    H2 --> B
    H3 --> B
    
    %% Histórico por Usuário
    C -->|6| I[Ver Histórico por Usuário]
    I --> I1{Tem Empréstimos?}
    I1 -->|Sim| I2[Mostrar Empréstimos]
    I1 -->|Não| I3[Mostrar Mensagem]
    I2 --> B
    I3 --> B
    
    %% Ver Categorias
    C -->|7| J[Ver Categorias]
    J --> J1{Tem Categorias?}
    J1 -->|Sim| J2[Listar Categorias]
    J1 -->|Não| J3[Mostrar Mensagem]
    J2 --> B
    J3 --> B
    
    %% Sair
    C -->|8| K[Sair]
    K --> L[Fim]
    
    %% Opção Inválida
    C -->|Inválido| M[Mostrar Erro]
    M --> B

    %% Estilo
    classDef default fill:#f9f,stroke:#333,stroke-width:2px
    classDef process fill:#bbf,stroke:#333,stroke-width:2px
    classDef decision fill:#dfd,stroke:#333,stroke-width:2px
    
    class C,F3,G3,G5,H1,I1,J1 decision
    class D,E,F,G,H,I,J,K process
```

# Sistema Biblioteca SENAI - Fluxograma Detalhado

Este fluxograma representa o funcionamento completo do Sistema de Biblioteca SENAI, incluindo:

1. **Cadastros Básicos**
   - Cadastro de Usuários
   - Cadastro de Livros

2. **Sistema de Empréstimos**
   - Verificação de disponibilidade
   - Sistema de fila de espera
   - Notificação automática

3. **Sistema de Devoluções**
   - Verificação de empréstimo
   - Processamento da fila de espera
   - Notificação do próximo usuário

4. **Consultas e Relatórios**
   - Histórico por livro
   - Histórico por usuário
   - Lista de categorias

5. **Controle de Fluxo**
   - Validações
   - Mensagens de erro
   - Retorno ao menu principal 