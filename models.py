from config import db
from datetime import datetime
import pytz

BRASILIA = pytz.timezone('America/Sao_Paulo')

class Chamado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Aberto')
    data_abertura = db.Column(
        db.DateTime,
        default=lambda: datetime.now(BRASILIA)
    )
    data_fechamento = db.Column(db.DateTime, nullable=True)
