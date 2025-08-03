import sqlalchemy as sa
from typing import List
import sqlalchemy.orm as orm
from datetime import datetime
from models.model_base import ModelBase

from models.tipo_picole import TipoPicole

class Lote(ModelBase):
    __tablename__: str = 'lotes'
    __allow_unmapped__ = True

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id')) #nome-tabela.campo
    tipo_picole: List[TipoPicole] = orm.relationship('TipoPicole', lazy='joined') #cong interna SQLAlchemy
    quantidade: int = sa.Column(sa.Integer, nullable=False)

    def __repr__(self) -> int:
        return f'<Lote: {self.id}>'