# Estudo inicial

- Instalação Python
- Criar pasta  EstudoFastAPI
- Criar arquivo main.py
- Intalação FastAPI

### Passos iniciais: 
- https://fastapi.tiangolo.com/tutorial/first-steps/

### Criação de rotas CRUD:
- Create - POST
- Read - GET
- Update - PUT
- Delete - DEL


### Integração com banco de dados com sqlite
- https://fastapi.tiangolo.com/tutorial/sql-databases/#create-an-engine


---


# Projeto: Sistema de Gerenciamento de Carros — Concessionária

## Objetivo Geral
Desenvolver uma **API REST** capaz de **gerenciar o cadastro de veículos em uma concessionária**, permitindo o registro, consulta, atualização e exclusão de informações de carros.

---

## Objetivos Específicos
- Criar uma estrutura de serviço organizada e modular (camadas: modelo, esquema, rotas, regras de negócio).  
- Implementar operações **CRUD** (Create, Read, Update, Delete) para a entidade **Carro**.  
- Garantir a persistência de dados em um banco relacional (**SQLite** ou **PostgreSQL**).  
- Utilizar o **FastAPI** para criação de endpoints e geração automática de documentação.  
- Promover boas práticas de desenvolvimento backend.  

---

## Modelo Lógico do Sistema

### **Entidade Principal: `Carro`**

| Campo | Tipo de Dado | Tamanho | Chave | Nulo | Descrição |
|--------|---------------|---------|--------|--------|------------|
| `id_carro` | Inteiro | — | PK | Não | Identificador único do carro |
| `marca` | Texto | 100 | — | Não | Marca do carro (ex: Toyota, Ford, Fiat) |
| `modelo` | Texto | 100 | — | Não | Modelo do carro (ex: Corolla, Onix) |
| `ano` | Inteiro | — | — | Não | Ano de fabricação |
| `preco` | Decimal | — | — | Não | Valor do carro |
| `cor` | Texto | 50 | — | Sim | Cor do veículo |
| `disponivel` | Booleano | — | — | Sim | Indica se o carro está disponível para venda |

---

## Requisitos Funcionais

| Código | Descrição |
|--------|------------|
| **RF01** | O sistema deve permitir cadastrar um novo carro. |
| **RF02** | O sistema deve listar todos os carros cadastrados. |
| **RF03** | O sistema deve permitir buscar um carro específico pelo seu `id_carro`. |
| **RF04** | O sistema deve permitir atualizar as informações de um carro existente. |
| **RF05** | O sistema deve permitir excluir um carro do cadastro. |
| **RF06** | O sistema deve indicar se um carro está disponível ou não para venda. |

---

## Requisitos Não Funcionais

| Código | Descrição |
|--------|------------|
| **RNF01** | A aplicação deve ser desenvolvida em **Python**, utilizando o framework **FastAPI**. |
| **RNF02** | O banco de dados pode ser **SQLite** (para desenvolvimento)
| **RNF03** | A aplicação deve seguir o padrão **RESTful**. |
| **RNF04** | A API deve conter documentação automática acessível via Swagger (`/docs`). |
| **RNF05** | O código deve estar organizado em módulos: **modelos**, **schemas**, **rotas** e **CRUD**. |
| **RNF06** | Os dados de entrada devem ser validados com **Pydantic**. |

---

## Estrutura Lógica de Pastas (Proposta)


~~~
concessionaria/
├── app/
│ ├── main.py # Ponto de entrada da aplicação
│ ├── db.py # Configuração do banco
│ ├── models.py # Definição da entidade Carro
│ ├── schemas.py # Estrutura de dados (entrada/saída)
│ ├── crud.py # Regras de negócio e persistência
│ └── routers/
│ └── cars.py # Rotas HTTP para a entidade Carro
├── requirements.txt # Dependências do projeto
└── README.md # Descrição e instruções
~~~


---

## Rotas (Endpoints) Esperadas

| Método | Endpoint | Descrição | Corpo / Parâmetros | Resposta esperada |
|---------|-----------|------------|--------------------|------------------|
| **POST** | `/cars/` | Cadastrar um novo carro | JSON com dados do carro | Objeto JSON do carro criado |
| **GET** | `/cars/` | Listar todos os carros | — | Lista JSON de carros |
| **GET** | `/cars/{id}` | Consultar um carro específico | `id` (inteiro) | Objeto JSON do carro |
| **PUT** | `/cars/{id}` | Atualizar dados de um carro | JSON com campos a atualizar | Objeto JSON atualizado |
| **DELETE** | `/cars/{id}` | Excluir um carro | `id` (inteiro) | Código 204 (sem conteúdo) |

---

## Validações Esperadas

- Campos obrigatórios: `marca`, `modelo`, `ano`, `preco`.  
- O campo `ano` deve ser um número inteiro positivo (ex: 2000–2025).  
- O campo `preco` deve ser maior que zero.  
- O campo `disponivel` deve ser booleano (`true` ou `false`).  

---

## Regras de Negócio

1. Um carro só pode ser cadastrado se todos os campos obrigatórios estiverem preenchidos.  
2. O campo `disponivel` indica se o carro está em estoque.  
3. Caso um carro seja vendido (em futuras versões), o campo `disponivel` deverá ser marcado como `false`.  

---

## Tarefas dos Mentorados

Os mentorados deverão:

1. Configurar o ambiente Python e instalar as dependências.  
2. Criar a estrutura de pastas conforme o modelo lógico.  
3. Definir o modelo de banco (`models.py`) conforme a tabela `Carro`.  
4. Criar as rotas e operações CRUD usando FastAPI.  
5. Garantir a persistência em banco SQLite.  
6. Testar a aplicação via Swagger UI.  
7. (Opcional) Adicionar novas funcionalidades, como filtros por marca ou faixa de preço.  

---