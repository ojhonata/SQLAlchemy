import sqlalchemy as sa
import sqlalchemy.orm as orm
from typing import List, Optional
from datetime import datetime

from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

# Picolé pode ter vários ingredientes
ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey('ingredientes.id'))
)

# Picolé pode ter vários conservantes
conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_conservantes', sa.Integer, sa.ForeignKey('conservantes.id'))
)

# Picolé pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id')),
    sa.Column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey('aditivos_nutritivos.id'))
)


class Picole(ModelBase):
    __tablename__: str = 'picoles'
    __allow_unmapped__ = True

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    preco: float = sa.Column(sa.DECIMAL(8, 2), nullable=True)

    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey('sabores.id'))
    sabor: Sabor = orm.relationship('Sabor', lazy='joined')

    id_tipo_embalagem: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: TipoEmbalagem = orm.relationship('TipoEmbalagem', lazy='joined')

    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined')

    # um picolé pode ter vários ingredientes
    ingredientes: List[Ingrediente] = orm.relationship('Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='joined')

    # um picolé pode ter vários conservantes ou mesmo nenhum
    conservantes: Optional[List[Conservante]] = orm.relationship('Conservantes', secondary=conservantes_picole, backref='conservante', lazy='joined')

    # um picolé pode ter vários aditivos e nutritivos ou mesmo nenhum
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = orm.relationship('AditivoNutritivo', secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo', lazy='joined')

    def __repr__(self) -> int:
        return f'<Lote: {self.id}>'