from typing import List
from sqlalchemy import func # Função de agregação

from conf.helpers import formata_data
from conf.db_session import create_session

from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

from models.picole import Picole

# select simples - SELECT * FROM aditivos_nutritivos
def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        # forma 1
        # aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)

        # forma 2 retorna uma lista
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()

        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fómula Química: {an.formula_quimica}')
            print()

# SELECT * FROM sabores WHERE sabor.id == id_sabor
def select_filtro_sabor(id_sabor: int) -> None:
    with create_session() as session:
        #forma 1 retorna None caso não encontre
        #sabor: List[Sabor] = session.query(Sabor).filter(Sabor.id == id_sabor).first()

        #forma 2 retorna None caso não encontre (Recomendado)
        #sabor: List[Sabor] = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        #forma 3 retorna exec.NoResultFound caso não encontre
        #sabor: List[Sabor] = session.query(Sabor).filter(Sabor.id == id_sabor).one()

        # forma 4 usando WHERE ao invés de filter (one(), one_or_none(), first()) podemos usar mais de um filtro .where(filtro1, filtro2,....)
        sabor: List[Sabor] = session.query(Sabor).where(Sabor.id == id_sabor).one_or_none()

        print(f'ID: {sabor.id}')
        print(f'Data: {formata_data(sabor.data_criacao)}')
        print(f'Nome: {sabor.nome}')

def select_complexo_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Data: {formata_data(picole.data_criacao)}')
            print(f'Preço: {picole.preco}')

            print(f'ID Sabor: {picole.id_sabor}')
            print(f'Nome: {picole.sabor.nome}')

            print(f'ID Tipo Embalagem: {picole.tipo_embalagem}')
            print(f'Nome: {picole.tipo_embalagem.nome}')

            print(f'ID Tipo Picole: {picole.id_tipo_picole}')
            print(f'Nome: {picole.tipo_picole.nome}')

            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')
            print(f'Conservantes: {picole.conservantes}')

            print()

def select_order_by_sabor() -> None:
    with create_session() as session:
        #podemos usar mais de um filtro order_by(filtro1, filtro2,.....)
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')

'''SELECT * FROM picole
GROUP BY id, id_tipo_picole;
'''
def select_group_by_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()
        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')

# limitando a quantidade de exibição
def select_limit() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).limit(25)
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')

def select_agregacao() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro')
        )

        print(f'Resultado: {resultado}')

        # a função resultado é uma lista e cada função tembém é uma lista (lista dentro de uma lista)
        print(f'Soma de todos os picolés: {resultado[0][0]}')
        print(f'Média de todos os picolés: {resultado[0][1]:.2f}')
        print(f'Picolé mais barato: {resultado[0][2]}')
        print(f'Picolé mais caro: {resultado[0][3]}')

if __name__ == '__main__':
    #select_todos_aditivos_nutritivos()
    #select_filtro_sabor(10)
    #select_complexo_picole()
    #select_order_by_sabor()
    #select_group_by_picole()
    #select_limit()
    select_agregacao()