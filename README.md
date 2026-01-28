# Gestão de Chamados - Backend em Flask

## Descrição
Este projeto é uma **API REST de Gestão de Chamados** desenvolvida em **Python com Flask** e **MySQL**.  
Permite criar, consultar, atualizar e analisar chamados de suporte, com registro automático de horários.

O projeto também inclui um **script de análise de dados em Python (pandas)**, capaz de gerar estatísticas sobre status, categorias e tempo médio de fechamento.

---

## Tecnologias Utilizadas
- Python 3.14  
- Flask  
- Flask-SQLAlchemy  
- MySQL  
- PyMySQL  
- Pandas  
- Pytz (para controle de fuso horário)  

---

## Funcionalidades

### Endpoints da API
- **POST /chamados** → cria um chamado
- **GET /chamados** → lista todos os chamados
- **GET /chamados/<id>** → retorna chamado específico
- **PUT /chamados/<id>** → atualiza status do chamado; se for `"Fechado"`, preenche `data_fechamento` automaticamente

### Campos do Chamado
- `id` → Identificador único  
- `cliente` → Nome do cliente  
- `email` → Email do cliente  
- `categoria` → Categoria do chamado  
- `descricao` → Descrição detalhada do problema  
- `status` → Aberto / Fechado  
- `data_abertura` → Timestamp de criação (horário de Brasília)  
- `data_fechamento` → Timestamp de fechamento (horário de Brasília)  

---

## Como rodar localmente

### 1 Clonar o projeto
```bash
git clone <seu-repositorio>
cd gestao_chamados

### 2 Criar ambiente virtual
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac

### 3 Instalar dependências
pip install -r requirements.txt

### 4 Configurar o banco de dados
No MySQL Workbench:
CREATE DATABASE gestao_chamados;
* Atualize o config.py com usuário e senha corretos *

### 5 Rodar a API
python app.py
Acesse: http://127.0.0.1:5000


## RODANDO O TESTE

### Testando com Postman
Criar chamado (POST):
    POST http://127.0.0.1:5000/chamados
    Headers: Content-Type: application/json
    Body:
    {
    "cliente": "Nome completo do cliente",
    "email": "email_do_cliente@gmail.com",
    "categoria": "Suporte",
    "descricao": "Não consigo acessar o sistema"
    }


### Atualizar chamado para fechado (PUT)
PUT http://127.0.0.1:5000/chamados/<ID>
Body:
{
  "status": "Fechado"
}


### Listar todos os chamados (GET)
GET http://127.0.0.1:5000/chamados


### Consultar chamado por ID (GET)
GET http://127.0.0.1:5000/chamados/1


## Análise de dados
O script analise_chamados.py gera:

Estatísticas de chamados por status

Estatísticas de chamados por categoria

Tempo médio de abertura até fechamento

Execute: python analise_chamados.py


## Observação
Todos os horários são registrados com base no horário de Brasilia.