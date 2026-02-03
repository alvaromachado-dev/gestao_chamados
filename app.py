from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Chamado
from datetime import datetime
import pytz

# Configuração do Flask
app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/gestao_chamados'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Servir o front-end
@app.route('/')
def index():
    return render_template("index.html")

# Listar todos os chamados
@app.route('/chamados', methods=['GET'])
def listar_chamados():
    chamados = Chamado.query.all()
    return jsonify([{
        'id': c.id,
        'cliente': c.cliente,
        'email': c.email,
        'categoria': c.categoria,
        'descricao': c.descricao,
        'status': c.status,
        'data_abertura': c.data_abertura.strftime("%Y-%m-%d %H:%M:%S") if c.data_abertura else None,
        'data_fechamento': c.data_fechamento.strftime("%Y-%m-%d %H:%M:%S") if c.data_fechamento else None
    } for c in chamados])

# Criar chamado
@app.route('/chamados', methods=['POST'])
def criar_chamado():
    data = request.json
    print("POST recebido:", data)  # debug temporário
    chamado = Chamado(
        cliente=data['cliente'],
        email=data['email'],
        categoria=data['categoria'],
        descricao=data['descricao']
    )
    db.session.add(chamado)
    db.session.commit()
    return jsonify({'mensagem': 'Chamado criado'}), 201

# Atualizar/fechar chamado
@app.route('/chamados/<int:id>', methods=['PUT'])
def atualizar_chamado(id):
    data = request.json
    chamado = Chamado.query.get_or_404(id)

    if 'status' in data:
        chamado.status = data['status']
        if data['status'] == "Fechado":
            tz = pytz.timezone('America/Sao_Paulo')
            chamado.data_fechamento = datetime.now(tz)

    db.session.commit()
    return jsonify({'mensagem': 'Chamado atualizado'})


@app.route('/chamados/<int:id>', methods=['DELETE'])
def deletar_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    db.session.delete(chamado)
    db.session.commit()
    return jsonify({'mensagem': 'Chamado deletado'}), 200


if __name__ == "__main__":
    app.run(debug=True)
