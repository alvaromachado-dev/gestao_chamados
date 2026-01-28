from flask import request, jsonify
from config import create_app, db
from models import Chamado
from datetime import datetime
import pytz

BRASILIA = pytz.timezone('America/Sao_Paulo')

app = create_app()

with app.app_context():
    db.create_all()

# POST /chamados
@app.route('/chamados', methods=['POST'])
def criar_chamado():
    dados = request.json
    chamado = Chamado(
        cliente=dados['cliente'],
        email=dados['email'],
        categoria=dados['categoria'],
        descricao=dados['descricao']
    )
    db.session.add(chamado)
    db.session.commit()
    return jsonify({'mensagem': 'Chamado criado'}), 201

# GET /chamados
@app.route('/chamados', methods=['GET'])
def listar_chamados():
    chamados = Chamado.query.all()
    return jsonify([
        {
            'id': c.id,
            'cliente': c.cliente,
            'email': c.email,
            'categoria': c.categoria,
            'descricao': c.descricao,
            'status': c.status,
            'data_abertura': c.data_abertura.strftime('%Y-%m-%d %H:%M:%S'),
            'data_fechamento': str(c.data_fechamento) if c.data_fechamento else None
        } for c in chamados
    ])

# GET /chamados/<id>
@app.route('/chamados/<int:id>', methods=['GET'])
def get_chamado(id):
    c = Chamado.query.get_or_404(id)
    return jsonify({
        'id': c.id,
        'cliente': c.cliente,
        'email': c.email,
        'categoria': c.categoria,
        'descricao': c.descricao,
        'status': c.status,
        'data_abertura': c.data_abertura.strftime('%Y-%m-%d %H:%M:%S'),
        'data_fechamento': str(c.data_fechamento) if c.data_fechamento else None
    })

# PUT /chamados/<id>
@app.route('/chamados/<int:id>', methods=['PUT'])
def atualizar_chamado(id):
    c = Chamado.query.get_or_404(id)
    dados = request.json
    c.status = dados.get('status', c.status)
    if c.status.lower() == 'fechado':
        c.data_fechamento = datetime.now(BRASILIA)
    db.session.commit()
    return jsonify({'mensagem': 'Chamado atualizado'})

if __name__ == '__main__':
    app.run(debug=True)
