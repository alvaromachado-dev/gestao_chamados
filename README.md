Gestão de Chamados - Backend em Flask com Frontend Interativo

Descrição

Este projeto é uma aplicação completa de Gestão de Chamados, composta por:

API REST desenvolvida em Python com Flask e MySQL, permitindo criar, consultar, atualizar e fechar chamados.

Front-end interativo em HTML, CSS e JavaScript, integrado com a API, para facilitar a visualização e manipulação dos chamados.

Script de análise de dados em Python (pandas), gerando estatísticas de chamados por status, categoria e tempo médio de fechamento.

Todos os horários são registrados com base no fuso horário de Brasília.


Tecnologias Utilizadas

Python 3.14

Flask

Flask-SQLAlchemy

MySQL

PyMySQL

Pandas

Pytz (controle de fuso horário)

HTML, CSS, JavaScript (frontend)


Funcionalidades
API

POST /chamados → cria um chamado

GET /chamados → lista todos os chamados

GET /chamados/<id> → retorna chamado específico

PUT /chamados/<id> → atualiza status do chamado; se for "Fechado", preenche data_fechamento automaticamente


Campos do Chamado

id → Identificador único

cliente → Nome do cliente

email → Email do cliente

categoria → Categoria do chamado

descricao → Descrição detalhada do problema

status → Aberto / Fechado

data_abertura → Timestamp de criação (horário de Brasília)

data_fechamento → Timestamp de fechamento (horário de Brasília)


Frontend

Formulário interativo para criar chamados

Lista dinâmica de chamados exibindo cliente, categoria, status e horários

Botão para fechar chamados diretamente na interface

Layout moderno, responsivo e estilizado com CSS


Como rodar localmente
1️⃣ Clonar o projeto
git clone <seu-repositorio>
cd gestao_chamados

2️⃣ Criar ambiente virtual
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Configurar banco de dados

No MySQL Workbench:

CREATE DATABASE gestao_chamados;


Atualize o app.py ou config.py com usuário e senha corretos do MySQL

5️⃣ Rodar a aplicação
python app.py


Acesse no navegador: http://127.0.0.1:5000


Testando a aplicação
Criar chamado (POST)
POST http://127.0.0.1:5000/chamados
Headers: Content-Type: application/json
Body:
{
  "cliente": "Nome completo do cliente",
  "email": "email_do_cliente@gmail.com",
  "categoria": "Suporte",
  "descricao": "Não consigo acessar o sistema"
}

Atualizar chamado para fechado (PUT)
PUT http://127.0.0.1:5000/chamados/<ID>
Body:
{
  "status": "Fechado"
}

Listar todos os chamados (GET)
GET http://127.0.0.1:5000/chamados

Consultar chamado por ID (GET)
GET http://127.0.0.1:5000/chamados/1


Testar Frontend

Abra http://127.0.0.1:5000
 no navegador

Use o formulário para criar chamados

Veja a lista dinâmica atualizar e feche chamados com um clique


Análise de dados

O script analise_chamados.py gera:

Estatísticas de chamados por status

Estatísticas de chamados por categoria

Tempo médio de abertura até fechamento

Execute:

python analise_chamados.py
